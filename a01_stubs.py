######################################################################
# Author: Bryar Frank
# Username: frankb
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
import time     # This is too create time lapse
######################################################################
# This Section is to acquire person's name and birth year

name = input("Well hey there! What is your Name?")
print("I hope you're doing okay today, " + name + '!')
print('')
birth_year1 = int(input("So, what year were your born?"))

######################################################################
# This formula takes the year given and converts it into a counter from 0-11
zodiac_number1 = birth_year1 % 12

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
# time.sleep(2)
print("If you were born then,")
# time.sleep(2)
print("then thaaaat means...")
# time.sleep(2)
print('.')
# time.sleep(1)
print('.')
# time.sleep(1)
print('.')
# time.sleep(1)
print('Ah! So according to the Chinese Zodiac, you are a ' + zodiac_animal1 + '!')
print("That's so cool!")
# time.sleep(2)
######################################################################
# This section asks for the birth year of a friend

# This will allows them to terminate the program if they don't wish to put in a friend's birth year.
want_friend = input("So, would you like to see how you match with a friend, " + name + "?")

# Just like the last counter, this will assign their year a counter and an animal
if want_friend == "yes" or want_friend == "Yes":
    birth_year2 = int(input("Sweet! So what is your friend's birth year?"))
    zodiac_number2 = birth_year2 % 12
    if zodiac_number2 == 0:
        zodiac_animal2 = 'Monkey'
    elif zodiac_number2 == 1:
        zodiac_animal2 = 'Rooster'
    elif zodiac_number2 == 2:
        zodiac_animal2 = 'Dog'
    elif zodiac_number2 == 3:
        zodiac_animal2 = 'Pig'
    elif zodiac_number2 == 4:
        zodiac_animal2 = 'Rat'
    elif zodiac_number2 == 5:
        zodiac_animal2 = 'Ox'
    elif zodiac_number2 == 6:
        zodiac_animal2 = 'Tiger'
    elif zodiac_number2 == 7:
        zodiac_animal2 = 'Rabbit'
    elif zodiac_number2 == 8:
        zodiac_animal2 = 'Dragon'
    elif zodiac_number2 == 9:
        zodiac_animal2 = 'Snake'
    elif zodiac_number2 == 10:
        zodiac_animal2 = 'Horse'
    else:
        zodiac_animal2 = 'Goat'
# This is to allow for the program to have some personality
    print("Okay, okay...hmmm...")
    time.sleep(2)
    print("Give me a second to figure this out")
    time.sleep(2)
    print("So, if you are a " + zodiac_animal1 + ",")
    time.sleep(1)
    print('and I see that your friend is a ' + zodiac_animal2 + ',')
    time.sleep(1)
    print('soo...')
    time.sleep(1)
#########################################################################
# (Optional) Task 3
# Here, the program takes the difference between the two years.
# If they are 0,4, or 8 years apart, they are a match
# If they are 6 years apart, they are not a match
    match_coefficient = abs(birth_year1 - birth_year2)
    if match_coefficient == 0 or match_coefficient == 4 or match_coefficient == 8:
        print('You and your friend are a match made in heaven!!!')
        time.sleep(2)
        print('Now if only I could find a better RAM card...')
    elif match_coefficient == 6:
        print('Ouch, looks like your "friend" may not be the best fit with you.')
        time.sleep(2)
        print('Though who cares about what everyone else says,')
        time.sleep(1)
        print('You know your friend better than I do!')
    else:
        print("Seems like you've got an 'okay' friend there, bud!")
        print('''But remember, "EXTRA"ordinary isn't the same thing as "Extraordinary"''')
        time.sleep(2)
###########################################################################
# This gives a farewell if they didn't want to put in a friend's birth year
else:
    print("Well, I hope I was helpful! Have a good day!")