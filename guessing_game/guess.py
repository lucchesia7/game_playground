import random

'''
Welcome to the Guess a Number game!
'''
### PLAYER INTRODUCTION ###

''' When our game starts, how are we greeting players? What are the variables neccesary for us to properly handle objects for our player?
    In this game, we need to instantiate a guesses taken variable to understand the number of times a player has guessed a number.
    If we place this lower in our flow control, we run into the possibility of overwritting this variable without intention to.'''
guesses_taken = 0
print('Hello and Welcome to the Guess a Number Game! What is your name?')
my_name = input()
number = random.randint(1,20)
print(f'Well, {my_name}, I am thinking of a number between 1 and 20. Can you guess it correctly? You have 5 chances!')

### FLOW CONTROL ###
''' When something happenes in our game, how is it that the action is handled? 
    For every action a player can take, we need to ensure we have an appropriate
    reaction from our program. Hence flow control. '''
for guesses_taken in range(5): # Range values run 0-5.
    print('Take a guess.')
    guess = input()
    guess = int(guess) #input always returns a string value. 

    if guess < number:
        print("Your guess is too low!\n")

    elif guess > number:
        print("Your guess is too high!\n")
    
    elif guess == number:
        break

# If they guess correctly, this triggers
if guess == number:
    guesses_taken = str(guesses_taken +1)
    print(f'''
          Great job {my_name}! You guessed the number within
          {guesses_taken} guesses!
          '''
          )
    
# In all other circumstances, this option will trigger.
else:
    print(f'''Great Try! But, the number I was thinking of was {str(number)}. \n
          Better luck next time!
          ''')
