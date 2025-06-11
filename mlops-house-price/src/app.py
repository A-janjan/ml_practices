from fastapi import FastAPI, Request
from pydantic import BaseModel
import joblib
import numpy as np

from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
from starlette.responses import Response

app = FastAPI()

model = joblib.load("models/model.pkl")

# Prometheus metrics
REQUEST_COUNT = Counter("api_request_count", "Total number of requests")
REQUEST_LATENCY = Histogram("api_request_latency_seconds", "Latency of API requests in seconds")

class InputData(BaseModel):
    MedInc: float
    HouseAge: float
    AveRooms: float
    AveBedrms: float
    Population: float
    AveOccup: float
    Latitude: float
    Longitude: float

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)

@app.post("/predict")
@REQUEST_LATENCY.time()
def predict(data: InputData):
    REQUEST_COUNT.inc()
    input_array = np.array([[
        data.MedInc, data.HouseAge, data.AveRooms, data.AveBedrms,
        data.Population, data.AveOccup, data.Latitude, data.Longitude
    ]])
    prediction = model.predict(input_array)[0]
    return {"predicted_price": prediction}
