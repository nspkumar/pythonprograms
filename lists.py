listOne = [3, 6, 9, 12, 15, 18, 21]
listTwo = [4, 8, 12, 16, 20, 24, 28]
list3=[]

odd = listTwo[1::2]
even = listOne[0::2]
list3.extend(odd)
print(list3)
list3.extend(even)
print(list3)

listOne[2]=listOne[4]
listOne.append(listOne[4])
print(listOne)

sampleList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
one=sampleList[0:3]
one =one[::-1]
two=sampleList[3:6]
two=two[::-1]
three =sampleList[6:]
three=three[::-1]

print(one)
print(two)
print(three)

mylist = [10, 20, 30, 10, 20, 40, 50]
mydict={}

for i in mylist:
	mycount= mylist.count(i)
	mydict[i]=mycount

print(mydict)

firstList = [1, 2, 3, 4, 5]
secondList = [10, 20, 30, 40, 50]

mapped = zip(firstList,secondList)
mapped= set(mapped)
print(mapped)

firstSet = {10, 30, 40 , 60, 45}
secondSet = {20, 50, 10 , 40, 55}

intersection=firstSet.intersection(secondSet)
print(intersection)
for i in intersection:
 	firstSet.remove(i)

print(firstSet)

firstSet  = {57, 83, 29}
secondSet = {57, 83, 29, 67, 73, 43, 48}

if firstSet.issubset(secondSet):
	firstSet.clear()
elif secondSet.issubset(firstSet):
	secondSet.clear()

print(firstSet)
print(secondSet)

rollNumber = [47, 64, 69, 37, 76, 83, 95, 97]
sampleDict ={'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}

for i in rollNumber:
	if i not in sampleDict.values():
		rollNumber.remove(i)

print(rollNumber)

speed ={'jan':47, 'feb':52, 'march':47, 'April':44, 'May':52, 'June':53, 'july':54, 'Aug':44, 'Sept':54}
mylist=[]

for i in speed.values():
	if i not in mylist:
		mylist.append(i)

print(mylist)

sampleList = [87, 45, 41, 65, 94, 41, 99, 94]

myset= list(set(sampleList))
print(myset)
mytup=tuple(myset)

print(max(mytup))
print(min(mytup))





