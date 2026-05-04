def make_statement(statement, decoration):
        """Adds emoji / additional characters to the start and end of headings"""
        ends = decoration * 3
        print(f"{ends} {statement} {ends}")
import random

# Main routine
make_statement (" hello"," 🤓")

input("my name is Coconut (enter to continue)")

input("welcome to math game")

# type player's name
while True:
    player_name = input("                     Enter your name: ").lower()
    if player_name == player_name:
        print(player_name,                          "uhm nice")
        break

input("     enter to go next")

# ask player want instruction yes or no to continue
instrution = 1
while True:
   answer = input("Do you want to see the instruction? ").lower()
   if answer == "yes":
       print("Okay, I will instruction for you.")
      # instruction for new player
       print("")
       print("           Step 1:  based on the available numbers")
       print("")
       print("           Step 2: Calculate it  and type your answer")
       print("")
       print("           final step: check and give the correct answer")
       print("")
       print("             you will get point(socre) if aswer correct ")
       print("")
       input("    if you done reading instruction to start the game ")
       break
   elif answer == "no":
      answer = input(" Are you sure about that?")

      if answer == "no":
         print("")
         print("i knew it, let see the instrucion!")
         print("")
         input("               to see intrustion!!")
         print("")
         print("Step 1: based on the available numbers")
         print("")
         print("Step 2:Calculate it  and type your answer")
         print("")
         print("final step: check and give the correct answer")
         print("")
         print("")
         input("    if you done reading instruction  to start the game ")
         break

      elif answer == "yes":
         print ("okay, i think you're good at math game...")
         break
   else:
        if instrution <= 1:
             print("")
             print("please type yes or no!")
             print(" ")
             instrution += 1
             continue
        elif instrution <= 2:
             print("")
             print("stop keep type nothing, please type yes or no dude!!!")
             print("")
             instrution += 1
             continue
        elif instrution <= 3:
             print("")
             print("we will skip the instrution if you don't say anything")
             print("please just tpye yes or no!!")
             print("")
             instrution += 1
             continue
        elif instrution <=4:
             print("")
             print("           you didn't say anything so we was skip your instrution")
             print("                               good luck")
             break


# get start the game
print("")
make_statement (                                "WELCOME TO MATH GAME"," ✍️")
print(                                     player_name, "ready to play!")
print("")
input("                                        now we can start the game")
print("")

# adds score if players answer correct 
quest1 = 0
quest2 = 0
three = 0
four = 0
five = 0
six = 0
seven = 0
eight = 0
nine =0
ten = 0
score = 0
again = 1

# numbers of questions
a = random.randint(1, 10)
b = random.randint(1, 10)
c = random.randint(1, 10)
d = random.randint(1, 10)
e = random.randint(1, 10)
f = random.randint(1, 10)
h= random.randint(1, 10)
k = random.randint(1, 10)
t = random.randint(1, 10)
r = random.randint(1, 10)
p = random.randint(1, 10)
g = random.randint(1, 10)
correct_answer = a + b
hehe = t + f
print("")
input ("before we start, we just have 10 question and use type number not word")
print("")
while True:
   # Question 1
   print("question 1")
   answer = input(f"What is {a} + {b}? ")
   if answer == "":
        print("you didn't answer")
        break

   elif int(answer) == correct_answer:
        print("Correct!")
        quest1 += 1
        score += 1
        break
   else:
        print(f"OH nooooo, it's {correct_answer} hehe")
        break
   
print("")
while True:
   # Question 2
   input(" enter to keep going")
   print("question 2")
   answer = input(f"What is {t} + {f}? ")
   if answer == "":
        print("you didn't answer")
        break

   elif int(answer) == hehe:
        print("Correct!")
        quest2 += 1
        score += 1
        break
   else:
        print(f"sorry but you wasn worng , it's {hehe}")
        break
   
print("")
quest3 = k + a
while True:
   # Question 3
   print("question 3")
   input(" to keep going")
   answer = input(f"What is {k} + {a}? ")
   if answer == "":
        print("you didn't answer")
        break

   elif int(answer) == quest3:
        print("Correct!")
        three += 1
        score += 1
        break
   else:
        print(f"it's {quest3}, not that ")
        break

if score >= 2: 
                 make_statement ("Are you a robot?"," 🤖")
elif score <= 0:
                 make_statement ("stop keep not answer my question!!!","🚨")
print("")
while True:
   input("enter to keep going")
   # Question 4
   heel = k + h 
   print("question 4")
   answer = input(f"What is {k} + {h}? ")
   if answer == "":
        print("you didn't answer")
        break

   elif int(answer) == heel:
        print("Correct!")
        four += 1
        score += 1
        break
   else:
        print(f"worng , it's {heel}")
        break
print("")
while True:
   input(" to keep going")
   # Question 5
   good = t + f
   print("question 5")
   answer = input(f"What is {t} + {f}? ")
   if answer == "":
        print("you didn't answer")
        break

   elif int(answer) == good:
        print("Correct!")
        five += 1
        score += 1
        break
   else:
        answer = input(" Do you want to answer again?").lower()
        if answer == "yes":
           print ("ok, let try again")
           print("")
           answer = input(f"What is {t} + {f}? ")
           if answer == "":
                print ("you didn't answer")
                break
           elif int(answer) == good:
                print("Correct!!")
                five += 1
                score += 1
                break
        elif answer == "no":
           print("ok, we still not done yet!")
           break
        else:
           print("you didn't answer, don't give up .")
           break


if score >= 5:
   print("                 Amazing! You’re god waaaa 🌟")
elif score >= 3:
   print("               not bab haha” Keep practicing! 👍")
else:
   print("            you answer worng too much!! keep trying ")


print("")
quest6 = b + b
while True:
   # Question 6
   print("question 6")
   input(" enter to keep going")
   answer = input(f"What is {b} + {b}? ")
   if answer == "":
        print("you didn't answer")
        break
   elif int(answer) == correct_answer:
        print("Correct!")
        six += 1
        score += 1
        break
   else:
        print(f"worng , it's {correct_answer}")
        break

if score <= 1:
                 make_statement ("HEYYYYY STOP!!!","🚨")

print("")
while True:
   # Question 7
   input(") to keep going")
   answer = input(f"What is {a} + {g}? ")
   if answer == "":
        print("you didn't answer")
        break

   elif int(answer) == correct_answer:
        print("Correct!")
        seven += 1
        score += 1
        break
   else:
        print(f"worng , it's {correct_answer}")
        break

if score <= 1:
                 make_statement ("we will report you if you still keep doing that!!!","🚨")

print("")
while True:
   # Question 8
   input(") to keep going")
   answer = input(f"What is {e} + {d}? ")
   if answer == "":
        print("you didn't answer")
        break

   elif int(answer) == correct_answer:
        print("Correct!")
        eight += 1
        score += 1
        break
   else:
        print(f" that's easy!!! , it's {correct_answer}")
        break

if score <= 1:
                 make_statement ("NAH MAN THIS IS MY GAME!!!","🚨")

print("")
while True:
   # Question 9
   input(") to keep going")
   answer = input(f"What is {g} + {e}? ")
   if answer == "":
        print("you didn't answer")
        break

   elif int(answer) == correct_answer:
        print("Correct!")
        nine += 1
        score += 1
        break
   else:
        print(f"worng , it's {correct_answer}")
        break

if score <= 1:
   print("what worng with you?" )

make_statement ("         FINALLY, you got this","*")
while True:
   # Question 10
   input("not bad, last questio to final question")
   answer = input(f"What is {h} + {c}? ")
   if answer == "":
        print("you didn't answer")
        break

   elif int(answer) == correct_answer:
        print("Correct!")
        ten += 1
        score += 1
        break
   else:
        print(f" that's the final question OMG , it's {correct_answer} !!!!")
        break



# Output the result
print("")
make_statement("Round Results","📢")



if score >= 8:
   print("OMG, YOU DROPPED THIS 👑" 
   "      " 
   "       YOU WON THIS GAME")
elif score >= 6:
   make_statement (player_name," you did very well","🤓")
else:
   print("this is the end...")

# aksing about want to see the score(history)

while True:
    answer = input("do you want to see the history's score?").lower()
    if answer == "yes":
        print("total your score is:", score, "/ 10")
        if quest1 >= 1:
            print ("question 1 is Correct!")
            print("")
        elif quest1 <= 0:
            print ("question 1 is worng!")
            print("")
        if quest2 >= 1:
            print ("question 2 is Correct!")
            print("")
        elif quest2 <= 0:
            print ("question 2 is worng!")
            print("")
        if three >= 1:
            print ("question 3 is Correct!")
            print("")
        elif three <= 0:
            print ("question 3 is worng!")
            print("")
        if four >= 1:
            print ("question 4 is Correct!")
            print("")
        elif four <= 0:
            print ("question 4 is worng!")
            print("")
        if five >= 1:
            print ("question 5 is Correct!")
            print("")
        elif five <= 0:
            print ("question 5 is worng!")
            print("")
        if six >= 1:
            print ("question 6 is Correct!")
            print("")
        elif six <= 0:
            print ("question 6 is worng!")
            print("")
        if seven >= 1:
            print ("question 7 is correct!")
            print("")
        elif seven <= 0:
            print("question 7 is worng")
            print("")
        if eight >= 1:
            print ("question 8 is correct!")
            print("")
        elif eight <= 0:
            print("question 8 is worng")
            print("")
        if nine >= 1:
            print ("question 9 is correct!")
            print("")
        elif nine <= 0:
            print("question 9 is worng")
            print("")
        if ten >= 1:
            print ("question 10 is correct!")
            print("")
        elif ten <= 0:
            print("question 10 is worng")
            break
    elif answer == "no":
        while True:
            answer = input(" Are you sure about that?").lower()
            if answer == "yes":
                print("")
                print("")
                while True:
                    answer = input(" you will never know if you can check your score, are you sure about that?").lower()
                    if answer == "yes":
                        print ("ok :)")
                        break
                    elif answer == "no":
                        print("")
                        print          ("i knew it ")            
                        print("total your score is:", score, "/ 10")
                    if quest1 >= 1:
                        print ("question 1 is Correct!")
                        print("")
                    elif quest1 <= 0:
                        print ("question 1 is worng!")
                        print("")
                    if quest2 >= 1:
                        print ("question 2 is Correct!")
                        print("")
                    elif quest2 <= 0:
                        print ("question 2 is worng!")
                        print("")
                    if three >= 1:
                        print ("question 3 is Correct!")
                        print("")
                    elif three <= 0:
                        print ("question 3 is worng!")
                        print("")
                    if four >= 1:
                        print ("question 4 is Correct!")
                        print("")
                    elif four <= 0:
                        print ("question 4 is worng!")
                        print("")
                    if five >= 1:
                        print ("question 5 is Correct!")
                        print("")
                    elif five <= 0:
                        print ("question 5 is worng!")
                        print("")
                    if six >= 1:
                        print ("question 6 is Correct!")
                        print("")
                    elif six <= 0:
                        print ("question 6 is worng!")
                        print("")
                    if seven >= 1:
                        print ("question 7 is correct!")
                        print("")
                    elif seven <= 0:
                        print("question 7 is worng")
                    if eight >= 1:
                        print ("question 8 is correct!")
                        print("")
                    elif eight <= 0:
                        print("question 8 is worng")
                    if nine >= 1:
                        print ("question 9 is correct!")
                        print("")
                    elif nine <= 0:
                        print("question 9 is worng")
                    if ten >= 1:
                        print ("question 10 is correct!")
                        print("")
                    elif ten <= 0:
                        print("question 10 is worng")
                        break
                    else:
                        print("please type yes or no")
                        break
            elif answer == "no":
                print("")
                print(" here is your history score")
                print("total your score is:", score, "/ 10")
                if quest1 >= 1:
                    print ("question 1 is Correct!")
                    print("")
                elif quest1 <= 0:
                    print ("question 1 is worng!")
                    print("")
                if quest2 >= 1:
                    print ("question 2 is Correct!")
                    print("")
                elif quest2 <= 0:
                    print ("question 2 is worng!")
                    print("")
                if three >= 1:
                    print ("question 3 is Correct!")
                    print("")
                elif three <= 0:
                    print ("question 3 is worng!")
                    print("")
                if four >= 1:
                    print ("question 4 is Correct!")
                    print("")
                elif four <= 0:
                    print ("question 4 is worng!")
                    print("")
                if five >= 1:
                    print ("question 5 is Correct!")
                    print("")
                elif five <= 0:
                    print ("question 5 is worng!")
                    print("")
                if six >= 1:
                    print ("question 6 is Correct!")
                    print("")
                elif six <= 0:
                    print ("question 6 is worng!")
                    print("")
                if seven >= 1:
                    print ("question 7 is correct!")
                    print("")
                elif seven <= 0:
                    print("question 7 is worng")
                if eight >= 1:
                    print ("question 8 is correct!")
                    print("")
                elif eight <= 0:
                    print("question 8 is worng")
                if nine >= 1:
                    print ("question 9 is correct!")
                    print("")
                elif nine <= 0:
                    print("question 9 is worng")
                if ten >= 1:
                    print ("question 10 is correct!")
                    print("")
                elif ten <= 0:
                    print("question 10 is worng")
                    break
            else:
                print("error")
                break
    else:
        if again <= 1:
            print    (" ")
            print    ("")
            print    ("     don't do it again!!, please type yes or no")
            print("")
            print("")
            again += 1
            continue
        elif again <= 2:
            print    ("")
            print    (    "")
            print    ("     you did it again!!, please just say yes or no!")
            print("")
            print("")
            again += 1
            continue
        elif again <= 3:
            print("")
            print    ("     you will get kick out if keep do it again!!")
            print    ("     please type yes or no")
            print("")
            print("")
            again += 1
            continue
        elif again <= 4:
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("                                                           you kicked out the game")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("") 
            break
        break
input("                           thank for your play")
print("")
if score <= 3:
                    make_statement ("you not good at math","🚨")
elif score >= 7:
                   make_statement ("you did very well","!")
print("")
input("                          the game made by Minh D")
input("                               have good day")
print("                                 thank you  ")