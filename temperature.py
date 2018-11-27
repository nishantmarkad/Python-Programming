#TEMPERATURE SCALE
#NISHANT MARKAD
#DIV-M,ROLL NO-39


x=int(input("Enter temperature:"))                       #input from user
y=input("is it in 'celcius' or 'farenhite'")
if y is 'celsius':                                       #if-else statement
 f=9*x/5 + 32
 print(f)
else:
 c=5/9*(x-32)
print(c)
