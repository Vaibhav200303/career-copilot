import uuid

from fastapi import FastAPI,Depends, HTTPException,File,UploadFile
from fastapi.security import OAuth2PasswordRequestForm
from app.db import engine
from sqlalchemy import text
from app.schemas import UserResponse,UserCreate,Token,UserLogin,JobDescriptionCreate,JobDescriptionResponse,SkillGapResponse,RoadmapResponse ,AnalysisResponse ,InterviewResponse  
from sqlalchemy.orm import Session
from app.db import get_db
from app.crud import create_user,create_resume,create_job_description,get_resume_by_id,get_job_description_by_id,create_analysis,get_analysis_by_id,create_roadmap,create_interview
from app.auth import authenticate_user,create_access_token,get_current_user
from app.auth import hash_password
from app.models import User
from pathlib import Path
from app.pdf_utils import extract_text_from_pdf
from app.services.ai import analyze_skill_gap
from app.services.roadmap import generate_learning_roadmap
from app.services.interview import generate_interview_questions

app=FastAPI(title="Career Copilot")

@app.get("/")
def health_check():
    return {"message":"working"}

@app.get("/db-check")
def db_health_check():
    with engine.connect() as connection:
        connection.execute(text("SELECT 1"))
    return {"message": "connection healthy"}

@app.post("/users",response_model=UserResponse,status_code=201)
def create_new_user(user:UserCreate,db:Session=Depends(get_db)):
    user_data=user.model_dump()
    user_data["hashed_password"]=hash_password(user_data.pop("password"))
    return create_user(db,user_data)


@app.post("/login",response_model=Token)
def login(form_data:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(get_db)):
    user=authenticate_user(db,form_data.username,form_data.password)
    if not user:
        raise HTTPException(status_code=401,detail="Invalid credentials")
    access_token=create_access_token(data={"sub":user.email})
    return {"access_token":access_token,"token_type":"bearer"}

@app.get("/me")
def get_me(current_user:User=Depends(get_current_user)):
    return current_user


UPLOAD_DIR=Path("uploads/resumes")
UPLOAD_DIR.mkdir(parents=True,exist_ok=True)

@app.post("/resumes")
async def upload_resume(
    db:Session=Depends(get_db),
    file:UploadFile=File(...),
    current_user:User=Depends(get_current_user)
):
    if file.content_type!="application/pdf":
        raise HTTPException(status_code=400,detail="Only PDF files are allowed")
    unique_filename=(f"{uuid.uuid4()}_{file.filename}")
    file_path=UPLOAD_DIR/unique_filename
    contents=await file.read()
    with open(file_path,"wb") as buffer:
        buffer.write(contents)
    extracted_text=extract_text_from_pdf(str(file_path))
    resume=create_resume(
        db,current_user.id,unique_filename,str(file_path),extracted_text
    )
    return {
        "id":resume.id,
        "filename":resume.file_name,
    }


@app.post("/job-description",response_model=JobDescriptionResponse,status_code=201)
def create_job(
    job:JobDescriptionCreate,
    db:Session=Depends(get_db),
    current_user:User=Depends(get_current_user)

):
    return create_job_description(
        db=db,
        user_id=current_user.id,
        job=job
    )

@app.post("/analysis/{resume_id}/{job_id}",response_model=AnalysisResponse)
def analyze_resume(
    resume_id:int,
    job_id:int,
    db:Session=Depends(get_db),
    current_user : User=Depends(get_current_user)
):
    resume=get_resume_by_id(resume_id,db)
    job=get_job_description_by_id(job_id,db)
    if not resume:
        raise HTTPException(
            status_code=404,
            detail="Resume not found"
        )

    if not job:
        raise HTTPException(
            status_code=404,
            detail="Job description not found"
        )
    if resume.user_id!= current_user.id:
        raise HTTPException(status_code=403,detail="Access denied")
    
    if job.user_id!=current_user.id:
        raise HTTPException(status_code=403,detail="Access denied")
    
    analysis=analyze_skill_gap(
        resume_text=resume.extracted_text,
        job_description=job.content
    )
    db_analysis = create_analysis(
        db=db,
        user_id=current_user.id,
        resume_id=resume.id,
        job_description_id=job.id,
        analysis=analysis
    )
    return db_analysis

@app.post("/roadmaps/{analysis_id}",response_model=RoadmapResponse,status_code=201)
def generate_roadmap(
    analysis_id:int,
    db:Session=Depends(get_db),
    current_user:User=Depends(get_current_user)
):
    analysis=get_analysis_by_id(db,analysis_id)
    if not analysis:
        raise HTTPException(
            status_code=404,
            detail="Analysis not found"
        )

    if analysis.user_id != current_user.id:
        raise HTTPException(
            status_code=403,
            detail="Access denied"
        )
    roadmap_content = generate_learning_roadmap(
        analysis.missing_skills
    )
    roadmap = create_roadmap(
        db=db,
        user_id=current_user.id,
        analysis_id=analysis.id,
        content=roadmap_content.model_dump()
    )
    return roadmap_content


@app.post(
    "/interviews/{analysis_id}",
    response_model=InterviewResponse,
    status_code=201
)
def generate_interview(
    analysis_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    analysis = get_analysis_by_id(
        db,
        analysis_id
    )
    if not analysis:
        raise HTTPException(
            status_code=404,
            detail="Analysis not found"
        )

    if analysis.user_id != current_user.id:
        raise HTTPException(
            status_code=403,
            detail="Access denied"
        )
    interview = generate_interview_questions(
        matched_skills=analysis.matched_skills,
        missing_skills=analysis.missing_skills
    )
    create_interview(
        db=db,
        user_id=current_user.id,
        analysis_id=analysis.id,
        content=interview.model_dump()
    )
    return interview