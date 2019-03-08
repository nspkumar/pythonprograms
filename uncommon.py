""""
def transpose():

	lista = [[1,2,3], [4,5,6], [7,8,9]]

	#print(lista[0][0])
	#print(len(lista))


	result=[[0,0,0],[0,0,0], [0,0,0]]

	for i in range (0, len(lista)):
		for j in range(0, len(lista)):

			result[i][j] = lista[j][i]

	print(result)





def intToRoman(num):

	result=""
        reminder =1
        
        quotient=1
        
        romandict={1000:"M",900:"CM", 500:"D",400:"CD", 100:"C", 90:"XC",50:"L", 40:"XL", 10:"X",9:"IX",5:"V",4:"IV",1:"I"}
        
        
        while num>0:
            if num>=1000:
                base =1000
            elif num>=100 and num<1000:
                base =100
            elif num>=10 and num<100:
                base=10
            elif num>=1 and num<10:
                base=1
            
            
            reminder = num%base
            quotient = num//base
            
            
            if base==1000:
                for i in range(0,quotient):
                    result +=romandict[base]
            
            elif base==100 or base ==10 or base==1:
                if quotient ==9 or quotient==4 :
                    result+=romandict[(quotient*base)]
                else:
                    
                    if quotient>=5:
                        newquotient=quotient//5
                        if newquotient>0:
                            result+=romandict[(5*base)]
                            quotient-=5
                            for temp in range (0,quotient):
                                result+=romandict[base]
                    else:
                        for temp in range(0,quotient):
                            result+=romandict[base]
                        
                    
                    
            num=reminder
        return result
        


def reverse(s):
	result=list(s)
	x=len(s)-1
	for i in range(0,len(s)-1):
		
		result[x], result[i] = result[i], result[x]
		#print(result)
		x-=1

	
	return result

print(reverse("pavan"))

import math

def circle(h):
	r=10
	volume =((4*math.pi*r**3)/3) -((math.pi * h**2 *((3*r)-h))/3)

	return volume

print(circle(2))


import re

def fread():
	i=0
	file= open("words2.txt","r")
	words = file.read()
	mylist = words.replace(",", " ")
	mylist = mylist.split(" ")
	print (mylist)
	
	for items in mylist:
		print(items)
		i+=1

	print("total words ={}".format(i))


fread()


import string

def fwrite():
	mylist=[]
	con="pyhton"
	con =list(con)
	file = open("alpa.txt","w")
	slice1= string.ascii_lowercase[0::3]
	slice2= string.ascii_lowercase[1::3]
	slice3= string.ascii_lowercase[2::3]

	for s1,s2,s3 in zip(slice1,slice2,slice3):
		file.write(s1+s2+s3+"\n")

	file.close()

	for letter in string.ascii_lowercase:
		file =open(letter+".txt","w")
		file.write(letter)
		file.close()

	for letter in string.ascii_lowercase:
		file =open(letter+".txt","r")
		letter = file.read().strip("\n")
		print(letter)
		if letter in con:
			mylist.append(letter)
		file.close()

	print(mylist)
fwrite()



import json

def mulist():

	mydict ={"employees":[{"firsname":"Pavan","lastname":"kumar"},{"firsname":"Pafads","lastname":"fadsdr"}], "owners":[{"firsname":"xyz", "lastname": "xabc"}]}
	print(mydict['employees'][1]['lastname'])
	mydict['employees'].append({"firsname":"fad","lastname":"kumar"})

	#print(mydict)

	file = open("my.json","w")
	json.dump(mydict,file,indent=4)
	file.close()

	file = open("my.json","r")

	print(json.loads(file.read()))


mulist()




import webbrowser

def webbb():
	query= input("enter your search query")
	webbrowser.open("www.google.com/search?q=%s" %query)

webbb()


import csv

def xfilereader():
	linecount=0
	myfile = open("sampledata.txt","r")
	mywfile =open("newsampledata.txt","w")
	csvreader= csv.reader(myfile, delimiter=",")
	csvwriter = csv.writer(mywfile, delimiter=",")
	for row in csvreader:
		if linecount==0:
			csvwriter.writerow(["x", "y"])
			linecount+=1

		else:
			print("{} {}".format((row[0]*2), (row[1]*2)))
			csvwriter.writerow([row[0]*2, row[1]*2])
			linecount+=1


	myfile.close()
	mywfile.close()




xfilereader()




def stringrev(S):

	new=""

	if len(S) < 2:
		return S

	s = list(S)
	low = 0
	high = len(S)-1

	while low <= high:
		if s[low].isalpha() and s[high].isalpha():
			s[low],s[high] = s[high],s[low]
			low += 1
			high -= 1

		else:
			if not s[low].isalpha():
				low += 1
			if not s[high].isalpha():
				high -= 1

	
	return (new.join(s))

print(stringrev("at-aba-bad-fafda"))




def adddigi(num):

	result =0

	result= sum((int(digit)**2) for digit in str(num))

	if result <10 and result!=1:
		return False

	elif result ==1:
		return True
	else:
		return adddigi(result)


print(adddigi(18))
"""
import re
import collections


def bancount(string,banned):
	
	print(banned)
	paragraph=string.lower()
	
	words=""
	x=0

	for i in paragraph:
		if paragraph[x].isalpha() or paragraph[x].isspace():
			words+="".join(i)
			x+=1
		else:
			words+=" "
			x+=1

	words = words.split()
	print(words)

	count= collections.Counter(words)

	result=''
	best=0

	for i in count:
	    if count[i]>best and i not in banned:
	    	result = i
	    	best=count[i]
	    	

	return result
	    	
print(bancount("Bob hit a ball, the hit BALL flew far after it was hit.","hit"))