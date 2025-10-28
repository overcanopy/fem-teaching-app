from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from fem_core.linear_static import run_linear_elasticity

app = FastAPI()

# Allow your frontend to talk to backend (adjust this URL later)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://github.com/overcanopy/fem-teaching-app"],  # change "*" to your GitHub Pages URL for better security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class FEMInput(BaseModel):
    E: float
    nu: float
    nx: int = 10
    ny: int = 2
    F: float = -1000.0

@app.post("/simulate")
def simulate(input: FEMInput):
    result = run_linear_elasticity(E=input.E, nu=input.nu, nx=input.nx, ny=input.ny, F=input.F)
    return {"status": "success", **result}


