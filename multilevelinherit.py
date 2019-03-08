class A:
	majorkeys = 12

	def __init__(self):
		print("class A")

class B(A):
	wood ="tone"

	def __init__(self):
		print("B class")

class C (B):
	strings =4
	def __init__(self):
		print("this has {} made of {} and has {}".format(self.strings,self.wood,self.majorkeys))

c =C()