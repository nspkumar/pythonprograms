class A:
	def method1(self):

		print("this is class A")

class B(A):
	def method1(self):
		print("this is class B")
	pass

class C(A):
	def method1(self):
		print("this is class c")

class D(B,C):
	def method1(self):
		print("this is class d")
	pass

d = D()
d.method1()
