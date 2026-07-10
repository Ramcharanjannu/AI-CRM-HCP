# AI-First CRM HCP Module

An AI-powered Customer Relationship Management (CRM) system for Healthcare Professionals (HCPs). This project was built as part of a technical assessment using React, FastAPI, LangGraph, Groq LLM, and MySQL.

---

## Project Overview

The application enables pharmaceutical field representatives to log interactions with doctors (HCPs) using a structured form while leveraging AI to automate common CRM tasks.

The system uses LangGraph as the AI orchestration framework and Groq LLM (Gemma 2 9B) to process conversations and generate intelligent outputs.

---

## Features

### Dashboard
- View recently logged HCP interactions
- Navigate to Log Interaction page
- Access AI Assistant for testing AI tools

### Log Interaction
- Record doctor interactions
- Generate AI-powered interaction summaries
- Generate AI follow-up recommendations
- Save interactions into MySQL database

### AI Assistant
A dedicated page to test all LangGraph tools individually.

---

# LangGraph AI Tools

The project includes the following five AI tools:

### 1. Log Interaction
Converts raw doctor conversations into structured CRM interaction notes.

### 2. Edit Interaction
Improves and rewrites existing interaction records.

### 3. Search HCP
Returns a CRM-style profile of a healthcare professional.

### 4. Generate Summary
Creates a concise summary from conversation notes.

### 5. Recommend Follow-up
Suggests the next action based on the doctor's interaction.

---

# Technology Stack

## Frontend
- React
- React Router
- Axios
- CSS

## Backend
- Python
- FastAPI
- SQLAlchemy

## AI
- LangGraph
- LangChain
- Groq API
- Gemma2-9B-IT

## Database
- MySQL

---

# Project Structure

```
AI-CRM-HCP
│
├── backend
│   ├── app
│   │   ├── ai
│   │   ├── routers
│   │   ├── models
│   │   ├── schemas
│   │   ├── services
│   │   ├── database
│   │   └── main.py
│   │
│   └── requirements.txt
│
├── frontend
│   ├── src
│   │   ├── pages
│   │   ├── routes
│   │   ├── api
│   │   └── main.jsx
│   │
│   └── package.json
│
└── README.md
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/Ramcharanjannu/AI-CRM-HCP.git

cd AI-CRM-HCP
```

---

## Backend

Navigate to backend folder

```bash
cd backend
```

Create virtual environment

```bash
python -m venv venv
```

Activate virtual environment

### Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file and add:

```env
GROQ_API_KEY=YOUR_GROQ_API_KEY

DB_HOST=YOUR_DB_HOST
DB_PORT=3306
DB_USER=YOUR_DB_USER
DB_PASSWORD=YOUR_DB_PASSWORD
DB_NAME=YOUR_DATABASE
```

Run backend

```bash
uvicorn app.main:app --reload
```

Backend runs at

```
http://127.0.0.1:8000
```

Swagger Documentation

```
http://127.0.0.1:8000/docs
```

---

## Frontend

Navigate to frontend

```bash
cd frontend
```

Install packages

```bash
npm install
```

Run React

```bash
npm run dev
```

Frontend runs at

```
http://localhost:5173
```

---

# API Endpoints

## HCP

- GET /hcps/
- POST /hcps/

## Interactions

- GET /interactions/
- POST /interactions/
- PUT /interactions/{id}

## AI

- POST /ai/chat

---

# AI Workflow

User Input

↓

LangGraph Agent

↓

Tool Selection

↓

Groq LLM

↓

Response

↓

Frontend Display

---

# Author

**Ram Charan Jannu**

- GitHub: https://github.com/Ramcharanjannu
- LinkedIn: https://www.linkedin.com/in/ramcharan01/

---

# Assessment Highlights

✔ React Frontend

✔ FastAPI Backend

✔ LangGraph Agent

✔ Groq LLM Integration

✔ Five AI Tools

✔ MySQL Database

✔ AI-assisted CRM Interaction Logging

✔ Swagger API Documentation
