## Progress

### v0.1 – User Foundation

- FastAPI setup
- PostgreSQL integration
- SQLAlchemy ORM
- Alembic migrations
- User creation endpoint
- Password hashing
- JWT token generation
- Login endpoint
- JWT authentication

### v0.2 – Resume Upload

- Resume model with user relationship
- Protected resume upload endpoint
- PDF file validation
- Unique file naming with UUID
- Local file storage
- Resume metadata persistence
- Resume ownership tracking

### v0.3 – Resume Processing

- PDF text extraction with pypdf
- OCR fallback for scanned PDFs
- Graceful handling of encrypted PDFs
- Extracted text persistence

### v0.4 – Job Description Management

- Job description model
- User-job relationships
- Protected job description endpoint
- Job description persistence