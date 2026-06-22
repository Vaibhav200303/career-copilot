# Progress

## v0.1 – User Foundation

- FastAPI setup
- PostgreSQL integration
- SQLAlchemy ORM
- Alembic migrations
- User creation endpoint
- Password hashing with bcrypt
- JWT token generation
- Login endpoint
- JWT authentication and protected routes

---

## v0.2 – Resume Upload

- Resume model with user relationship
- Protected resume upload endpoint
- PDF file validation
- Unique file naming with UUID
- Local file storage
- Resume metadata persistence
- Resume ownership tracking

---

## v0.3 – Resume Processing

- PDF text extraction with pypdf
- OCR fallback for scanned PDFs
- Graceful handling of encrypted PDFs
- Extracted text persistence in PostgreSQL

---

## v0.4 – Job Description Management

- Job description model
- User-job relationships
- Protected job description endpoint
- Job description persistence

---

## v0.5 – Skill Gap Analysis

- Local LLM integration using Ollama
- Resume and job description comparison
- AI-generated skill gap analysis
- Structured JSON responses
- Analysis persistence in PostgreSQL

---

## v0.6 – Learning Roadmaps

- Structured AI responses using JSON
- Personalized 4-week learning roadmaps
- Roadmaps stored as JSONB
- Reuse existing analyses to reduce LLM calls

---

## v0.7 – Mock Interviews

- AI-generated interview questions
- Questions tailored to skill gap analysis
- Categorized by topic and difficulty
- Interviews stored as JSONB

---

## v0.8 – Architecture Refactor

- Router-based FastAPI architecture
- Modular SQLAlchemy models
- Modular CRUD layer
- Modular schema organization
- Service layer separation
- Security module extraction
- Scalable project structure

---

## v0.9 – Vector Search Foundation

- Dockerized PostgreSQL
- pgvector integration
- Document knowledge base model
- Vector(768) embedding storage
- Ollama embedding model integration (`nomic-embed-text`)
- Text chunking pipeline
- Embedding generation service
- Document ingestion pipeline foundation

---