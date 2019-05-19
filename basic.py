def onum(num):
	prevnum =0
	for i in range(num):
		print(prevnum+i)
		prevnum=i

print(onum(10))

def evenstr(mystr):
	count =0

	for i in mystr:
		if count%2==0:
			print(i)
		count+=1

print(evenstr("pavan"))

def removechars(mystr,num):

	return mystr[num::]

print(removechars("pavan",2))

mylist=[1,2,34,55,64,2]
if mylist[0] == mylist[len(mylist)-1]:
	print("True")
else:
	print("False")

def findname(mystr,name):
	count=0
	for i in range(len(mystr)):
		if mystr[i:i+4]== name:
			count+=1

	return count

print(findname("Emma is a writer, Emma speaks english", "Emma"))

def patter(rows):

	for i in range(1,rows+1):

		for j in range(1,i+1):

			print(i,end=" ")
		print()

patter(5)
