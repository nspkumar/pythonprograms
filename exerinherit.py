class Furniture:
	def __init__(self):
		self.typeofwood ="teak"

	def display(self):
		print(self.typeofwood)


class chair(Furniture):
	__legs =4

	def resetwood(self):
		super().__init__()


mychair = chair()

print("type of wood ={}".format(mychair.typeofwood))



mychair.typeofwood ="matti"
print("type of wood ={}".format(mychair.typeofwood))


mychair.resetwood()

print("type of wood ={}".format(mychair.typeofwood))
