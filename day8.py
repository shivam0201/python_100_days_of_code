import math

def greet():
    print("Hello")
    print("How are you?")
    print("I am fine \n")

greet()

#----------------------------------------------------------
def greet(name):    #name is a parameter that would be used by the function
    print("Hello", name)
    print("How are you?")
    print(f"Hope you have a good day Mr. {name}")

greet("Shivam") #Shivam is the argument that is being passed to the function

#------------------------------------------------------------

def info(name,location):
    print(f"Hello {name} from {location}")

info("Shivam","Satna")
info(location="Satna",name="Shivani")

#--------------------------------------------------------------------
# Paint area calculator
def paint_calc(height, width, cover):
    area = height * width
    num_of_cans = area / cover
    print(f"\nYou'll need {math.ceil(num_of_cans)} cans of paint.")

paint_calc(2,4,5)

#--------------------------------------------------------------------
# Prime number checker
def prime_checker(number):
    is_prime = True
    for i in range(2,int(math.sqrt(number))):
        if number % i == 0:
            is_prime = False
            break
    if is_prime:
        print(f"The number {number} is prime")
    else:
        print(f"The number {number} is not prime")

prime_checker(19)

#-------------------------------------------------------------------------
# Caesar Cipher
# Alphabets using ASCII value
alphabet=[]
for i in range(97,123):
    alphabet.append(chr(i))
print(alphabet)
def encrypt(word,shift):
    encrypted_word=""
    for i in word:
        if i in alphabet:
            index = alphabet.index(i)
            new_index = (index + shift) % 26
            encrypted_word += alphabet[new_index]
    return encrypted_word

def decrypt(word,shift):
    decrypted_word=""
    for i in word:
        if i in alphabet:
            index = alphabet.index(i)
            new_index = (index - shift) % 26
            decrypted_word += alphabet[new_index]
    return decrypted_word

encr=encrypt("hello",5)
decr=decrypt(encr,5)
print(encr)
print(decr)

# Caesar Cipher
def caesar(word,shift,direction):
    shift%=26
    if direction == "decode":
        shift *= -1
    res=""
    for char in word:
        if char in alphabet:
            pos=alphabet.index(char)
            new_pos=pos+shift
            res+=alphabet[new_pos]
        else:
            res+=char
    print(f"The modified word is {res}")

print(caesar("hello15",5,"encode"))
print(caesar("mjqqt",5,"decode"))