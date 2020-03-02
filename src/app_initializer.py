from controller.electricity_reading_controller import service as electricity_reading_service
from domain.price_plan import PricePlan
from generator.electricity_reading_generator import generate_electricity_readings
from repository.price_plan_repository import price_plan_repository

DR_EVILS_DARK_ENERGY_ENERGY_SUPPLIER = "Dr Evil's Dark Energy"
THE_GREEN_ECO_ENERGY_SUPPLIER = "The Green Eco"
POWER_FOR_EVERYONE_ENERGY_SUPPLIER = "Power for Everyone"

MOST_EVIL_PRICE_PLAN_ID = "price-plan-0"
RENEWBLES_PRICE_PLAN_ID = "price-plan-1"
STANDARD_PRICE_PLAN_ID = "price-plan-2"

NUM_METERS = 10
NUM_READINGS_AGAINST_METER = 5

def populate_random_electricity_readings():
    for index in range(NUM_METERS):
        smartMeterId = f"smart-meter-{index}"
        electricity_reading_service.store_reading({
            "smartMeterId": smartMeterId,
            "electricityReadings": generate_electricity_readings(NUM_READINGS_AGAINST_METER)
        })

def populate_price_plans():
    price_plans = [
        PricePlan(MOST_EVIL_PRICE_PLAN_ID, DR_EVILS_DARK_ENERGY_ENERGY_SUPPLIER, 10),
        PricePlan(RENEWBLES_PRICE_PLAN_ID, THE_GREEN_ECO_ENERGY_SUPPLIER, 2),
        PricePlan(STANDARD_PRICE_PLAN_ID, POWER_FOR_EVERYONE_ENERGY_SUPPLIER, 1)
    ]
    price_plan_repository.store(price_plans)

def initialize_data():
    populate_random_electricity_readings()
    populate_price_plans()