class Car:
	Engine ="Petrol"
	Trans = "Manual"

	def __init__(self):
			print("base class")

	def display(self):
		print("This car runs on {} and has {} transmission".format(self.Engine,self.Trans))


class Maruti(Car):

	def __init__(self):
		self.year ="2018"
		print("child class")

	def manu(self):
		print("This car was manufactured in year{}".format(self.year))

zen = Maruti()

zen.manu()
zen.display()

