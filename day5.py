#Python Loops
#For Loop
for i in range(10):
    print(i)
fruits=["Apple","Peach","Pear"]
for fruit in fruits:
    print(fruit)
#-------------------------------------------------
#Average student height
student_heights = [180,150,167,198,145,172,168]
print(sum(student_heights)/len(student_heights))
av=0
for height in student_heights:
    av+=height
print(round(av/len(student_heights)))
#-------------------------------------------------
maximum_height=0
for height in student_heights:
    if height>maximum_height:
        maximum_height=height
print(maximum_height)
#--------------------------------------------------
#Fizz Buzz
#If num is divisible by 5 print buzz and if by 3 print fizz and if both print fizzbuzz
for i in range(1,101):
    if i%3==0 and i%5==0:
        print(f"{i} is FizzBuzz")
    elif i%5==0:
        print(f"{i} is Buzz")
    elif i%3==0:
        print(f"{i} is Fizz")
