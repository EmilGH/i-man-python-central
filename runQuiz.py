#!/usr/bin/env python3

## The line below creates a function called runQuiz1.  Put all the code for the first quiz here... (indented once!)
def runQuiz1():
	print("Now running Quiz 1: History Quiz")

	questions = ("When was OJ Simpsion trial?: ",
					"When was pearl harbor?: ",
					"What is the most abundant gas in Earth's atmosphere?: ",
					"What is the best star wars moive?: ",
					"Which planet in the solar system is the hottest?: ")

	options = (("A. 1990", "B. 1976", "C. 1995", "D. 1994"),
					("A. 1943", "B. 1945", "C. 1939", "D. 1941"),
					("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"),
					("A. The Empire Strikes Back", "B. Revenge of the Sith", "C. the Force Awakens", "D. the Way of Water"),
					("A. Mercury", "B. Venus", "C. Earth", "D. Mars"))

	answers = ("C", "D", "A", "B", "B")
	guesses = []
	score = 0
	question_num = 0

	for question in questions:
		print()
		print("----------------------")
		print(question)
		for option in options[question_num]:
			print(option)

		guess = input("Enter (A, B, C, D): ").upper()
		guesses.append(guess)
		if guess == answers[question_num]:
			score += 1
			print("That is correct, " + name)
		else:
			print("Nope.")
			print(f"{answers[question_num]} is the correct answer")
		question_num += 1

	print()
	print("----------------------")
	print("       RESULTS        ")
	print("----------------------")

	print("Right Answers: ", end="")
	for answer in answers:
		print(answer, end=" ")
	print()

	print(" Your Answers: ", end="")
	for guess in guesses:
		print(guess, end=" ")
	print()

	score = int(score / len(questions) * 100)
	print(f"Your score is: {score}%")

	user_input = input("Did you enjoy the Quiz? ")
	print("Really, " + user_input + "! Go to know?")

## The line below creates a function called runQuiz2.  Put all the code for the second quiz here... (indented once!)
def runQuiz2():
	print("Now running Quiz 2: The Dog Quiz")

	questions = ("What is the best dog?: ",
					"Dogs are called ____: ",
					"What is a dog's favorite food?: ")
	
	options = (("A. Mutt", "B. Collie", "C. Momo", "D. None."),
					("A. Man's Best Friend", "B. Loyal and Loving", "C. Furry and Funny", "D. Stinky"),
					("A. Kibble", "B. Tacos", "C. Fish", "D. Their own shit"))
	
	answers = ("D", "D", "D")
	guesses = []
	score = 0
	question_num = 0
	
	for question in questions:
		print()
		print("----------------------")
		print(question)
		for option in options[question_num]:
			print(option)
			
		guess = input("Enter (A, B, C, D): ").upper()
		guesses.append(guess)
		if guess == answers[question_num]:
			score += 1
			print("That is correct, " + name)
		else:
			print("Nope.")
			print(f"{answers[question_num]} is the correct answer")
		question_num += 1

	print()
	print("----------------------")
	print("       RESULTS        ")
	print("----------------------")

	print("Right Answers: ", end="")
	for answer in answers:
		print(answer, end=" ")
	print()

	print(" Your Answers: ", end="")
	for guess in guesses:
		print(guess, end=" ")
	print()

	score = int(score / len(questions) * 100)
	print(f"Your score is: {score}%")

	user_input = input("Did you enjoy the Quiz? ")
	print("Really, " + user_input + "! Go to know?")


## This is where the script will start to run...

##Let's ask for some basic information from the player.

print("Welcome to I-Man Quiz Central.")
print("------------------------------")
print()
name = input("What is your name? ")
print("Hello, " + name + " it is nice to meet you.")
print()

age = int(input("How old are you? (Numbers only, please) "))
height = float(input("How tall are you? (In inches, numbers only, please) "))

print("Thank you for sharing, " + name)

## Display quiz choices...

print()
print("Quizzes Available:")
print("  1: The History Quiz")
print("  2: The Dog Quiz")
print()
quizChoice = input("What quiz do you want to run? [1 or 2] ")

## If the player enters "1" we will execute the runQuiz1 funstion.  If they enter "2" we will execute the runQuiz2 function.
## Both of those functions are at the top of this source code...

if quizChoice == "1":
	runQuiz1()
elif quizChoice == "2":
	runQuiz2()
## If the player does not enter "1" or "2" call them an idiot and exit
elif (quizChoice != "1") or (quizChoice != "2"):
	print()
	print("Invalid selection.  I didn't realize that you are an idiot, " + name + ".")