print("Welcome to Love Calculator!")
name1=input("What is your name?\n")
name2=input("What is their name?\n")
n1=name1.lower()
n2=name2.lower()

count2=n1.count('l')+n1.count('o')+n1.count('v')+n1.count('e')+n2.count('l')+n2.count('o')+n2.count('v')+n2.count('e')
count1=n1.count('t')+n1.count('r')+n1.count('u')+n1.count('e')+n2.count('t')+n2.count('r')+n2.count('u')+n2.count('e')
percent=count1*10+count2
if percent>90 or percent<10:
    print(f"Your score is {percent}, you go together like coke and mentos.")
elif percent>=40 and percent<=50:
    print(f"Your score is {percent}, you are alright together.")
else:
    print(f"Your score is {percent}.")