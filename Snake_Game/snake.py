'''
1 for snake
-1 for water 
0 for gun 
'''
import random
computer=random.choice([-1,0,1])
youstr=input("enter a  your choice : ")
youDict={"s":1,"w":-1,"g":0}
reverseDict={1:"snake",-1:"water",0:"Gun"}
you=youDict[youstr]

print(f"you choose{reverseDict[you]}\n computer choose  {reverseDict[computer]}")

if(computer==you):
    print('its a draw')
else:
    if(computer==-1 and you==1):
        print("you Win")
    elif(computer==-1 and you==0):
        print("you lose")
    elif(computer==1 and you==-1):
        print(" you lose")
    elif(computer==1 and you==0):
        print(" you Win")
    elif(computer==0 and you==-1):
        print(" you Win")
    elif(computer==1 and you==1):
        print(" you lose")

    else:
        print("Somthing went wrong !")
    
