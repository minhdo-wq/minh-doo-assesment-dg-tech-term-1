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

# click to continue to instruction 
input("click to go next")

# ask player want instruction yes or no to continue
while True:
   answer = input("Do you want to see the instruction? ").lower()
   if answer == "yes":
       print("Okay, I will instruction for you.")
      # instruction for new player
       print("")
       print("           Step 1:  based on the available numbers")
       print("")
       print("           Step 2: Calculate it  and tpye your answer")
       print("")
       print("           final step: check and give the correct answer")
       print("")
       print("             you will get point(socre) if aswer correct ")
       print("")
       input("    if you done reading instruction, click to start the game ")
       break
   elif answer == "no":
      answer = input(" Are you sure about that?")

      if answer == "no":
         print("")
         print("i knew it, let see the instrucion!")
         print("")
         input("              click to see intrustion!!")
         print("")
         print("Step 1: based on the available numbers")
         print("")
         print("Step 2:Calculate it  and tpye your answer")
         print("")
         print("final step: check and give the correct answer")
         print("")
         print("")
         input("    if you done reading instruction, click to start the game ")
         break

      elif answer == "yes":
         print ("okay, i think you're good at math game...")
         break

   else:
      print("can you please tpye yes or no")
      continue

# get start the game
print("")
make_statement ("     WELCOME TO MATH GAME"," ✍️")
print(player_name, "ready to play!")
input("now we can start the game (click)")
print("")

# math quest


# adds score if players answer correct 
score = 0

while True:
   # Question 1
   answer = input("question 1) What is 1 + 1? ")
   if answer == "3":
      print("Correct!")
      score += 1
      break
   elif answer == "":
      print("you didn't answer")
      break
   else:
      print("OH noooooo, it's 3 hehe")
      break
print("")
while True:
   # Question 2
   input("click to keep going")
   answer = input("question 2) What is 23 + 10? ")
   if answer == "33":
      print("Correct!")
      score += 1
      break
   elif answer == "":
      print("you didn't answer")
      break
   else:
      print("Wrong!")
      break
print("")
while True:
   # Question 3
   input("click to keep going")
   answer = input("question 3) What is 5 × 3? ")
   if answer == "15":
      print("Correct!")
      score += 1
      break
   elif answer == "":
      print("you didn't answer")
      break
   else:
      print("Wrong!")
      break

if score >= 2: 
                 make_statement ("Are you a robot?"," 🤖")
elif score <= 0:
                 make_statement ("stop keep not answer my question!!!","🚨")
print("")
while True:
   input("click to keep going")
   # Question 4
   answer = input("question 4) What is 7 × 7? ")
   if answer == "49":
      print("Correct!")
      score += 1
      break
   elif answer == "":
      print("you didn't answer")
      break
   else:
      print("Wrong!")
      break
print("")
while True:
   input("click to keep going")
   # Question 5
   answer = input("question 5) What is 8 × 3? ")
   if answer == "24":
      print("Correct!")
      score += 1
      break
   elif answer == "":
       answer = input(" Do you want to answer again?").lower()
       
       if answer == "yes":
           print ("ok, let try again")
           print("")
           answer = input("question 5) What is 8 × 3? ")
           if answer == "24":
              print("Correct!!")
              score += 1
              break
           elif answer == "":
               print("you didn't answer, it's to hard for you?")
               break
           else:
               print("HOW, you still worng but that's so easy")
               break
       elif answer == "no":
           print("ok, we still not done yet!")
           break
       else:
           print("you didn't answer, please keep your cool head.")
           break


if score >= 5:
   print("                 Amazing! You’re god waaaa 🌟")
elif score >= 3:
   print("               not bab haha” Keep practicing! 👍")
else:
   print("            you answer worng too much!! keep trying ")


print("")
while True:
   # Question 6
   input("click to keep going")
   answer = input("question 6) What is 9 × 9? ")
   if answer == "81":
      print("Correct!")
      score += 1
      break
   elif answer == "":
      print("stop keep do not answer")
      break
   else:
      print("Wrong!!!!")
      break

if score <= 1:
                 make_statement ("HEYYYYY STOP!!!","🚨")

print("")
while True:
   # Question 7
   input("click to keep going")
   answer = input("question 7) What is (2+5) × 4? ")
   if answer == "28":
      print("Correct!")
      score += 1
      break
   elif answer == "":
      print("you didn't answer")
      break
   else:
      print("oh that's easy, keep try again")
      break

if score <= 1:
                 make_statement ("we will report you if you still keep doing that!!!","🚨")

print("")
while True:
   # Question 8
   input("click to keep going")
   answer = input("question 8) What is 10 × 7? ")
   if answer == "70":
      print("Correct!")
      score += 1
      break
   elif answer == "":
      print("         you didn't answer")
      break
   else:
      print("         Wrong!waaaaaahaha")
      break

if score <= 1:
                 make_statement ("NAH MAN THIS IS MY GAME!!!","🚨")

print("")
while True:
   # Question 9
   input("click to keep going")
   answer = input("question 9) What is 4 × 9? ")
   if answer == "36":
      print("Correct!")
      score += 1
      break
   elif answer == "":
      print("you didn't answer")
      break
   else:
      print("Wrong!")
      break

if score <= 1:
   print("what worng with you?" )

make_statement ("         FINALLY, you got this","*")
while True:
   # Question 10
   input("not bad, last question click to final question")
   answer = input("question 10) What is 8 × 6? ")
   if answer == "48":
      print("Correct!")
      score += 1
      break
   elif answer == "":
      print("you didn't answer")
      break
   else:
      print("Wrong!")
      break


# Output the result
print("")
make_statement("Round Results","📢")



if score >= 8:
   print("OMG, YOU DROPPED THIS 👑" 
   "      " 
   "       YOU WON THIS GAME")
elif score >= 6:
   make_statement (player_name," you did very well"," 🤓")
else:
   print("this is the end...")

# aksing about want to see the score(history)
input("click to keep continue")
answer = input("do you want to see the history's score?")
if answer == "yes":
   print("total your score is:", score, "/ 10")
elif answer == "no":
   print("the game is over")
else:
   make_statement("it's ok","😓")
   
input("                           thank for your play")
print("")
if score <= 3:
                    make_statement (player_name,"you not good at math","🚨")
elif score >= 7:
                   make_statement ("you did very well")
print("")
input("                          the game made by Minh Do(click to go next)")
input("                               have good day")
print("                                 thank you  ")


