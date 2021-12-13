# Make a mini-budget program that:
# • Allow the user to enter revenue
# • Allow the user to enter costs
# • Allow the user to show an income / expense balance
# • Allow the user to display a budget report (all revenue and expense records with amounts)
# • Allow the user to exit the program

class Record:
    def __init__(self, type, amount):
        self.type = type
        self.amount = amount

    def __str__(self):
        return f"{self.type}: {self.amount}"


class Budget:
    def __init__(self):
        self.magazine = []

    def add_income_record(self, amount):
        income = Record("Income", amount)
        self.magazine.append(income)

    def add_expenses_record(self, amount):
        expenses = Record("Expenses", amount)
        self.magazine.append(expenses)

    def get_balance(self):
        amount = 0
        for record in self.magazine:
            if record.type == "Income":
                amount += record.amount
            if record.type == "Expenses":
                amount -= record.amount
        print(amount)

    def show_report(self):
        for record in self.magazine:
            print(f"{record.type}: {record.amount}")

budget = Budget()

while True:
    choice = int(input("1 - enter income, \n2 - enter expenses, \n3 - get balance, "
                             "\n4 - show report, \n9 - exit the program: \n"))
    if choice == 1:
        amount = float(input("Enter the amount of income: "))
        budget.add_income_record(amount)
    if choice == 2:
        amount = float(input("Enter the amount of expenses: "))
        budget.add_expenses_record(amount)
    if choice == 3:
        budget.get_balance()
    if choice == 4:
        budget.show_report()
    if choice == 9:
        print("Good bye!")
        break
