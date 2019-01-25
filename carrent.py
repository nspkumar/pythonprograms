class Hertzrent :
	def __init__ (self,hatch,sed,su):
		self.Hatchback=hatch
		self.Sedan =sed
		self.Suv=su

	def displayCars(self):
		print("Hatchback=",self.Hatchback)
		print("Sedan=",self.Sedan)
		print("Suv=",self.Suv)


	def rentCars(self, car, days):

		if car==1:
			if self.Hatchback ==0:
				print("No hatchback avaialble")
			else:
				self.Hatchback = self.Hatchback-1
				print("Hatchback rented to you")
				return 30*days

		elif car==2:
			if self.Sedan ==0:
				print("No Sedan avaialble")
			else:
				self.Sedan = self.Sedan-1
				print("Sedan rented to you")
				return 50*days

		elif car ==3:
			if self.Suv ==0:
				print("No Suv avaialble")
			else:
				self.Suv = self.Suv-1
				print("Suv rented to you")
				return 100*days

	def returnCar(self,cart):
		if cart==1:
			if (self.Hatchback+1) > self.Hatchback:
				print("you cant return vehicle you havent rented")
			else:

				self.Hatchback = self.Hatchback+1
				print("Hatchback returned, Thank you")
			

		elif cart==2:
			if (self.Sedan+1) > self.Sedan:
				print("you cant return vehicle you havent rented")
			else:
				self.Sedan = self.Sedan+1
				print("Sedan returned, Thank you")
			

		elif cart ==3:
			if (self.Suv+1) > self.Suv:
				print("you cant return vehicle you havent rented")
			else:
				self.Suv = self.Suv+1
				print("Suv returned, Thank you")
			



rent = Hertzrent(3,2,2)

while(1):

	userinput = int(input("Enter 1 to display, 2 to rent, 3 to return, 4 to quit"))

	if userinput==1:
		rent.displayCars()

	elif userinput ==2:
		cartype = int((input("Enter 1 for hatchback, 2 for sedan, 3 for Suv")))
		numdays = int((input("Enter number of days you want to rent")))

		amount =rent.rentCars(cartype, numdays)
		print("Total cost is",amount)

	elif userinput ==3:
		cartype = int((input("Enter 1 for hatchback, 2 for sedan, 3 for Suv")))
		rent.returnCar(cartype)

	elif userinput ==4:
		quit()






		
