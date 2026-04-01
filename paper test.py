

def make_statement(statement, decoration):
        """Adds emoji / additional characters to the start and end of headings"""
        ends = decoration * 3
        print(f"{ends} {statement} {ends}")

player_name = ("goku")

# history answer of player
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

while True:
   input("click to keep going")
   # Question 5
   answer = input("question 5) What is 8 × 3? ")
   if answer == "24":
      make_statement (player_name,"keep going","*")
      print("Correct!")
      score += 1
      break
   elif answer == "":
      print("you didn't answer")
      break
   else:
      print("Wrong!")
      break

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

while True:
   # Question 8
   input("click to keep going")
   answer = input("question 8) What is 10 × 7? ")
   if answer == "70":
      print("Correct!")
      score += 1
      break
   elif answer == "":
      print("you didn't answer")
      break
   else:
      print("Wrong!waaaaaahaha")
      break

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


print("total your score is:", score, "/ 10")








