#Randomization
import random
random_int=random.randint(1,10)
print(random_int)
random_float=random.random()*5
print(random_float)
love_score =random.randint(1,100)
print(f"your love score is {love_score}")
#----------------------------------------------------------------------------------
print("This is a head or tail generator")
coin = random.randint(1,2)
if coin==1:
    print("HEAD")  
else:
    print("TAILS")

#-------------------------------------------------------------------------------------
#List
neighbours = ["Shivam","Tanmay","Yashvir","Aakashdeep","Amol"]
print(neighbours)
print(neighbours[3],neighbours[1])
print(neighbours[-1],neighbours[-5])
neighbours[4]='Gautam'
print(neighbours)
neighbours.append('Dixit')
print(neighbours)
neighbours.extend(["Sajal","Siddhant"])
print(neighbours)
#---------------------------------------------------------------------------------------
#Bankers dinner
import random
people=['shivam','amit','rohit','akash','mohit','sakshi']
total_people=len(people)
pay=random.randint(0,total_people-1)
print(f"The person to pay is {people[pay]}")
print(random.choice(people))
#----------------------------------------------------------------------------------------
mixed_people=[neighbours,people]
print(mixed_people)
#-----------------------------------------------------------------------------------------
row1=['😀','😀','😀']
row2=['😀','😀','😀']
row3=['😀','😀','😀']
map=[row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}\n")
print("Who do you want to kill?\n")
x=2
y=1
map[x][y]='☠️'
print(f"{row1}\n{row2}\n{row3}")
#----------------------------------------------------------------------------------------
#Final Project of rock paper and scissor
choice=input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors\n")
computer_choice=random.randint(0,3)
if choice==0:
    if computer_choice==0:
        print("It's a draw")
    elif    computer_choice==1:
        print("You lose")
    else:
        print("You win")
elif choice==1:
    if computer_choice==0:
        print("You win")
    elif computer_choice==1:
        print("It's a draw")
    else:
        print("You lose")
else:
    if computer_choice==0:
        print("You lose")
    elif computer_choice==1:
        print("You win")
    else:
        print("It's a draw")
#------------------------------------------------------------------------
#Day 4 ends here