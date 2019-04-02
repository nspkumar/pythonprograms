import string

def myatoi(mystr):
    if str.isspace() or str=="":
            return 0
        
        s= str.strip()
                       
        res=0
        start=0
        end = len(s)
        sign=1
        curr=0
        
        
        if s[0] =="-":
            sign=-1
        elif s[0] =="+":
            sign=1
        
        if (s[0] =="+" or s[0]== "-"):
            start=1
        else:
            start=0
            
        
        for i in range(start,end):
            
            curr=s[i] 
                
            if curr.isdigit():
                res = 10*res +(ord(curr)- ord("0"))
                
            
                                 
            elif curr.isalpha() or curr =="\s+" or curr in string.punctuation or curr.isspace():
                break
        
        if (res *sign) >= -2**31 and (res *sign) <= 2**31:
            
            return res*sign
        
        elif (res*sign)<-2**31:
            return -2**31
        
        elif (res*sign)>2**31:
            return 2**31 
        
        else:
            return 0
            

print(myatoi("           "))