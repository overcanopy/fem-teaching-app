from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# Allow your frontend to talk to backend (adjust this URL later)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://github.com/overcanopy/fem-teaching-app"],  # change "*" to your GitHub Pages URL for better security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class InputData(BaseModel):
    E: float
    nu: float
    F: float

@app.post("/simulate")
def simulate(data: InputData):
    displacement = data.F / (data.E * (1 - data.nu ** 2))
    return {"max_displacement": displacement}

