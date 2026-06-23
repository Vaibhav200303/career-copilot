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

## v1.0 – RAG Knowledge Base

- Document CRUD layer
- Generic document ingestion pipeline
- Automatic chunking and embedding generation
- Resume ingestion into vector database
- Job Description ingestion into vector database
- Analysis ingestion into vector database
- Roadmap ingestion into vector database
- Analysis and roadmap text formatting
- Multi-source knowledge base architecture
- User-scoped document storage
- End-to-end ingestion validation
- pgvector embedding verification (768 dimensions)

## v1.1 – Vector Retrieval Engine

- Query embedding generation
- Semantic similarity search with pgvector
- User-scoped vector retrieval
- Top-K document retrieval
- Retrieval service layer
- Retrieval testing endpoint
- RAG context retrieval foundation

## v1.2 – RAG Response Generation

- RAG prompt construction layer
- Context aggregation from retrieved documents
- Integration with `qwen3:8b`
- Context-aware career guidance generation
- End-to-end RAG pipeline implementation
- Retrieval + generation testing endpoint
- Multi-source context utilization
- Personalized AI career assistant foundation

## v1.3 – Knowledge Base Maintenance

- Reindex service for document regeneration
- Embedding regeneration support
- Chunking strategy upgrades
- User-scoped knowledge base rebuilding
- Overlapping chunk support (300/50)
- Knowledge base maintenance endpoint

## v1.4 – Career Copilot Chat

- Career Copilot chat endpoint
- End-to-end Retrieval-Augmented Generation (RAG)
- Context-aware career guidance
- Resume-aware responses
- Job-description-aware responses
- Analysis-aware responses
- Roadmap-aware responses
- Personalized AI career assistant

## v1.5 – Notes Knowledge Base

- Notes model and CRUD APIs
- User-owned notes
- Automatic note ingestion into knowledge base
- Automatic embedding generation for notes
- Automatic re-indexing on note updates
- Automatic vector cleanup on note deletion
- Notes integrated into Career Copilot RAG