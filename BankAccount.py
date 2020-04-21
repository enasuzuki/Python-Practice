class BankAccount:
  def __init__(self, balance, deposit, withdraw, level):
    self.balance = int(balance)
    self.level = level

  def Balance(self): #function
    if self.balance >= 0:
      print("Your balance is $" + str(self.balance))

  def Deposit(self,amount_deposit): #function
    if amount_deposit > 0 and amount_deposit < 2000 and self.level == "Blonde":
      self.balance += amount_deposit
      print("Done! Your balance is $" + str(self.balance))
    elif amount_deposit > 0 and amount_deposit < 3000 and self.level == "Silver":
      self.balance += amount_deposit
      print("Done! Your balance is $" + str(self.balance))
    elif amount_deposit > 0 and amount_deposit < 5000 and self.level == "Gold":
      self.balance += amount_deposit
      print("Done! Your balance is $" + str(self.balance))
    else: 
      self.balance = self.balance
      print("The amount is over the maximum.")

  def Withdraw(self,amount_withdraw):
    if amount_withdraw > 0 and self.balance > amount_withdraw:
      self.balance -= amount_withdraw
      print("Done! Your balance is $" + str(self.balance))
    else:
      self.balance = self.balance
      print("Your balance doesn't have enough money.")

  def LevelUp(self, level_up):
    self.level = ""
    if level_up == 1:
      self.level = "Blonde"
      print ("You are upgraded to " + self.level)
    elif level_up == 2:
      self.level = "Silver"
      print ("You are upgraded to " + self.level)
    elif level_up == 3:
      self.level = "Gold"
      print ("You are upgraded to " + self.level)
    else:
      print("There is an error with your input.")


Ena = BankAccount(200,"","","Blonde")
activity = 0

while activity != 9:
  activity = int(input("What do you want to do? \n1 for checking balance \n2 for deposit \n3 for withdraw \n4 for level up\n9 for quit \n"))
  if activity == 1:
    Ena.Balance()
  elif activity == 2:
    amount_deposit = int(input("How much do you want to deposit? ")) #varuable 
    Ena.Deposit(amount_deposit)
  elif activity == 3:
    amount_withdraw = int(input("How much do you want to withdraw? ")) #varuable
    Ena.Withdraw(amount_withdraw)
  elif activity == 4:
    level_up = int(input("1 for Blonde: deposit up to $2000\n2 for Silver: deposit up to $3000\n3 for Gold: deposit up to $5000\n"))
    Ena.LevelUp(level_up)

  elif activity == 9:
    print("Thank you")
  else:
    print("Error, try again!")
