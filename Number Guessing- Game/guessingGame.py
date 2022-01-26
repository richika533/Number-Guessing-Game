import random

#write a text 
print("Number Guessing Game")

#use a function from random module to choose number between 1 and 9
number= random.randint(1,9)

#write a text
print("Guess the number between 1 and 9")

#chances should be 
chances= 0

#create a loop function for giving the chances 
while chances < 5:
    #choose the number between 1 and 9
    guessnumber= int(input("Enter your guess number"))
    print(number)
#start a condition
    if guessnumber == number:
      print("You Won")
      break
#choosen number is smaller than random number
    elif guessnumber < number:
        print("You were too low: Guess a bigger number", guessnumber)

    else:
       print("You were too high: Guess a smaller number", guessnumber)
    chances= chances+1

    if not chances < 5:
       print("you lose!!! the number is", number)
