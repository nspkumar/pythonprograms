def powof2(num):
	
	if num==1:
		return True
	elif num==0:
		return False
	else:
		if (num & num-1) ==0:
			return True
		else:
			return False

def powof3(num):

	if num==1:
		return True
	elif num==0:
		return False
	else:

		while num%3==0:
			if num==3:
				return True
			num/=3

		return False

def powof4(num):

	if num==1:
		return True
	elif num==0:
		return False
	else:

		while num%4==0:
			if num==4:
				return True
			num/=4

		return False


print(powof2(4))

print(powof3(9))

print(powof4(-4))




