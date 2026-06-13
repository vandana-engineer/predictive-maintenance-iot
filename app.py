from fastapi import FastAPI
from src.ingestion import collect_sensor_data
from src.preprocessing import preprocess_sensor_data
from src.predict import predict_failure

app = FastAPI(title="Predictive Maintenance API")

@app.get("/")
def home():
    return {"message": "IoT Predictive Maintenance API is running"}

@app.get("/predict")
def predict():
    sensor_data = collect_sensor_data()
    features = preprocess_sensor_data(sensor_data)
    result = predict_failure(features)

    return {
        "sensor_data": sensor_data,
        "prediction": result
    }
