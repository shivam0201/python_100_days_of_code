import random
word_list=["camel","monkey","peacock"]
chosen_word=random.choice(word_list)
chosen_word_length=len(chosen_word)
solution=[]
for i in range(chosen_word_length):
    solution.append("_")

print(solution)

#Take user input 

mistakes=4
end_of_game=False
while end_of_game == False:
    guess=input("Enter the guess\n").lower()
    if guess in chosen_word:
        for i in range(chosen_word_length):
            if chosen_word[i]==guess:
                solution[i]=guess
        print(solution)
    else:
        mistakes-=1
        print(f"You have {mistakes} lives remaining")
        
        
    if '_' not in solution:
        end_of_game=True
        print("You win")

    if mistakes == 0:
        end_of_game = True
        print("You lose")
    if end_of_game:
        print("Game Over")
        break

    if end_of_game ==True:
        break


