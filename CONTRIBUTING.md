# Contributing to Career Copilot

First off, thank you for taking the time to contribute to Career Copilot! 🎉

Career Copilot is an AI-powered backend platform that combines modern backend engineering with Retrieval-Augmented Generation (RAG) to help users analyze resumes, identify skill gaps, generate personalized learning roadmaps, prepare for interviews, and receive AI-powered career guidance.

Every contribution—whether it's fixing a bug, improving documentation, or adding a new feature—is appreciated.

---

# Table of Contents

- Code of Conduct
- Development Setup
- Project Structure
- Branching Strategy
- Commit Messages
- Pull Requests
- Coding Standards
- Reporting Bugs
- Suggesting Features
- AI Development Guidelines

---

# Code of Conduct

By participating in this project, you agree to respect all contributors and maintain a welcoming, professional, and inclusive environment.

Please read the project's `CODE_OF_CONDUCT.md` before contributing.

---

# Getting Started

## 1. Fork the Repository

Click the **Fork** button on GitHub.

---

## 2. Clone Your Fork

```bash
git clone https://github.com/<your-username>/career-copilot.git

cd career-copilot
```

---

## 3. Create a Virtual Environment

### Windows

```bash
python -m venv .venv

.venv\Scripts\activate
```

### Linux/macOS

```bash
python3 -m venv .venv

source .venv/bin/activate
```

---

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 5. Configure Environment Variables

Copy

```text
.env.example
```

to

```text
.env
```

Update the values according to your local environment.

---

## 6. Start PostgreSQL

```bash
docker compose up -d
```

---

## 7. Run Database Migrations

```bash
alembic upgrade head
```

---

## 8. Download AI Models

```bash
ollama pull llama3.2:3b

ollama pull nomic-embed-text
```

---

## 9. Run the Application

```bash
uvicorn app.main:app --reload
```

---

# Project Structure

```
app/

├── core/

├── crud/

├── db/

├── models/

├── routers/

├── schemas/

├── services/

├── utils/

└── main.py
```

Each folder has a single responsibility.

Please keep new code within the appropriate module.

---

# Branch Naming

Create feature branches using descriptive names.

Examples

```
feature/resume-versioning

feature/conversation-search

feature/redis-cache

bugfix/chat-history

bugfix/jwt-validation

docs/api-update

refactor/document-service
```

Avoid committing directly to `main`.

---

# Commit Message Convention

Use short, descriptive commit messages.

Examples

```
feat: add conversation history endpoint

feat: implement interview experience indexing

fix: resolve JWT authentication issue

fix: prevent duplicate embeddings

docs: update deployment guide

refactor: simplify retrieval service

test: add RAG integration tests
```

Follow the format

```
type: description
```

Common commit types

- feat
- fix
- docs
- refactor
- test
- chore

---

# Pull Requests

Before submitting a Pull Request:

- Ensure the project builds successfully.
- Run database migrations if required.
- Verify Swagger documentation.
- Test affected endpoints.
- Update documentation if behavior changes.

Pull Requests should include:

- Description of the change
- Motivation
- Testing performed
- Screenshots (if applicable)
- Related issue number (if applicable)

---

# Coding Standards

## Python

- Follow PEP 8.
- Use meaningful variable names.
- Prefer type hints.
- Keep functions focused on a single responsibility.

---

## FastAPI

- Keep routers lightweight.
- Move business logic into services.
- Use dependency injection.
- Validate all requests with Pydantic.

---

## SQLAlchemy

- Define clear relationships.
- Avoid raw SQL when ORM queries are sufficient.
- Use transactions where appropriate.

---

## AI Services

- Keep prompts modular.
- Validate AI output before persistence.
- Avoid hardcoding model names.
- Read configuration from environment variables.

---

# Documentation

If your contribution changes behavior, update the appropriate documentation.

Possible files include:

- README.md
- docs/API.md
- docs/ARCHITECTURE.md
- docs/DATABASE.md
- docs/SYSTEM_DESIGN.md
- docs/DEPLOYMENT.md
- docs/TESTING.md

Documentation should remain synchronized with the implementation.

---

# Reporting Bugs

When opening an issue, include:

- Operating System
- Python version
- Database version
- Ollama version
- Error message
- Steps to reproduce
- Expected behavior
- Actual behavior

Providing detailed information helps reproduce and resolve issues more quickly.

---

# Suggesting Features

Feature requests should include:

- Problem statement
- Proposed solution
- Alternative approaches
- Potential implementation details
- Expected benefits

This helps guide discussion before implementation.

---

# AI Development Guidelines

When adding AI-powered features:

- Prefer Retrieval-Augmented Generation over prompt-only approaches.
- Reuse the existing knowledge base whenever possible.
- Keep prompts deterministic.
- Validate structured outputs before storing them.
- Ensure new knowledge sources integrate with the `documents` table.

These practices maintain consistency across AI features.

---

# Thank You

Thank you for contributing to Career Copilot.

Whether you're fixing a typo, improving documentation, or implementing a new feature, your contribution helps make the project more useful for everyone.

Happy coding! 🚀