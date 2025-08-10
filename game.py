import random
'''
1 for snake
-1 for water
0 for gun
'''
computer=random.choice([1,0,-1])

youstring=input("Enter your choice: ")
youDict={"s":1,"w":-1, "g":0}
reverseDict={1:"Snake",-1:"Water",0:"Gun"}

you= youDict[youstring]

#now will show the user what he chose and what computer choses
print(f"You chose: {reverseDict[you]}\n Computer chose: {reverseDict[computer]}")

if(computer==you):
    print("It's a draw")
else:
    if(computer==-1 and you==1):
        print("You won!!! Snake drank the water")
    elif(computer==1 and you==-1):  
       print("You Lose!!! Snake drank the water") 
    elif(computer==1 and you==0):  
       print("You Won!!! Snake is killed by Gun") 
    elif(computer==0 and you==1):  
       print("You Lose!!! Snake is killed by Gun") 
    elif(computer==-1 and you==0):  
       print("You Lose!!! The Gun is submerged in Water")
    elif(computer==0 and you==-1):  
       print("You Won!!! The Gun is submerged in Water") 
    else:
       print("Something went wrong.")