import random

class Bank:

	def __init__(self, acctid, name, amt):
		self.acctid = acctid
		self.name = name
		self.amt = amt

	def deposit(self, amt):
		self.amt = self.amt +amt

	def display(self):
		print("{} {} avaialble deposit is {}".format(self.acctid,self.name,self.amt))


	def withdraw (self, amt):
		self.amt = self.amt -amt

	

acct2 = Bank(12,"Pavan",100)
acct2.display()

acct3 = Bank(19,"kumar", 200)
acct3.display()

while(1):

	userinput = int(input("Enter 1 to create new account, 2 for existing account, 3 to deposit, 4 to display, 5 to quit"))

	if userinput==1:
		acctid = random.randint(1,101)
		name = input("enter name")
		dep = input("Enter deposit amount")
		acct1 = Bank(acctid, name, dep)
		acct1.display()

		

	elif userinput ==2:
		acctid = int((input("enter account id")))
		name  = (input("Enter name"))
		if (acctid == acct2.acctid and name == acct2.name):
			userinput2 = int(input("Enter 3 to deposit, 4 to display 6 to withdraw, 5 to quit"))
			if userinput2 ==3:
				dep = int(input("Enter deposit amount"))
				acct2.deposit(dep)				
			elif userinput2 ==4:
					acct2.display()
			elif userinput2 ==6:
					dep = int(input("Enter withdraw amount"))
					acct2.withdraw(dep)
		elif (acctid == acct3.acctid and name == acct3.name):
				userinput2 = int(input("Enter 3 to deposit, 4 to display 6 to withdraw, 5 to quit"))
				if userinput2 ==3:
					int(dep = input("Enter deposit amount"))
					acct3.deposit(dep)				
				elif userinput2 ==4:
					acct3.display()
				elif userinput2 ==6:
					dep = int(input("Enter withdraw amount"))
					acct3.withdraw(dep)
			
	elif userinput ==5:
		quit()
