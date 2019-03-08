class A:
	multitasking = True
	name = "linux"

	def __init__(self):
			print("class a")

class B:
	name = "Desktop"
	contact = "www.yahoo.com"

	def __init__(self):
			print("class b")

class c (B,A):
	def __init__(self):

		if (self.multitasking) == True:

			print("This OS is {} and contact{}".format(self.name,self.contact))

obj = c()

