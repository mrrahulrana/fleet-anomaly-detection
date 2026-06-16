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