import random
x1 = random.randint(1,10) # generate random int between 1 and 10 and define as x1

guess = int(input("enter a number and prepare to experience true pain in the form of guessing a random number between 1 and 10 until you get the right number I am thinking of"))

while True: # starts while loop that repeats the prompt for input until you finally get it right
    guess = int(input("enter a number and prepare to experience true pain in the form of guessing a random number between 1 and 100 until you get the right number I am thinking of"))

    if guess < x1:
        print("too low son! don't guess")
    else:
        print("too high son! You will be here for a while, but don't worry I have plenty of time")
    if guess == x1:
        print("CORRECTAMUNDO")
    
        
    
