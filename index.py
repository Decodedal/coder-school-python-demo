# brings in the random module 
import random

# sets the secret number for user to guess
secret_number = random.randint(1,10)

# begins out game by asking user for input 
print('enter a number between 1 and 10')
# collects the first guess from the user and assigns it to the var user_number
user_number = input()

# this will keep track of how many guesses the user makes before getting the correct answer
number_of_guesses = 1
guessed_so_far = []

# checks if user_numebr is the correct Number if so skips loop 
while int(user_number) != secret_number:
    # adds the latest incorrect guess to our list guessed_so_far
    guessed_so_far.append(user_number)

    # adds one to our count for each round of guessing so we can return to the user how many guesses it took to get the right number. 
    number_of_guesses += 1

# if users number is greater then the secret_number tell them that they have to pick a smaller number and give them a list of all guesses so far. 
    if int(user_number) > secret_number:
        print(f"You have to go lower, Pick again, so far you have guessed {guessed_so_far} ")

# if users number is greater then the secret_number tell them that they have to pick a Bigger number and give them a list of all guesses so far.
    else:
        print(f"You have to go higher Guess again, so far you have guessed {guessed_so_far} ")

# asks the user for a new guess 
    user_number = input()

# only runs once loop is broken meaning the user guessed the correct number. 
print(f"Congratulations {secret_number} is correct! It took you {number_of_guesses} guesses 🎇")    

