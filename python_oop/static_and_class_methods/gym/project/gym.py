from project.customer import Customer
from project.subscription import Subscription
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.trainer import Trainer


class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription):
        if not subscription in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id: int):
        res = []
        subscription = [s for s in self.subscriptions if s.id == subscription_id][0]
        res.append(subscription)
        customer = [c for c in self.customers if c.id == subscription.customer_id][0]
        res.append(customer)
        trainer = [t for t in self.trainers if t.id == subscription.trainer_id][0]
        plan = [p for p in self.plans if p.id == subscription.exercise_id][0]

        res.append(trainer)
        for e in self.plans:
            if e.id == plan.equipment_id:
                res.append(e)
                break
        res.append(plan)
        return '\n'.join(str(r) for r in res)

