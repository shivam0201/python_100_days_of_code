print("Welcome to Treasure Island\nYour Mission is to find the treasure")
door_side=input("You are standing in front of two doors. One door leads to treasure and the other door")
if door_side.lower()=='right':
    print("Game over")
river=input("Swim or wait")
if river.lower()=='swim':
    print("Game over")
door=input("Choose door to open for treasure")
if door.lower()=='yellow':
    print("Congratulations! You found the treasure")
else:
    print("Game over")
