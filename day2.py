#print len of number using string
print(len(str(154265)))
#string indexing
print("Hello"[3])

print("123"+"456")
print(123+345)

#Boolean - True/False

#--------------------------------------------------------------------------------------

num_char=len("Shivam")
print(70+float("10.2"))
print("Your name has "+str(num_char)+" characters.")
print(type(num_char))
val=str(123)
print(type(val))
print(str(10)+str(143))

#------------------------------------------------------------------------------------------
#test
#89 -> 8+9=17
inp="89"
print(str(inp[0])+"+"+str(inp[1])+" = "+str(int(str(inp[0]))+int(str(inp[1]))))

#--------------------------------------------------------------------------------------------
print(2+2)  
print(2-2)  
print(2*2)  
print(2/2)
print(2**2)

"""
Operator preference
PEMDAS:Left to Right - Parenthesis, Exponentiation, Multiplication, Division, Addition, Subtraction
Left to Right
"""
print(3*3+3/3-3)
print(3*(3+3)/3-3)
#----------------------------------------------------------------------------------------------
#BMI calculator
weight=67
height=1.73
bmi=weight/height**2
print("Your BMI is "+str(int(bmi)))
#--------------------------------------------------------------------------------------------------
print(round(8/3,2)) #Round function rounds to nearest decimal,  round(val,places)
print(8//3)
res=84/2
res/=2  #It allows shorthand
print(res)
winn=True
#f-string
print(f"Your final result is {res} and winning is {winn}")
#-------------------------------------------------------------------------------------------------------
#Life in weeks until 90
years=67    #int(input("Whats your age?\n"))
total_days=90*365
total_weeks=90*52
total_months=90*12
days=years*365
weeks=years*52
months=years*12
print(f"You have {total_days-days} days,{total_weeks-weeks} weeks and {total_months-months} months")
#-----------------------------------------------------------------------------------------------------------
#Tip Calculator
bill=int(input("What is bill amount?\n"))
people=int(input("How many people?\n"))
tip_per=int(input("What is tip percentage?\n"))
total=tip_per/100
print(f"Each person should pay {(total/people)+(bill+(bill*total))/people}")