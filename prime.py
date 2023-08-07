a=int(input("Enter a number"))
d=0
if(a==2):
    print("Number is prime\n")
else:
    for i in range(3,int(a/2)):
        if(a%i==0):
            d=1
            break
    if(d==1):
        print("The number ",a," is not prime")
    else:
        print("The number is prime",a)
