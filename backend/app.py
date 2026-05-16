from fastapi import FastAPI
from pydantic import BaseModel
from model import predict

from fastapi.middleware.cors import CORSMiddleware

from prometheus_client import Counter, generate_latest
from fastapi.responses import Response

# -------------------------
# App Initialization
# -------------------------
app = FastAPI(title="Resume Shortlisting MLOps System")

# -------------------------
# CORS FIX (IMPORTANT)
# -------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # allow React frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------------
# Prometheus Metrics
# -------------------------
REQUEST_COUNT = Counter("resume_requests", "Total prediction requests")

# -------------------------
# Request Schema
# -------------------------
class ResumeInput(BaseModel):
    experience: int
    skills: int
    projects: int

# -------------------------
# Routes
# -------------------------
@app.get("/")
def home():
    return {
        "message": "Resume MLOps System Running",
        "status": "healthy"
    }

@app.post("/predict")
def predict_resume(data: ResumeInput):

    # track API usage
    REQUEST_COUNT.inc()

    input_data = [
        data.experience,
        data.skills,
        data.projects
    ]

    prediction = predict(input_data)

    return {
        "prediction": "Shortlisted" if prediction == 1 else "Rejected",
        "input_received": input_data
    }

# -------------------------
# Monitoring Endpoint
# -------------------------
@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type="text/plain")