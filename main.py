from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return "api is running"

@app.get("/BPM")
def BPM():
    return "BPM: 92"

@app.get("/oxygenation")
def oxygenation():
    return "Oxygenation: 100%"

@app.get("/temperature")
def temperature():
    return"Temperature: 37°C"

@app.get("/physicactivity")
def physicactivity():
    return "PhysicActivity: high"
