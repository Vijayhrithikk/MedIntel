# MedIntel Architecture

## Vision

MedIntel is an AI Clinical Intelligence Platform.

It does not replace an EMR/HIS/HMS.

It sits on top of existing hospital systems and intelligently retrieves,
analyzes and reasons over structured and unstructured clinical data.

---

# System Overview

                    Web UI
                  Voice Agent
                  Public API
                       │
                       ▼
               Orchestrator Agent
                       │
        ┌──────────────┼──────────────┐
        │              │              │
 Patient Tool     Document Tool    SQL Tool
        │              │              │
 PostgreSQL      Vector DB      PostgreSQL
                       │
                 Final Response

---

# Layers

Presentation Layer
------------------

Next.js
Voice API
REST API

AI Layer
--------

Planner
Tool Executor
Response Synthesizer

Business Layer
--------------

Patient Service
Document Service
Appointment Service
Billing Service

Data Layer
----------

Repositories

Storage Layer
-------------

PostgreSQL
Vector Database
File Storage

# Data Sources

| Source             | Type         | Storage    | Owner           |
| ------------------ | ------------ | ---------- | --------------- |
| Patients           | Structured   | PostgreSQL | Patient Tool    |
| Documents          | Unstructured | Chroma     | Document Tool   |
| Appointments       | Structured   | PostgreSQL | Scheduling Tool |
| Bills              | Structured   | PostgreSQL | Billing Tool    |
| Insurance Policies | Unstructured | Chroma     | Document Tool   |
| Medical Reports    | Unstructured | Chroma     | Report Tool     |
