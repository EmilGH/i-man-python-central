#!/usr/bin/env python3

def runQuiz1():
	print("Now running Quiz 1...")

def runQuiz2():
	print("Now running Quiz 2...")

quizChoice = input("What quiz do you want to run? [1 or 2] ")

if quizChoice == "1":
	runQuiz1()
elif quizChoice == "2":
	runQuiz2()
elif (quizChoice != "1") or (quizChoice != "2"):
	print("Invalid selection, idiot.")
