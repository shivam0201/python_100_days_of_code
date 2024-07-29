# Functions with outputs
# End goal is building a simple calculator

def func(f_name,l_name):
    if f_name=="" or l_name=="":
        return "NO valid input"
    print(f"First name is {f_name.title()}")
    print(f"First name is {l_name.title()}")

func("Shivam","mISHra")

# Doctrings

"""
Docstrings are used to document functions, classes, and modules.
They are used to provide a description of what the function does, what arguments it takes
"""

def calculator(val1,symbol,val2):
    if symbol=="+":
        return val1+val2
    elif symbol=='-':
        return val1-val2
    elif symbol=='*':
        return val1*val2
    else:
        return val1/val2

first_time=0
more="y"
while True:
    if more=="y":
        if first_time==0:
            val1=int(input("Input first number:-\n"))
            first_time+=1
        symbol=input("Choose any operation :- \n +\n-\n*\n/\n")
        val2=int(input("Input second number:-\n"))
        ans=calculator(val1,symbol,val2)
        print(f"The output is: {ans}")
        val1=ans
        more=input("Want more calculation?:-\n").lower()
    else:
        break


        

