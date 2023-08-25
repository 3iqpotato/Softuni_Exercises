from project.loans.base_loan import BaseLoan


class MortgageLoan(BaseLoan):
    STARTER_AMOUNT = 50_000
    STARTER_INTEREST = 3.5

    def __init__(self):
        super().__init__(MortgageLoan.STARTER_INTEREST, MortgageLoan.STARTER_AMOUNT)

    def increase_interest_rate(self):
        self.interest_rate += 0.5