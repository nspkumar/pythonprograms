class power:
	def __init__(self,side):
		self.side=side

	def __pow__(side1,side2):
		return(side1.side ** side2.side)


sq1=power(2)
sq2=power(5)

print("the result is {}".format(sq1**sq2))
