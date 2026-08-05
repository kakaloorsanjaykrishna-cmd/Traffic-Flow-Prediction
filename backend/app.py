from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import Routers
from routes.predict import router as predict_router
from routes.dashboard import router as dashboard_router
from routes.analytics import router as analytics_router
from routes.history import router as history_router
from routes.traffic_map import router as traffic_map_router
from routes.weather import router as weather_router
from routes.settings import router as settings_router

app = FastAPI(
    title="Traffic Flow Prediction API",
    description="AI Powered Traffic Flow Prediction using LSTM Deep Learning",
    version="2.0.0"
)

# ===================================
# CORS
# ===================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ===================================
# Register Routes
# ===================================

app.include_router(predict_router, tags=["Prediction"])
app.include_router(dashboard_router, tags=["Dashboard"])
app.include_router(analytics_router, tags=["Analytics"])
app.include_router(history_router, tags=["History"])
app.include_router(traffic_map_router, tags=["Traffic Map"])
app.include_router(weather_router, tags=["Weather"])
app.include_router(settings_router, tags=["Settings"])

# ===================================
# Home
# ===================================

@app.get("/")
def home():
    return {
        "project": "Traffic Flow Prediction",
        "version": "2.0",
        "status": "Backend Running Successfully",
        "framework": "FastAPI",
        "model": "LSTM Deep Learning"
    }

# ===================================
# Health Check
# ===================================

@app.get("/health")
def health():
    return {
        "status": "Healthy",
        "database": "Connected",
        "api": "Running"
    }

# ===================================
# API Information
# ===================================

@app.get("/info")
def info():
    return {
        "project": "Traffic Flow Prediction",
        "frontend": "Next.js 16",
        "backend": "FastAPI",
        "database": "MySQL",
        "model": "LSTM Deep Learning",
        "dataset": "100000 Records",
        "version": "2.0"
    }