def showNum(lim):
	for i in range(lim):
		if i%2==0:
			print("{} even".format(i))
		elif i%2==0:
			print("{} odd".format(i))
		elif i%3==0:
			print("{} 3 mult".format(i))
		elif i%5==0:
			print("{} 5 mult".format(i))


print(showNum(20))

def showStars(num):

	for i in range(0,num):
		for j in range (0, num-i-1):
			print(end=" ")

		for k in range(0,i+1):
			print("*", end =" ")
		print()

print(showStars(5))

def floydtriangle(num):
	count=1
	for i in range(1,num+1):

		for j in range(1,i+1):

			print(count, end =" ")
			count+=1
		print()

print(floydtriangle(10))