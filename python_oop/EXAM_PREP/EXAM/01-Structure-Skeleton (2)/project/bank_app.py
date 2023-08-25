from project.clients.adult import Adult
from project.clients.student import Student
from project.loans.mortgage_loan import MortgageLoan
from project.loans.student_loan import StudentLoan


class BankApp:
    VALID_LOAN_TYPES = {
        'StudentLoan': StudentLoan,
        'MortgageLoan': MortgageLoan
    }

    VALID_CLIENT_TYPES = {
        'Student': Student,
        'Adult': Adult
    }

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.loans = []
        self.clients = []

    def add_loan(self, loan_type: str):
        try:
            loan = self.VALID_LOAN_TYPES[loan_type]()
        except KeyError:
            raise Exception("Invalid loan type!")
        self.loans.append(loan)
        return f"{loan_type} was successfully added."

    def add_client(self, client_type: str, client_name: str, client_id: str, income: float):
        if client_type not in self.VALID_CLIENT_TYPES:
            raise Exception("Invalid client type!")

        if self.capacity <= len(self.clients):
            return f"Not enough bank capacity."

        client = self.VALID_CLIENT_TYPES[client_type](client_name, client_id, income)
        self.clients.append(client)
        return f"{client_type} was successfully added."

    def grant_loan(self, loan_type: str, client_id: str):
        client = self.find_client_by_id(client_id)
        if self.check_if_loan_can_be_granted(loan_type, client.__class__.__name__):
            loan = self.find_loan_by_type(loan_type)
            self.loans.remove(loan)
            client.loans.append(loan)
            return f"Successfully granted {loan_type} to {client.name} with ID {client_id}."

        raise Exception("Inappropriate loan type!")

    def remove_client(self, client_id: str):
        client = self.find_client_by_id(client_id)
        if not client:
            raise Exception("No such client!")

        if len(client.loans) > 0:
            raise Exception("The client has loans! Removal is impossible!")

        self.clients.remove(client)
        return f"Successfully removed {client.name} with ID {client_id}."

    def increase_loan_interest(self, loan_type: str):
        count = 0
        for loan in self.loans:
            if loan.__class__.__name__ == loan_type:
                count += 1
                loan.increase_interest_rate()
        return f"Successfully changed {count} loans."

    def increase_clients_interest(self, min_rate: float):
        count = 0
        for client in self.clients:
            if client.interest < min_rate:
                client.increase_clients_interest()
                count += 1

        return f"Number of clients affected: {count}."

    def get_statistics(self):
        total_income = sum([c.income for c in self.clients])
        loans_in_clients = sum(len(c.loans) for c in self.clients)
        granted_sum = self.calculete_loans_sum()

        sum_of_non_granted_loans = sum(l.amount for l in self.loans)
        if len(self.clients) == 0:
            clients_interest_rate = 0
        else:
            clients_interest_rate = sum([c.interest for c in self.clients])
            clients_interest_rate /= len(self.clients)

        res = f"Active Clients: {len(self.clients)}\n"\
               f"Total Income: {total_income:.2f}\n"\
                f"Granted Loans: {loans_in_clients}, Total Sum: {granted_sum:.2f}\n"\
                f"Available Loans: {len(self.loans)}, Total Sum: {sum_of_non_granted_loans:.2f}\n"\
                f"Average Client Interest Rate: {clients_interest_rate:.2f}"

        return res



    @staticmethod
    def check_if_loan_can_be_granted(loan_type, client_type):
        if loan_type == 'StudentLoan' and client_type == 'Student':
            return True

        elif loan_type == 'MortgageLoan' and client_type == 'Adult':
            return True
        return False

    def find_client_by_id(self, client_id):
        for client in self.clients:
            if client.client_id == client_id:
                return client

    def find_loan_by_type(self, loan_type):
        for loan in self.loans:
            if loan.__class__.__name__ == loan_type:
                return loan

    def calculete_loans_sum(self):
        money = 0
        for client in self.clients:
            for loan in client.loans:
                money += loan.amount
        return money

# a = BankApp(3)
# print(a.add_loan('MortgageLoan'))
# print(a.add_loan('StudentLoan'))
# print(a.add_loan('StudentLoan'))
# print(a.add_loan('StudentLoan'))
# print(a.add_client('Adult', 'pepo', 'pppppppppp', 100))
# print(a.grant_loan('MortgageLoan', 'pppppppppp'))
# # print(a.remove_client('pppppppppp'))
# print(a.increase_loan_interest('StudentLoan'))
# print(a.increase_clients_interest(1))
bank = BankApp(3)

print(bank.add_loan('StudentLoan'))
print(bank.add_loan('MortgageLoan'))
print(bank.add_loan('StudentLoan'))
print(bank.add_loan('MortgageLoan'))


print(bank.add_client('Student', 'Peter Simmons', '1234567891', 500))
print(bank.add_client('Adult', 'Samantha Peters', '1234567000', 1000))
print(bank.add_client('Student', 'Simon Mann', '1234567999', 700))
print(bank.add_client('Student', 'Tammy Smith', '1234567555', 700))

print(bank.grant_loan('StudentLoan', '1234567891'))
print(bank.grant_loan('MortgageLoan', '1234567000'))
print(bank.grant_loan('MortgageLoan', '1234567000'))

print(bank.remove_client('1234567999'))

print(bank.increase_loan_interest('StudentLoan'))
print(bank.increase_loan_interest('MortgageLoan'))

print(bank.increase_clients_interest(1.2))
print(bank.increase_clients_interest(3.5))

print(bank.get_statistics())
