class Node:
	def __init__(self,dataval=None):

		self.dataval = dataval
		self.nextval =None

class SLinkList:

	def __init__(self):
		self.headval=None

	def listprint(self):

		printval = self.headval

		while printval is not None:
			print(printval.dataval)
			printval = printval.nextval

	def addAtBeg(self,newdata):

		NewNode= Node(newdata)

		NewNode.nextval = self.headval
		self.headval = NewNode

	def addatEnd(self,newdata):
		NewNode = Node(newdata)
		if self.headval is None:
			self.headval = NewNode
			return
		myval = self.headval
		while myval.nextval:
			myval = myval.nextval

		myval.nextval = NewNode


	def addInBetween(self,middle,add):

		if middle is None:
			print("Middle node is absent")
			return

		NewNode = Node(add)

		NewNode.nextval = middle.nextval
		middle.nextval = NewNode

	def removeKey(self,remove):

		myval = self.headval

		if (myval is not None):
			if (myval.data == remove):
				self.head = myval.nextval
				myval = None
				return

		while(myval is not None):

			if myval.data == remove:
				break
			prev = myval
			myval = myval.nextval

		if myval == None:
			return

		prev.next = myval.next
		myval = None




list1= SLinkList()

list1.headval = Node("Monday")

day2= Node("Tuesday")
day3= Node("Wednesday")

list1.headval.nextval=day2
day2.nextval=day3

list1.listprint()

list1.addAtBeg("Sunday")
list1.listprint()

list1.addatEnd("Thursday")
list1.listprint()

list1.addInBetween(list1.headval.nextval,"Sunday")
list1.listprint()

list1.removeKey("Sunday")
list1.listprint()