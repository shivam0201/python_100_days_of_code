print("Small Pizza: $15\nMedium Pizza: $25\n:Large Pizza: $35")
print("Pepperoni for Small Pizza : +$2")
print("Pepperoni for Medium or Large Pizza : +$3")
print("Extra cheese: +$1")

size=input("Size = \n")
add_pepperoni=input("Add_Pepperoni = \n")
extra_cheese=input("Extra_Cheese = \n")

bill=0
if size == "S":
    bill=15
    if add_pepperoni == 'Y':
        bill+=2
else:
    if size=='M':
        bill=25
    elif size=='L':
        bill=35
    if add_pepperoni=='Y':
        bill+=3
if extra_cheese=='Y':
    bill+=1
print(f"Your final bill is ${bill}")
