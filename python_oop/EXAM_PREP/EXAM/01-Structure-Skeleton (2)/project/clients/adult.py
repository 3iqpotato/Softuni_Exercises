from project.clients.base_client import BaseClient


class Adult(BaseClient):
    DEFAULT_INTEREST = 4

    def __init__(self, name: str, client_id: str, income: float):
        super().__init__(name, client_id, income, Adult.DEFAULT_INTEREST)

    def increase_clients_interest(self):
        self.interest += 2