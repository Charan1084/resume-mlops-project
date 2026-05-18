# 🔄 Project Workflow

This project implements an end-to-end MLOps workflow for a Resume Shortlisting System.

## Workflow Architecture

```text
User
 ↓
React Frontend
 ↓
FastAPI Backend
 ↓
ML Model Prediction
 ↓
Prediction Result

Backend Metrics
 ↓
Prometheus
 ↓
Grafana Dashboard


Developer
 ↓
Git Push
 ↓
GitHub Repository
 ↓
GitHub Actions (CI)
 ↓
ArgoCD (GitOps)
 ↓
Kubernetes (Minikube)
 ↓
Application Deployment


Dataset / ML Pipeline
 ↓
DVC (Data Versioning)
 ↓
Great Expectations (Data Validation)
 ↓
Feast (Feature Management)
 ↓
MLflow (Experiment Tracking)
 ↓
OpenLineage
 ↓
Marquez (Lineage Tracking)
```

## Step-by-Step Workflow

### 1. User Interaction
- User enters resume-related details through the React frontend.
- Frontend sends request to FastAPI backend.

### 2. Prediction Flow
- FastAPI receives input.
- ML model processes the data.
- Prediction result is returned to frontend.

### 3. Monitoring
- Backend exposes metrics.
- Prometheus collects metrics.
- Grafana visualizes dashboards.

### 4. CI/CD + GitOps Flow
- Developer pushes code to GitHub.
- GitHub Actions performs CI tasks.
- ArgoCD detects GitHub changes.
- Kubernetes deploys updated application automatically.

### 5. Data & ML Lifecycle Management
- DVC manages dataset versions.
- Great Expectations validates data quality.
- Feast manages features.
- MLflow tracks experiments.
- OpenLineage + Marquez track lineage and metadata.

## Technologies Used

- Frontend: React, HTML, CSS, JavaScript
- Backend: FastAPI, Python
- ML: Scikit-learn, Pandas, NumPy
- Containerization: Docker
- Orchestration: Kubernetes, Minikube
- Monitoring: Prometheus, Grafana
- CI/CD: GitHub Actions, ArgoCD
- MLOps: DVC, MLflow, Feast, Great Expectations, OpenLineage, Marquez
