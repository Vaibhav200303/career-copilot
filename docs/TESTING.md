#  Testing Guide

This document demonstrates how to test every major feature of Career Copilot using the interactive Swagger UI.

All examples assume the backend is running locally.

Base URL

```text
http://127.0.0.1:8000
```

Swagger UI

```text
http://127.0.0.1:8000/docs
```

---

#  Table of Contents

* Prerequisites
* Authentication
* Resume Upload
* Job Description
* Resume Analysis
* Learning Roadmap
* Mock Interview
* Notes
* Interview Experiences
* Knowledge Base
* Career Copilot
* Conversations
* Common Errors

---

#  Before You Begin

Ensure the following services are running.

| Service    | Status |
| ---------- | ------  |
| FastAPI    |Done     |
| PostgreSQL |Done     |
| Ollama     |Done     |

Verify the AI models.

```bash
ollama list
```

Expected models

* llama3.2:3b (or your configured chat model)
* nomic-embed-text

---

# Test Flow

Career Copilot is designed to be tested in the following order.

```text
Create User

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

Create Notes

↓

Create Interview Experience

↓

Chat with Career Copilot

↓

View Conversations
```

Following this order ensures that every AI feature has sufficient context.

---

# Step 1 — Create User

Endpoint

```http
POST /users
```

Example Request

```json
{
    "name":"John Doe",
    "email":"john@example.com",
    "password":"Password123"
}
```

Expected Response

```http
201 Created
```

---

# Step 2 — Login

Endpoint

```http
POST /login
```

Example

```text
username=john@example.com

password=Password123
```

Expected Response

```json
{
    "access_token":"JWT_TOKEN",
    "token_type":"bearer"
}
```

Copy the token.

Click **Authorize** inside Swagger.

Paste

```text
Bearer YOUR_TOKEN
```

---

# Step 3 — Upload Resume

Endpoint

```http
POST /resumes
```

Upload any PDF resume.

Expected Response

```http
201 Created
```

Verify

* Resume stored
* Text extracted
* Resume appears in database

---

# Step 4 — Create Job Description

Endpoint

```http
POST /job-description
```

Example

```json
{
    "title":"Backend Developer",
    "description":"Looking for a Backend Developer with Python, FastAPI, PostgreSQL, Docker, Redis, Kubernetes and AWS experience."
}
```

Expected

```http
201 Created
```

---

# Step 5 — Generate Analysis

Endpoint

```http
POST /analysis/{resume_id}/{job_id}
```

Example

```http
POST /analysis/1/1
```

Expected

```json
{
    "matched_skills":[
        "Python",
        "FastAPI"
    ],
    "missing_skills":[
        "Redis",
        "Kubernetes"
    ],
    "recommendations":[
        "Learn Redis",
        "Study Kubernetes"
    ]
}
```

Verify

* Analysis created
* Knowledge Base updated

---

#  Step 6 — Generate Roadmap

Endpoint

```http
POST /roadmaps/{analysis_id}
```

Expected

```json
{
    "weeks":[
        {
            "week":1
        }
    ]
}
```

Verify

* Roadmap saved
* Documents indexed

---

# Step 7 — Generate Interview

Endpoint

```http
POST /interviews/{analysis_id}
```

Expected

```json
{
    "questions":[
        {
            "topic":"Redis",
            "difficulty":"Medium"
        }
    ]
}
```

Verify

* Interview created
* Questions stored

---

# Step 8 — Create Note

Endpoint

```http
POST /notes
```

Example

```json
{
    "title":"Redis",
    "content":"Redis supports caching, pub/sub and persistence."
}
```

Expected

```http
201 Created
```

Verify

* Note stored
* Document indexed

---

# Step 9 — Create Interview Experience

Endpoint

```http
POST /interview-experiences
```

Example

```json
{
    "company":"Amazon",
    "role":"Software Development Engineer Intern",
    "interview_type":"Technical",
    "interview_date":"2026-06-20",
    "outcome":"Rejected",
    "questions_asked":[
        "Explain HashMap.",
        "Implement LRU Cache."
    ],
    "experience":"The interview focused heavily on backend concepts.",
    "lessons_learned":"Need stronger system design preparation."
}
```

Expected

```http
201 Created
```

Verify

* Experience stored
* Knowledge Base updated

---

# Step 10 — Chat with Career Copilot

Endpoint

```http
POST /copilot/chat
```

First message

```json
{
    "conversation_id":null,
    "message":"Summarize my resume."
}
```

Expected

```json
{
    "conversation_id":1,
    "title":"Summarize my resume.",
    "message":"..."
}
```

Second message

```json
{
    "conversation_id":1,
    "message":"What should I improve?"
}
```

Verify

* Conversation continues
* Previous context retained
* Messages stored

---

# Step 11 — Conversations

Get all

```http
GET /conversations
```

Get one

```http
GET /conversations/{id}
```

Delete

```http
DELETE /conversations/{id}
```

Verify

* Messages returned
* Conversation title
* Cascade deletion

---

# End-to-End Verification

At this stage verify that:

User created

Resume uploaded

Resume parsed

Job description stored

Analysis generated

Roadmap generated

Interview generated

Notes indexed

Interview experiences indexed

Career Copilot responds

Conversation memory works

---

# Expected Database State

After completing every step, the database should contain records in:

* users
* resumes
* job_descriptions
* analyses
* roadmaps
* interviews
* notes
* interview_experiences
* documents
* conversations
* chat_messages

---

# Common Errors

## 401 Unauthorized

Cause

Missing or invalid JWT token.

Solution

Login again and authorize in Swagger.

---

## 404 Resource Not Found

Cause

Invalid ID.

Verify

* resume_id
* job_id
* analysis_id

---

## 422 Validation Error

Cause

Missing required request fields.

Verify the request body matches the API schema.

---

## 500 AI Generation Failed

Possible causes

* Ollama not running
* Chat model unavailable
* Embedding model unavailable

Verify

```bash
ollama list
```

---

# Testing Checklist

| Feature               | Status|
| --------------------- | ----- |
| Authentication        |       |
| Resume Upload         |       |
| Job Description       |       |
| Analysis              |       |
| Roadmap               |       |
| Interview             |       |
| Notes                 |       |
| Interview Experiences |       |
| Knowledge Base        |       |
| Career Copilot        |       |
| Conversations         |       |

Complete this checklist before deploying or publishing the project.

---

# Conclusion

Following this guide verifies that every major module of Career Copilot functions correctly and that the complete AI workflow—from resume upload to personalized conversation—is operating as expected.

---


