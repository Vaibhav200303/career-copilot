# 🛠 Setup Guide

This guide walks you through setting up **Career Copilot** on your local machine from scratch.

---

# 📑 Table of Contents

* System Requirements
* Clone Repository
* Create Virtual Environment
* Install Dependencies
* Install Docker
* Start PostgreSQL
* Install Ollama
* Download AI Models
* Configure Environment Variables
* Database Migration
* Run the Backend
* Access Swagger
* Verify Installation
* Common Issues

---

# 💻 System Requirements

Before starting, ensure the following software is installed.

| Software            | Version |
| ------------------- | ------- |
| Python              | 3.11+   |
| Git                 | Latest  |
| Docker Desktop      | Latest  |
| PostgreSQL (Docker) | 16+     |
| Ollama              | Latest  |

---

# 📥 Clone Repository

```bash
git clone https://github.com/<your-username>/career-copilot.git

cd career-copilot
```

---

# 🐍 Create Virtual Environment

## Windows

```bash
python -m venv .venv

.venv\Scripts\activate
```

---

## Linux / macOS

```bash
python3 -m venv .venv

source .venv/bin/activate
```

---

# 📦 Install Python Dependencies

```bash
pip install --upgrade pip

pip install -r requirements.txt
```

---

# 🐳 Install Docker Desktop

Download Docker Desktop from:

https://www.docker.com/products/docker-desktop/

Verify installation.

```bash
docker --version

docker compose version
```

---

# 🗄 Start PostgreSQL

Career Copilot uses PostgreSQL with pgvector.

Start the database.

```bash
docker compose up -d
```

Verify.

```bash
docker ps
```

You should see a PostgreSQL container running.

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

Expected output:

```text
NAME

llama3.2:3b

nomic-embed-text
```

---

# ⚙ Environment Variables

Create a file named

```text
.env
```

using

```text
.env.example
```

Example configuration:

```env
DATABASE_URL=postgresql+psycopg2://postgres:password@localhost:5432/career_copilot_db

SECRET_KEY=your-secret-key

ALGORITHM=HS256

ACCESS_TOKEN_EXPIRE_MINUTES=60

UPLOAD_DIR=uploads

OLLAMA_CHAT_MODEL=llama3.2:3b

OLLAMA_EMBEDDING_MODEL=nomic-embed-text
```

---

# 🛠 Database Migration

Run Alembic migrations.

```bash
alembic upgrade head
```

Verify tables were created.

---

# 🚀 Start the Backend

```bash
uvicorn app.main:app --reload
```

Expected output:

```text
INFO: Application startup complete.
```

---

# 📖 Swagger Documentation

Open your browser.

```
http://127.0.0.1:8000/docs
```

Swagger provides an interactive interface for testing every API endpoint.

---

# ✅ Verify Installation

The following endpoints should be accessible.

## Health Check

```
GET /
```

---

## Database Check

```
GET /db-check
```

---

## Swagger

```
/docs
```

---

# 🧪 First API Test

Create a user.

```http
POST /users
```

Example request.

```json
{
    "name":"John Doe",
    "email":"john@example.com",
    "password":"Password123"
}
```

Login.

```http
POST /login
```

Copy the JWT token and authorize inside Swagger.

You are now ready to use every protected endpoint.

---

# 📂 Project Workflow

Typical usage flow.

```
Register User

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

Add Notes

↓

Record Interview Experiences

↓

Chat with Career Copilot
```

---

# 🔍 Troubleshooting

## Docker is not running

Start Docker Desktop before executing

```bash
docker compose up -d
```

---

## Ollama not found

Verify installation.

```bash
ollama --version
```

---

## AI model not found

Download again.

```bash
ollama pull llama3.2:3b

ollama pull nomic-embed-text
```

---

## Database connection failed

Ensure the PostgreSQL container is running.

```bash
docker ps
```

---

## Migration failed

Ensure the database exists and

```
DATABASE_URL
```

matches your PostgreSQL configuration.

---

## Unauthorized (401)

Generate a JWT token using

```
POST /login
```

and click **Authorize** in Swagger.

---

## Port already in use

Change the backend port.

```bash
uvicorn app.main:app --reload --port 8001
```

---

# 🎉 Congratulations!

Career Copilot is now running locally.

Continue with:

* **API Documentation** → `docs/API.md`
* **Architecture** → `docs/ARCHITECTURE.md`
* **Testing Guide** → `docs/TESTING.md`
* **Deployment Guide** → `docs/DEPLOYMENT.md`
