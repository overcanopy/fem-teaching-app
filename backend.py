from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

# --- define web app ---
app = FastAPI()

# --- define data structure coming from the web ---
class InputData(BaseModel):
    E: float
    nu: float
    F: float

# --- define what happens when browser calls /simulate ---
@app.post("/simulate")
def simulate(data: InputData):
    # Fake "simulation" (just math)
    displacement = data.F / (data.E * (1 - data.nu ** 2))
    return {"max_displacement": displacement}

# --- run the server ---
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
