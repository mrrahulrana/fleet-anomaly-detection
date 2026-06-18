# Fleet Anomaly Detection System

AI-powered fleet telemetry anomaly detection platform.

## Overview

This project detects abnormal vehicle behavior
using machine learning and telemetry analytics.

Examples:

- Overspeeding
- Excessive Idling
- Fuel Theft Indicators
- Engine Temperature Anomalies
- Route Deviations

## Planned Architecture

Telemetry Data
→ Feature Engineering
→ ML Models
→ Anomaly Detection
→ Alert Engine
→ Dashboard

## Tech Stack

- Python
- Scikit-learn
- XGBoost
- FastAPI
- PostgreSQL
- MLflow
- Streamlit

## Synthetic Fleet Data Generator

The project includes a telemetry simulator
that generates realistic fleet operational data.

Generated attributes:

- Vehicle ID
- Timestamp
- Speed
- Engine RPM
- Fuel Level
- Engine Temperature
- GPS Coordinates
- Ignition Status

## Feature Engineering

The platform generates ML-ready telemetry features including:

- Rolling average speed
- Speed variance
- RPM variance
- Temperature change rate
- Speed change rate
- RPM change rate
- Idle indicators
- High temperature indicators
- Overspeed indicators

## Anomaly Detection Model

The system uses an Isolation Forest model to identify abnormal fleet behavior.

Detected anomalies include:

- Overspeeding
- Excessive RPM
- Engine overheating
- Unusual driving patterns

Model Features:

- Speed
- RPM
- Fuel Level
- Engine Temperature
- Rolling Statistics
- Behavioral Indicators

## Model Evaluation

The anomaly detection model is evaluated against synthetic ground-truth anomaly labels.

Metrics tracked:

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix

Generated Reports:

reports/
├── classification_report.txt
├── confusion_matrix.csv
└── metrics.json

## Real-Time Prediction API

The trained Isolation Forest model is exposed via FastAPI.

Endpoints:

GET /

Health Check

POST /predict

Predict whether telemetry data represents an anomaly.

Example:

{
  "speed": 180,
  "rpm": 6200,
  "engine_temp": 140
}

Response:

{
  "anomaly": true,
  "anomaly_score": -0.2785
}

## Prediction Persistence

Every anomaly prediction is stored in PostgreSQL.

Stored attributes:

- Vehicle ID
- Speed
- RPM
- Fuel Level
- Engine Temperature
- Anomaly Result
- Anomaly Score
- Timestamp

This enables:

- Historical analysis
- Auditability
- Trend monitoring
- Dashboard reporting

## Real-Time Alert Engine

The platform generates operational alerts from incoming telemetry.

Supported alerts:

- Overspeed
- Engine Overheat
- Low Fuel
- High RPM

Alerts are:

- Persisted to PostgreSQL
- Exposed through API
- Logged for operational monitoring