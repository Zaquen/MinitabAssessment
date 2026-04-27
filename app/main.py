"""
FastAPI service providing statistical calculations supported by Pydantic validation

Endpoints:
- POST /mean: returns mean of a list of numbers
- POST /stddev: returns population standard deviation
- GET /health: health check endpoint
"""

import math
import logging
from fastapi import FastAPI
from pydantic import BaseModel, field_validator
from typing import List

# Setup Items
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] [%(name)s] %(message)s"
)

logger = logging.getLogger(__name__)
app = FastAPI()

class NumbersRequest(BaseModel):
    """Pydantic Data Validation for a list of floating point numbers"""
    numbers: List[float]

    @field_validator("numbers")
    @classmethod
    def validate_numbers(cls, v):
        """Custom validation to ensure the list contains at least one number"""
        if not v:
            logger.error("Empty list provided in request")
            raise ValueError("List must not be empty")
        
        return v


def get_mean(nums: List[float]) -> float:
    """Calculates the mean from a list of numbers"""
    return sum(nums) / len(nums)


@app.post("/mean")
def mean(request: NumbersRequest):
    """Returns the mean of a list of numbers"""
    logger.info("Processing /mean request")

    nums = request.numbers
    logger.debug(f"Received {len(nums)} numbers")


    mean_val = round(get_mean(nums), 3)
    logger.debug(f"Mean Value, rounded: {mean_val}")

    return {"mean": mean_val}


@app.post("/stddev")
def stddev(request: NumbersRequest):
    """Returns the population standard deviation from a list of numbers"""
    logger.info("Processing /stddev request")

    nums = request.numbers
    logger.debug(f"Received {len(nums)} numbers")

    mean_val = get_mean(nums)
    logger.debug(f"Mean Value: {mean_val}")

    # Population variance, divide by N
    variance = sum((num - mean_val) ** 2 for num in nums) / len(nums)
    logger.debug(f"Variance: {variance}")

    stddev_val = round(math.sqrt(variance), 3)
    logger.debug(f"Standard Deviation, rounded: {stddev_val}")

    return {"stddev": stddev_val}


@app.get("/health")
def health():
    """Health check endpoint"""    
    return {"status": "ok"}


if __name__ == '__main__':
    import os
    import uvicorn

    port = int(os.getenv("PORT", 8000))
    logger.info(f"Starting server on port {port}")

    uvicorn.run("app.main:app", host="0.0.0.0", port=port)
