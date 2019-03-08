class circle:

	def __init__(self,side):
		self.side =side

	def __add__(sq1,sq2):
		return ((4*sq1.side) + (4*sq2.side))

c1= circle(5)
c2= circle(10)

print("sum of circles ={}".format(c1+c2))