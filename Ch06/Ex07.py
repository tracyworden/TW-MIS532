"""Tracy Worden MIS532 Spanish training program """

# Create dictionary
import random

to_spanish = {
    'zero': 'cero',
    'one': 'uno',
    'two': 'dos',
    'three': 'tres',
    'four': 'cuatro',
    'five': 'cinco',
    'six': 'seis',
    'seven': 'siete',
    'eight': 'ocho',
    'nine': 'nueve'}

# display header message to user to indicate the program
print('\nWelcome to the Spanish digit tutor!\n')

# create a loop to allow user to continue until they select x
count = 0
correct = 0

while True:

    # select random digit
    digit = random.choice(list(to_spanish.keys()))

    # prompt user for guess
    guess = input(f'What is the Spanish word for {digit} (enter x to exit):').strip()

    # check to see if user entered the x and exit or continue and check if they are correct or incorrect
    if guess == 'x':
        break
    elif guess == to_spanish[digit]:
        print('You are correct!')
        correct += 1
        count += 1
    else:
        print('Sorry you are incorrect')
        count += 1

# when finished display a summary of words tried and percentage correct
if count > 0:
    # User attempted the game
    print(f'You attempted {count} times and got {correct / count * 1 * 100}% correct.')

# print goodbye message
print('Thanks for playing, goodbye.')

