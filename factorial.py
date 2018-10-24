print("Factorial(!)")
print("Enter a number")
x=int(input())
product=1
if x==0:
    product=1
if x==1:
    product=1
while x>1:
    product=product*x
    x=x-1
print("Factorial is ",product)    
m=input("\n press the enter key to exit")
