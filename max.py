class speed:
	demerit=0
	def __init__(self,name):
		self.name = name
		
	def speedcheck(self, kmh):

		if kmh<=70:
			print("{} your speed is ok and you have {} demerit points".format(self.name,self.demerit))

		elif kmh>70:
			print("{} your speed is above 70".format(self.name))
			
			self.demerit = self.demerit + (int(((kmh -70)/5))) *2
			#self.demerit = int(self.demerit) * 2
			print("You have {} demerit points".format(self.demerit))

			if(self.demerit>=12):
				print("{} your license is suspended".format(self.name))
				quit()



def maxnum(num1,num2):


	if (num1>num2):
	
		return num1

	elif (num1<num2):	
		
		return num2

def fizzbuzz(num1):
	if(num1%3==0):
		if(num1%5==0):
			print("FizzBuzz")
		else:
			print("Fizz")

	elif(num1%5==0):
		print("Buzz")
	elif(num1%3==0 and num1%5==0):
		print("Fizzbuss")
	else:
		print(num1)

def showNum(limit):

	for item in range (0,limit):
		if item %2 ==0:
			print("{} Even".format(item))
		else:
			print("{} Odd".format(item))


def showMultiples(limit):
	sum =0
	for item in range (0,limit):
		if item %3 ==0 or item % 5==0:
			sum = sum + item
			print(sum)
	return sum


def showStars(rows):

	for item in range (rows):
		for col in range (item):
			print("*", end=" ")
		print("\n")



def showPrime(limit):

	print ("Prime numbers for the limit {} \n".format(limit))
	print ("1,2,3,")
	for item in range (4,limit):
		if (item%2 !=0):
			print(item, end=" ")




userinput1=int(input("Enter number 1"))
userinput2=int(input("Enter number 2"))

ans = maxnum(userinput1, userinput2)

print("Max number{}".format(ans))

fizzbuzz(userinput1)

speedobj = speed("pavan")

#speedobj.speedcheck(89)

showNum(20)
print(showMultiples(20))

showStars(5)

showPrime(20)
while (1):
	userinput = input("Enter your speed if you want to quit enter #")

	if userinput != "#" :
		speedobj.speedcheck(int(userinput))

	else:
		quit()



