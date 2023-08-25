from project.clients.base_client import BaseClient


class Student(BaseClient):
    DEFAULT_INTEREST = 2

    def __init__(self, name: str, client_id: str, income: float):
        super().__init__(name, client_id, income, Student.DEFAULT_INTEREST)

    def increase_clients_interest(self):
        self.interest += 1