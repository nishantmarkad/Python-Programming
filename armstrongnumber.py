#ARMSTRONG NUMBER
#NISHANT MARKAD
#DIV-M,ROLL NO-39


def armstrong_number(x):     #function called
    sum=0
    num=x 
    while x>0:
        digit=x%10           #153%10 gives 3
        sum=digit**3+sum
        x=x//10              #because we have to cube each number  153//10 gives 15
    print(sum)
    if sum==num:
       print(" Armstrong number")
    else:
       print("is not an Armstrong number")
x=int(input("enter no"))     #user input.  
result=armstrong_number(x)
print(result)


