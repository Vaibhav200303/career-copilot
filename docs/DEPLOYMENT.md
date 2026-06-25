# 🚀 Deployment Guide

This document explains how to deploy and run **Career Copilot** in a local development environment.

The project is designed to be simple to set up while following production-oriented practices such as environment-based configuration, Dockerized services, database migrations, and configurable AI models.

---

# 📑 Table of Contents

* Deployment Overview
* Prerequisites
* Project Setup
* Environment Variables
* Database Setup
* AI Model Setup
* Running the Backend
* Verifying the Deployment
* Production Considerations
* Future Deployment Targets

---

# 🌍 Deployment Overview

Career Copilot consists of four primary components.

```mermaid
flowchart LR

Client

-->

FastAPI

FastAPI

-->

PostgreSQL

FastAPI

-->

Ollama

PostgreSQL

-->

pgvector
```

Each component has a clearly defined responsibility.

| Component  | Purpose                |
| ---------- | ---------------------- |
| FastAPI    | Backend API            |
| PostgreSQL | Relational Database    |
| pgvector   | Semantic Vector Search |
| Ollama     | Local LLM Inference    |

---

# 💻 System Requirements

Before deploying Career Copilot, ensure the following software is installed.

| Software       | Recommended Version |
| -------------- | ------------------- |
| Python         | 3.11+               |
| Docker Desktop | Latest              |
| Git            | Latest              |
| Ollama         | Latest              |

---

# 📥 Clone Repository

```bash
git clone https://github.com/<your-username>/career-copilot.git

cd career-copilot
```

---

# 🐍 Create Virtual Environment

### Windows

```bash
python -m venv .venv

.venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv .venv

source .venv/bin/activate
```

---

# 📦 Install Dependencies

```bash
pip install --upgrade pip

pip install -r requirements.txt
```

---

# ⚙ Configure Environment Variables

Create a `.env` file in the project root.

Example

```env
DATABASE_URL=postgresql+psycopg2://postgres:password@localhost:5432/career_copilot_db

SECRET_KEY=replace_with_your_secret_key

ALGORITHM=HS256

ACCESS_TOKEN_EXPIRE_MINUTES=60

UPLOAD_DIR=uploads

OLLAMA_CHAT_MODEL=llama3.2:3b

OLLAMA_EMBEDDING_MODEL=nomic-embed-text
```

---

# 🐳 Start PostgreSQL

Career Copilot uses Docker to run PostgreSQL.

```bash
docker compose up -d
```

Verify the container.

```bash
docker ps
```

Expected output includes a running PostgreSQL container.

---

# 🗄 Database Migration

Initialize the database schema.

```bash
alembic upgrade head
```

Alembic automatically creates every required table.

---

# 🤖 Install Ollama

Download Ollama from

https://ollama.com

Verify installation.

```bash
ollama --version
```

---

# 📥 Download AI Models

Download the chat model.

```bash
ollama pull llama3.2:3b
```

Download the embedding model.

```bash
ollama pull nomic-embed-text
```

Verify.

```bash
ollama list
```

Expected models

* llama3.2:3b
* nomic-embed-text

---

# ▶ Run the Backend

Start FastAPI.

```bash
uvicorn app.main:app --reload
```

The server starts on

```text
http://127.0.0.1:8000
```

Swagger documentation is available at

```text
http://127.0.0.1:8000/docs
```

---

# ✅ Verify Deployment

Test the following endpoints.

| Endpoint      | Expected Result    |
| ------------- | ------------------ |
| GET /         | 200 OK             |
| GET /db-check | Database Connected |
| GET /docs     | Swagger UI         |

If all endpoints respond successfully, the backend is ready for use.

---

# Typical Usage Flow

```text
Register

↓

Login

↓

Upload Resume

↓

Create Job Description

↓

Generate Analysis

↓

Generate Roadmap

↓

Generate Interview

↓

Write Notes

↓

Save Interview Experiences

↓

Chat with Career Copilot
```

---

# Docker Components

The Docker Compose configuration currently manages

* PostgreSQL
* pgvector

FastAPI and Ollama run directly on the host machine during development.

This approach simplifies debugging while keeping the database isolated.

---

# Configuration Management

Career Copilot uses environment variables rather than hardcoded configuration.

Benefits include

* Easier deployment
* Better security
* Multiple environments
* Simple model switching

Changing the chat model only requires updating

```env
OLLAMA_CHAT_MODEL
```

No code changes are required.

---

# Health Checks

Before using the application verify

✅ PostgreSQL is running

✅ Ollama is running

✅ AI models are downloaded

✅ Database migrations applied

✅ FastAPI server started

---

# Troubleshooting

## PostgreSQL Connection Error

Ensure Docker Desktop is running.

Verify

```bash
docker ps
```

---

## Migration Error

Check

```env
DATABASE_URL
```

matches your PostgreSQL configuration.

---

## Ollama Model Missing

Download models again.

```bash
ollama pull llama3.2:3b

ollama pull nomic-embed-text
```

---

## Unauthorized Requests

Authenticate using

```text
POST /login
```

Copy the JWT token into Swagger's **Authorize** dialog.

---

## AI Generation Failure

Confirm

* Ollama service is running
* Chat model exists
* Embedding model exists

---

# Production Considerations

The current deployment targets local development.

Before deploying to production, consider adding:

* HTTPS
* Reverse Proxy (Nginx)
* Rate Limiting
* Centralized Logging
* Monitoring
* Automated Backups
* CI/CD Pipeline
* Secret Management

These improvements enhance security, reliability, and maintainability.

---

# Future Deployment Targets

Career Copilot's architecture supports deployment on platforms such as:

* AWS EC2
* DigitalOcean
* Azure Virtual Machines
* Google Compute Engine
* Self-hosted Linux servers

Because PostgreSQL, FastAPI, and Ollama are loosely coupled, each component can be scaled or migrated independently.

---

# Deployment Summary

Career Copilot is designed to be straightforward to deploy while maintaining production-oriented engineering practices.

Using Docker for PostgreSQL, environment-based configuration, Alembic migrations, and local AI inference with Ollama provides a reproducible development environment that is easy to extend and suitable for future production deployment.

---


