def is_prime(num):
    if num<=1:
        return False
    for i in range (2,int(num**0.5)+1):
        if num %i==0:
            return False
    return True
def isperfect (num):
    if num <0:
        return False
    sqr= int(num ** 0.5)
    return sqr*sqr==num
n=int(input("enter the number"))
arr=[]
sqr2=1
sqr3=1
for i in range(0,n):
    if (is_prime(i+1)):
        arr.append(sqr2)
        sqr2*=2
    elif(isperfect(i+1)):
        arr.append(sqr3)
        sqr3*=3
    else:
        arr.append(arr[i-1]+arr[i-2]) 
print (arr[n-1])  