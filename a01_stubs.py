######################################################################
# Author: Dr. Scott Heggen      TODO: Change this to your name
# Username: heggens             TODO: Change this to your username
#
# Assignment: A01
#
# Purpose: A program that returns your Chinese Zodiac animal given a
# birth year between 1988 and 1999. Also prints your friend's animal,
# and your compatibility with that friend's animal.
######################################################################
# Acknowledgements:
#   Original Author: Dr. Scott Heggen
######################################################################

# Remember to read the detailed notes about each task in the A01 document.

######################################################################
import time     # This is too create time lapse
######################################################################
# This Section is to acquire person's name and birth year

name = input("Well hey there! What is your Name?")
print("I hope you're doing okay today, " + name + '!')
print('')
birth_year1 = int(input("So, what year were your born?"))

######################################################################
# This formula takes the year given and converts it into a counter from 0-11
zodiac_number1= birth_year1 % 12

# This assigns the counter to the correct Zodiac animal
if zodiac_number1 == 0:
    zodiac_animal1 = 'Monkey'
elif zodiac_number1 == 1:
    zodiac_animal1 = 'Rooster'
elif zodiac_number1 == 2:
    zodiac_animal1 = 'Dog'
elif zodiac_number1 == 3:
    zodiac_animal1 = 'Pig'
elif zodiac_number1 == 4:
    zodiac_animal1 = 'Rat'
elif zodiac_number1 == 5:
    zodiac_animal1 = 'Ox'
elif zodiac_number1 == 6:
    zodiac_animal1 = 'Tiger'
elif zodiac_number1 == 7:
    zodiac_animal1 = 'Rabbit'
elif zodiac_number1 == 8:
    zodiac_animal1 = 'Dragon'
elif zodiac_number1 == 9:
    zodiac_animal1 = 'Snake'
elif zodiac_number1 == 10:
    zodiac_animal1 = 'Horse'
else:
    zodiac_animal1 = 'Goat'

######################################################################
# This next section displays the name. All the extra coding was for aesthetic
# The time.sleep helps the program look like its "thinking"

print("Lets see here.")
time.sleep(2)
print("If you were born then,")
time.sleep(2)
print("then thaaaat means...")
time.sleep(2)
print('.')
time.sleep(1)
print('.')
time.sleep(1)
print('.')
time.sleep(1)
print('Ah! So according to the Chinese Zodiac, you are a ' + zodiac_animal1 + '!')

######################################################################
# (Required) Task 2
# TODO Ask the user for their friend's birth year


# TODO Similar to above, check your friend's year using if conditionals, and print the correct animal for that year


######################################################################
# (Optional) Task 3
# TODO Check for compatibility between your birth year and your friend's birth year
# NOTE: You can always assume the first input is your birth year (i.e., 1982 for me).
# This way, you are not writing a ton of code to consider every possibility.
# In other words, only do one row of the sample compatibility table.


# TODO print if you are a strong match, no match, or in between
