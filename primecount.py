import math

def myprimecount(n):
    count=0

    def isPrime(num):
        if num <=1:
            return False
        if num == 2:
            return True
        if num>2 and num%2 ==0:
            return False
        
        maxdiv = math.floor(num **0.5)
        
        for i in range (3, 1+maxdiv,2):
            if(num %i ==0):
                return False
        
        return True
    
    for i in range (1,n):
        if isPrime(i):
            count+=1
            
            
    return count

print (myprimecount(10))