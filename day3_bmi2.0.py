height=int(input("Height in cms\n"))
weight=int(input("Weight in kg\n"))

bmi=round(weight/(height/100)**2)

if bmi<18.5:
    print("Underweight")
elif bmi<22:
    print("Normal weight")
elif bmi<25:
    print("higher end of normal weight")
else:
    print("Overweight")