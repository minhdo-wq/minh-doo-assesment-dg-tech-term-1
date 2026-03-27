
input("hello, my bad guy ")

input("my name is your mom ")

input("welcome to math game")

# tpye player's name

player_name = input("Enter your name: ").lower()
print("Welcome,", player_name, "!")


# ask player want instruction
while True:
    want_instruction =input(" ✍️  ?Do you want intruction before start the game?✍️  "). lower()
    if want_instruction == "yes" or want_instruction == "y" or want_instruction == "yesss" or want_instruction == "yesssss":
        print("you said yes")
        break

    elif want_instruction == "no" or want_instruction == "n" or want_instruction == "nooo" or want_instruction == "nah":
        print("you said no")
        break

    else:
        print("please just say yes or no ")
        break

# ask again 
while True:
    want_instruction =input(" ✍️  ?Do you want intruction?✍️  "). lower()
    if want_instruction == "yes" or want_instruction == "y" or want_instruction == "yesss" or want_instruction == "yesssss":
        print("you said yes")
        break

    elif want_instruction == "no" or want_instruction == "n" or want_instruction == "nooo" or want_instruction == "nah":
        print("you said no, you think you good uh?")
        break

    else:
        print("HOLY MOLY SAY YES OR NO")
        continue

# get start the game

print(player_name, "is ready to play!")
print("okay")

input("now we can start the game ")

































