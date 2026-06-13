# Predictive Maintenance IoT

IoT Predictive Maintenance System using FastAPI, PySpark, AWS Kinesis, PostgreSQL, and Machine Learning.

## Features
- Collects IoT sensor data
- Preprocesses temperature, vibration, and pressure readings
- Predicts machine failure risk
- Provides FastAPI prediction endpoint
- Supports future AWS Kinesis streaming integration

## Tech Stack
- Python
- FastAPI
- PySpark
- PostgreSQL
- Scikit-learn
- AWS Kinesis

## Project Structure
predictive-maintenance-iot/
├── app.py
├── requirements.txt
├── README.md
└── src/
    ├── ingestion.py
    ├── preprocessing.py
    ├── model.py
    ├── train.py
    └── predict.py

## API Endpoint
GET /predict

Returns machine health prediction based on sensor readings.
