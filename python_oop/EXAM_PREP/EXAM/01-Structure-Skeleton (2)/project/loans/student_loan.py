from project.loans.base_loan import BaseLoan


class StudentLoan(BaseLoan):
    STARTER_AMOUNT = 2000
    STARTER_INTEREST = 1.5

    def __init__(self):
        super().__init__(StudentLoan.STARTER_INTEREST, StudentLoan.STARTER_AMOUNT)

    def increase_interest_rate(self):
        self.interest_rate += 0.2

# a = StudentLoan()
# print(a.interest_rate)
# a.increase_interest_rate()
# a.increase_interest_rate()
# print(a.interest_rate)