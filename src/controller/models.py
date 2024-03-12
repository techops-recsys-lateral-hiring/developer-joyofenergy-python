from typing import List

from pydantic import BaseModel


class Readings(BaseModel):
    time: int
    reading: float


class ElectricReading(BaseModel):
    smartMeterId: str
    electricityReadings: List[Readings]


class PricePlanComparisons(BaseModel):
    pricePlanId: str
    pricePlanComparisons: List[dict]


OPENAPI_EXAMPLES = {
    "Sarah": {"value": "smart-meter-0"},
    "Peter": {"value": "smart-meter-1"},
    "Charlie": {"value": "smart-meter-2"},
    "Andrea": {"value": "smart-meter-3"},
    "Alex": {"value": "smart-meter-4"},
}
