def CountTon(num):
    num = abs(num)
    for i in range(1,num+1,5):
        print i

def factors(num):
    num =abs(num)   
    mylist= []

    for i in range (1,num+1):
        if num % i == 0:
            mylist.append(i)
            # print factors (n)
    return mylist



    
n = raw_input ("Enter an integer")
n = int(n)
## CountTon(n)
l = factors(n)
print l

        
        

