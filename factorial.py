#FACTORIAL OF A NUMBER.
#NISHANT MARKAD
#DIV-M,ROLL NO-39


print("Factorial(!)")
print("Enter a number")


x=int(input())           #user input
product=1                #initialize
if x==0:
    product=1
if x==1:
    product=1
while x>1:               #while loop 
    product=product*x
    x=x-1                #updating x
print("Factorial is ",product) 



