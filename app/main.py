from fastapi import FastAPI
from sqlalchemy import text
from app.routers import copilot
from app.db import engine
from app.routers import (
    analyses,
    auth,
    interviews,
    job_descriptions,
    resumes,
    roadmaps,
    test,
    documents
)
from app.routers import notes

app = FastAPI(title="Career Copilot")


@app.get("/")
def health_check():
    return {"message": "working"}


@app.get("/db-check")
def db_health_check():
    with engine.connect() as connection:
        connection.execute(text("SELECT 1"))

    return {"message": "connection healthy"}


app.include_router(auth.router)
app.include_router(resumes.router)
app.include_router(job_descriptions.router)
app.include_router(analyses.router)
app.include_router(roadmaps.router)
app.include_router(interviews.router)
app.include_router(test.router)
app.include_router(documents.router)
app.include_router(copilot.router)
app.include_router(notes.router)