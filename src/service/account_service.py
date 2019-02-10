class AccountService:
    plan_ids_by_meter = {
        "meter-0": "price-plan-0",
        "meter-1": "price-plan-1",
        "meter-2": "price-plan-0",
        "meter-3": "price-plan-2",
        "meter-4": "price-plan-1",
    }

    def get_price_plan(self, smart_meter_id):
        return self.plan_ids_by_meter[smart_meter_id]