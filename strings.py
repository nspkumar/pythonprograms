def midchar(mystr):

	if len(mystr)<7:
		print("enter string greater than 7 chars")

	else:
		count= (len(mystr))//2
		print(mystr[count-1:count+2])

midchar("JohnDipPeta")
midchar("Jasonay")

def midappend(mystr1,mystr2):

	midcount=len(mystr1)//2
	midcount=midcount-1

	mystr1 = mystr1[:midcount:] +mystr2+ mystr1[midcount:]
	print(mystr1)
	print(mystr2)

midappend("Chrisdem","Iamnewstring")

def mixstring(mystr1,mystr2):

	mid1=len(mystr1)//2
	mid2 = len(mystr2)//2

	print(mystr1[0]+mystr2[0]+mystr1[mid1]+mystr2[mid2]+mystr1[len(mystr1)-1]+mystr2[len(mystr2)-1])

mixstring("America","Japan")

def lowerfirst(mystr):

	lower=[]
	upper=[]

	for i in mystr:
		if i.isupper():
			upper.append(i)
		elif i.islower():
			lower.append(i)

	result ="".join (lower+upper)
	print(result)

lowerfirst("PyNaTive")

def finddigsymbchar(mystr):

	lower=0
	upper=0
	dig=0
	symb=0

	for i in mystr:
		if i.isupper():
			upper+=1
		elif i.islower():
			lower+=1
		elif i.isdigit():
			dig+=1
		else:
			symb+=1

	print("Number of upper ={}, lower={}, digits={}, symbols={}".format(upper,lower,dig,symb))

finddigsymbchar("fdjasADFDA,343")

def mixstring2(mystr1,mystr2):

	result=""

	len1=len(mystr1)
	len2=len(mystr2)

	mystr2=mystr2[::-1]

	length= len1 if len1>len2 else len2

	for i in range(length):

		if i<len1:
			result+=mystr1[i]
		if i<len2:
			result+=mystr2[i]

	print(result)

mixstring2("Pynamtive", "Website")

def strbal(mystr1,mystr2):
	Flag =False
	len1=len(mystr1)
	len2=len(mystr2)

	if len1>len2 :
		print("String is not balanced")
		
	else:
		for i in range(len1):
			for j in range(len2):

				if mystr1[i]==mystr2[j]:
					Flag=True
					break
				else:
					Flag =False

	if Flag == True:
		print("String is balanced")

	else:
		print("String is not balanced")


strbal("ynpi","Pynative")

def countoccurence(mystr1, mystr2):

	count=0
	mystr1=mystr1.lower()
	mystr2=mystr2.lower()
	mystr2=mystr2.split()
	#print(mystr2)

	for i in mystr2:
		if i == mystr1:
			count+=1

	print("{} was found {} times".format(mystr1,count))


countoccurence("usa","Born in the USA Booorn in the usa ah")

def sumandAverage(mystr):
	sum=0
	avg=0
	count=0
	mystr = mystr.split(" ")
	print(mystr)

	for i in mystr:
		if i.isdigit():
			sum = sum+ int(i)
			count+=1

	print("sum is {}".format(sum))
	avg= sum/count
	print("average is {}".format(avg))

sumandAverage("English = 78 Science = 83 Math = 68 History = 65")

def countchars(mystr):

	mydict=dict()

	for i in mystr:

		count= mystr.count(i)
		mydict[i]= count

	print(mydict)

countchars("PavanKumarNivarthiSubramanyam")








