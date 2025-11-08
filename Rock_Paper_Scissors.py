# 1 - Rock 
# (-1) Paper
#  0 for Scissors
import random
#For getting random number from 1,-1,0 we use random

computer = random.choice([1, -1, 0])

yougive = input("Enter you Choise: ")
youDict = {"r":1,"s": 0 , "p": -1}
revDict = {1:"Rock",-1:"Paper",0:"Scissors"}
you = youDict[yougive]

print(f"Your Choise: {revDict[you]}\nComputer's choise: {revDict[computer]}")

if computer==you:
    print("Its A Drawn")
else:
    if computer == 1  and you == 0:
        print("You Lost!!\nYou are Dumb")
    elif computer ==1 and you == -1:
        print("You are Winner!!\nThats What winnner's do!!")
    elif computer == -1 and you ==1:
        print("You Lost!!\nYou are Dumb")
    elif computer == -1 and you ==0:
        print("You are Winner!!\nThats What winnner's do!!")
    elif computer == 0 and you ==1:
        print("You are Winner!!\nThats What winnner's do!!")
    elif computer == 0 and you ==-1:
        print("You Lost!!\nYou are Dumb")        