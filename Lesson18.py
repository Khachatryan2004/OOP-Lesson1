# խնդիր 1
'''
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


rectangle = Rectangle(3, 4)
area = rectangle.area()
perimeter = rectangle.perimeter()

print("Area ", area)
print("Perimeter ", perimeter)
'''


# խնդիր 2
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance <= amount:
            print("You don't have much money in your account")
        else:
            self.balance -= amount

    def print_balance(self):
        print("Account Number:", self.account_number)
        print("Balance:", self.balance)


account = BankAccount("12345", 5000)

deposit_amount = float(input("Enter deposit amount:\t"))
withdraw_amount = float(input("Enter withdraw amount:\t"))

account.deposit(deposit_amount)
account.withdraw(withdraw_amount)

account.print_balance()
