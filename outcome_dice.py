#OUTCOME OF ROLLING DICE
#NISHANT MARKAD
#DIV-M,ROLL NO-39


from random import randint as rt           #import randint
def game(dice,faces):                      #function defining
    result=0
    for roll in range (0,faces):           #for loop
        result+=rt(1,faces)
    return result
result=game(2,6)
print(result)
