# Number Classification API

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)

The **Number Classification API** is a lightweight and fast API built with **FastAPI** that classifies a given number and returns its mathematical properties along with a fun fact. It is designed to be simple, efficient, and easy to use.

---

## Table of Contents
- [Features](#features)
- [API Endpoint](#api-endpoint)
- [Example Usage](#example-usage)
- [Response Format](#response-format)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Running Locally](#running-locally)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)

---

## Features
- **Number Classification**: Determines if a number is prime, perfect, or an Armstrong number.
- **Digit Sum**: Calculates the sum of the digits of the number.
- **Fun Fact**: Fetches an interesting mathematical fact about the number from the [Numbers API](http://numbersapi.com/).
- **CORS Support**: Handles Cross-Origin Resource Sharing (CORS) for seamless integration with frontend applications.
- **Fast and Lightweight**: Built with **FastAPI** for high performance and low latency.

---

## API Endpoint
### **GET** `/api/classify-number`
Classifies a number and returns its properties.

#### Query Parameters
- `number` (required): The number to classify. Must be a valid integer.

#### Example Request
```bash
GET /api/classify-number?number=371

#### Response format
```bash
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}

Technologies Used
FastAPI: A modern, fast (high-performance) web framework for building APIs with Python.

Python: The programming language used for the backend logic.

Requests: A library for making HTTP requests to fetch fun facts from the Numbers API.

Uvicorn: A lightning-fast ASGI server for serving the FastAPI app.

## Installation
-Clone the repository:
   git clone https://github.com/jeid12/numberApi.git
-Install the dependencies:
     pip install -r requirements.txt

## Running Locally     
Start the FastAPI server:

bash

uvicorn main:app --reload
Access the API locally:

Open your browser or use a tool like Postman or cURL:

bash

curl "http://127.0.0.1:8000/api/classify-number?number=371"
Explore the Swagger UI documentation:

Visit http://127.0.0.1:8000/docs in your browser.

#### Deployed on render
![Visit](![FastAPI](https://numberapi-bfmt.onrender.com)

