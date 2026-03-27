

def make_statement(statement, decoration):
        """Adds emoji / additional characters to the start and end of headings"""
        ends = decoration * 3
        print(f"{ends} {statement} {ends}")

# Main routine
make_statement (" hello"," 🤓")

input("my name is Coconut ")

input("welcome to math game")

# tpye player's name
while True:
    player_name = input("Enter your name: ").lower()
    if player_name == player_name:
        print(player_name,"uhm nice")
        break

    elif player_name == "idk":
        continue

    else:
        print("who are are you?")
        continue

# time to loading payer's name
import time

while True:
    for dots in range(4):
        print("\rGame loading" + "." * dots, end="", flush=True)
        time.sleep(0.5)
    break
print("")
print("loading player's name done")

# Ask the player if they want the AI ​​assistant to help.
while True:
    answer = input("Do you want Ai to answer if you don't know? ").lower()

    if answer == "no":
        print("Alright, i hope you can understand it")
        break

    elif answer == "yes":
        print("Okay, I will give smart AI if you don't know or answer worng")
        Ai_name = input("Enter your Ai name:").lower()
        import time
        while True:
            for dots in range(4):
               print("\r creating Ai" + "🔨" * dots, end="", flush=True)
               time.sleep(0.5)
            break
        break

print("")
# click to continue to instruction 
input("click to got next")

# ask player want instruction yes or no to continue
while True:
    answer = input("Do you want to see the instruction: ").lower()

    if answer == "yes":
        print("Okay, I will instruction for you.")
        
        # instruction for new player
        print("Step 1: use your brain")
        print("Step 2: tpye your answer")
        print("final step: check and get answer")
        break

    elif answer == "no":
        print("Alright, don't think you too smart to understand how to play this game.")
        break

    else:
        print("Please type 'yes' or 'no'.")
        continue

# ASK USER THEY WANT
def yes_no(question):
    while True:

        response = input(question).lower()

        # check the user say yes / no / y / n
        if response == "yes" or response == "y":
            return "yes"

        if response == "no" or response == "y":
            return "no"
        else:
            print("error")



input ("click to continue")


# get start the game
print("")
make_statement (" welcome to math game"," ✍️")
print(player_name, "is ready to play!")
input("now we can start the game (click)")






