####################################################
####################################################
# Object Oriented Programming Challenge
####################################################
####################################################
#
# For this challenge, create a bank account class that has two attributes:
#
# * owner
# * balance
#
# and two methods:
#
# * deposit
# * withdraw
#
# As an added requirement, withdrawals may not exceed the available balance.
#
# Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.

class Account:

  name = 'Bank of Bogus'
  city = 'Apple Town'
  branch = 'Peach Branch'

  def __init__(self, owner, balance):
    self.owner = owner
    self.balance = balance
    self.record = [(self.owner, self.balance)]
    print(f'Account Created for {self.owner}')

  def deposit(self, amount):
    new_bal = self.balance + amount
    self.balance = new_bal
    self.record.append(('Deposit', amount))
    print('Transaction Recored: Deposit')
    print(f'New balance for {self.owner} is ${new_bal}')

  def withdraw(self, amount):
    # if statement to see if funds are available
    difference = self.balance - amount
    if amount > self.balance:
      print(f'Warning: Funds Not Available. Please Deposit ${abs(difference)}')
    else:
      self.record.append(('Withdrawl', amount))
      self.balance = difference
      print('Transaction Recored: Withdrawal')
      print(f'New balance for {self.owner} is ${difference}')

  def transactions(self):
    self.record.append(('Ending Balance', self.balance))
    print(f'Account Statement from {Account.name} in {Account.city} at {Account.branch}:')
    return print(self.record)

#############################
### --- Dan's Version --- ###
#############################

# from typing import Optional
# from datetime import datetime

# class Transaction:
#   def __init__(
#       self,
#       source: str,
#       destination: str,
#       starting_balance: float,
#       amount: float,
#       comment: Optional[str] = None
#   ) -> None:
#     self.timestamp = datetime.now()
#     self.source = source
#     self.destination = destination
#     self.starting_balance = starting_balance
#     self.amount = amount
#     self.ending_balance = starting_balance - amount
#     self.comment = comment

#   def __repr__(self):
#     return f'{self.timestamp}: ${self.amount} from {self.source} to {self.destination} - {self.comment}'

# class Account:
#   def __init__(self, owner: str, starting_balance: float) -> None:
#     self.owner = owner
#     self.balance = starting_balance
#     self.transactions = []

#   def add_transaction(
#       self,
#       source: str,
#       destination: str,
#       amount: float,
#       comment: Optional[str] = None
#   ) -> None:
#     self.transactions.append(
#         Transaction(source, destination, self.balance, amount, comment )
#     )
#     self.balance = self.transactions[-1].ending_balance

#   def deposit(self, amount: float, comment: Optional[str] = None) -> None:
#     self.add_transaction("Cash", self.owner, 0 - amount, comment)

#   def withdraw(self, amount: float, comment: Optional[str] = None) -> None:
#     self.add_transaction(self.owner, "Cash", amount, comment)

# acc = Account('Joe Berg', 100)
# acc.withdraw(50)
# acc.add_transaction('Work', acc.owner, 2000, 'Paycheck')
# acc.deposit(100, 'Birthday money')

# acc.transactions


#####################
### --- Tests --- ###
#####################

# 1. Instantiate the class
acct1 = Account('Jose',100)


# 2. Print the object
print(acct1)


# 3. Show the account owner attribute
print('The Account Owner is: ', acct1.owner)


# 4. Show the account balance attribute
print(f'{acct1.owner} has an account balance of $', acct1.balance)


# 5. Make a series of deposits and withdrawals
print('------')
acct1.deposit(50)


print('------')
acct1.withdraw(75)

# 6. Make a withdrawal that exceeds the available balance
print('------')
acct1.withdraw(500)

print('------')
acct1.transactions()

# # ## Good job!
