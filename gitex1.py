"""def example1():
	for item in range (2000,3002):
		if (item %7 ==0 and item%5!=0):
			print("{}".format(item))


example1()

def fact(val):
	if val ==0 or val ==1:
		return 1

	else:
		return val * fact(val-1)

print(fact(6))

def square(val):

	dict={}

	for item in range (1,val+1):
		dict[item] = item *item

	print(dict)

square(8)

def commainput(mystring):
	xlist=[]
	xtupple =()

	xlist = mystring.split(",")
	xtupple = mystring.split(",")

	print(xlist)
	print(xtupple)

	xlist.append("6443564")
	print(xlist)

commainput(str(input("Enter comma separated values")))

def printstring(mystring):

	print(mystring.upper())

printstring(input("Enter string"))


def myformula(myval):

	c=40
	d=50

	return (2*c*d*myval) ** 0.5

print(myformula(int(input("enter value of height"))))



def sortstr (mystring):
	xlist = []
	xlist = mystring.split(",")
	xlist.sort()
	print(xlist)

	for items in xlist:
		print("{},".format(items))

sortstr(str(input("enter comma separated string")))

def remdup(mystring):
	xlist=[]
	alist=[]
	#counter =0

	xlist = mystring.split(" ")

	xlist.sort()

	print(xlist)

	for items in xlist:
		counter =0
		for i in range (1, len(xlist)):
			if items != xlist[counter+i]:
				print(xlist[counter+i])
				print("equal ***")

			else:

				alist.append(items)

	print(alist)
remdup("hellow white red greeen black white hellow")


def countcase():

	dict = { "Upper":0,"Lower":0 }

	print (dict)

	user_input = str(input("enter the sentence"))

	
	xlist = user_input.split(" ")

	for items in xlist:
		for letters in items:
			if letters.isupper() == True:
				dict["Upper"]+=1
			elif letters.islower() == True:
				dict["Lower"]+=1

	print("Uppercase ={}".format(dict["Upper"]))
	print("Lowercase ={}".format(dict["Lower"]))


countcase ()


def calcbal(mystring, bal):

	mylist = mystring.split(" ")

	if mylist[0] == "D":
		return bal +int(mylist[1])
	elif mylist[0] == "W":
		return bal - int(mylist[1])

print(calcbal("W 300", 400))



def valpasswd(mystring):
	lowercounter=0
	uppercounter=0
	splcounter=0
	len=0

	for items in mystring:
		if items.isupper() == True:
			uppercounter+=1
		elif items.islower() == True:
			lowercounter+=1
		elif items == "~" or items =="!" or items=="@" or items =="#" or items =="$" or items =="%" or items =="^" or items =="&" or items=="*":
			splcounter+=1
		len+=1
	
	if lowercounter >0 and uppercounter>0 and splcounter>0 and len>= 8 and len<=12:
		print("Your password {} is ok".format(mystring))
	elif lowercounter ==0:
		print ("Your password needs to have a lower case alphabet")
	elif uppercounter==0:
		print ("Your password needs to have a upper case alphabet")
	elif splcounter ==0:
		print ("Your password needs to have spl character like ~!@#$%^&*")
	elif len<8:
		print("YOur password needs to be min 8 characters ")
	elif len>12:
		print("YOur password needs to be max 12 characters")

valpasswd("abcdEf#afadsadsfadsf")




def sorttupple():
	import operator

	mylist =[]

	mytupple=("Jon, 17, 90", "Jam, 17, 100", "Jan, 18, 90", "Jbm, 17, 91")
	print(mytupple)
	mylist = list(mytupple)
	mylist.sort(key=operator.itemgetter(0,1,2))

	print(mylist)



sorttupple()


class iter:
	range1=0

	def __init__(self):
		pass



	def iteratoryeild(self,range1):
		mylist=[]
		print(self.range1)
		for i in range (0,range1):

			if i%7 ==0:
				mylist.append(i)
				
				yield i

		print(mylist)

myiter = iter()
myiter.iteratoryeild(100)


def freq():

	user_input = input("Enter the sentence")

	freq={}

	words =[]

	for words in user_input.split(" "):
		freq[words] = freq.get(words,0)+1


	words = freq.keys()
	words.sort()

	for w in words:
		print ("{} :{}" .format(w,freq[w]))

freq()


import random

def dice():

	while(1):
		user_input= input("enter c to roll the dice or q to quit")
		if user_input == "c":

			val = random.randint(1,6)
			print("your dice roll is {}".format(val))

		elif user_input == "q":

			break


dice()

def twosum(target):

	nums = [4,2,11,15,7]
	for i in range(0, len(nums)):
		for j in range(i+1, len(nums)):
			if nums[i]+nums[j]== target:
				print("[{}, {}]".format(i,j))


twosum(9)


def numrev(num):
	rev = 0
	pop =1
	counter =0

	while (pop>0):
		pop=int(num%10)
		
		print(counter)
		if pop == 0 and counter ==0:
			yield
		elif pop ==0 and counter >0:
			break

		else:
			rev = rev *10 + pop
		#print(rev)
		num //=10
		counter+=1
	return rev

print(numrev(120))



def roman(s):
	sum =0
	counter =0

	
	romanDict ={"I":1, "V":5, "X":10, "L":50, "C":100, "D":500,"M":1000}

	for item in s:
		
		if item in romanDict:
			sum = sum + romanDict.get(item)
			

		

		if item == "I"  and counter+1 <= len(s) -1 : 
			
			if s[counter+1] =="V" or s[counter+1]=="X" :
				sum = sum - 2
			
			


		elif s[counter] == "X" and counter+1 <=len(s)-1:
			if s[counter+1]=="L" or  s[counter+1]=="C":
				sum = sum -20
			
		elif s[counter] == "C" and counter+1 <=len(s)-1:
			if s[counter+1]=="D" or  s[counter+1]=="M" :
				sum = sum - 200
			
		counter+=1
		
			
				
				

	return sum

print(roman("MCMXCIV"))

"""

def uncommon(A,B):

	lista = A.split(" ")
	listb = B.split(" ")
	mylist =[]
	counter = True
	x =0
	item =""
	#print(len(lista))
		
	for item in lista:
		for x in range (1, len(lista)):
			if item == lista[x]:
				del item
				del lista[x]

	print(lista)



uncommon("apple the and fruit apple", "banana")


