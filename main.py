from fastapi import FastAPI, Query, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import requests

from number_check import is_armstrong, is_prime, is_perfect, digit_sum

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

def get_fun_fact(n: int) -> str:
    url = f"http://numbersapi.com/{n}/math"
    response = requests.get(url)
    return response.text if response.status_code == 200 else "No fun fact available."

# API Endpoint
@app.get("/api/classify-number")
async def classify_number(number: int = Query(..., description="The number to classify")):
    if not isinstance(number, int):
        raise HTTPException(status_code=400, detail={"number": str(number), "error": True})

    properties = []
    if is_armstrong(number):
        properties.append("armstrong")
    if number % 2 == 0:
        properties.append("even")
    else:
        properties.append("odd")

    response = {
        "number": number,
        "is_prime": is_prime(number),
        "is_perfect": is_perfect(number),
        "properties": properties,
        "digit_sum": digit_sum(number),
        "fun_fact": get_fun_fact(number),
    }
    return response