#A-Z capital letters in a list
cap=[chr(i) for i in range(65,91)]
#a-z small letters in a list    
small=[chr(i) for i in range(97,123)]
#0-9 numbers in a list
num=[chr(i) for i in range(48,58)]
#special characters in a list
special=['!','@','#','$','%','^','&','*','(',')','_','-',]
#User inputs
len=int(input("How many digits in the password"))
symbols=int(input("How may symbols would you want?"))
numbers=int(input("How may numbers would you want?"))
#Password generator
password=""
import random
for char in range(1,len-symbols-numbers+1):
    password+=random.choice(cap+small)
for sym in range(1,symbols+1):
    password+=random.choice(special)
for n in range(1,numbers+1):
    password+=random.choice(num)

print(password)

passw=[]
for char in range(1,len-symbols-numbers+1):
    passw.append(random.choice(cap+small))
for sym in range(1,symbols+1):
    passw.append(random.choice(special))
for n in range(1,numbers+1):
    passw.append(random.choice(num))
print(passw)
random.shuffle(passw)
print(passw)
passcode=""
for char in passw:
    passcode+=char
print(f"The hard password is {passcode}")