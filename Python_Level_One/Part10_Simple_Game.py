###########################
## PART 10: Simple Game ###
### --- CODEBREAKER --- ###
## --Nope--Close--Match--  ##
###########################

# It's time to actually make a simple command line game so put together everything
# you've learned so far about Python. The game goes like this:

# 1. The computer will think of 3 digit number that has no repeating digits.
# 2. You will then guess a 3 digit number
# 3. The computer will then give back clues, the possible clues are:
#
#     Close: You've guessed a correct number but in the wrong position
#     Match: You've guessed a correct number in the correct position
#     Nope: You haven't guess any of the numbers correctly
#
# 4. Based on these clues you will guess again until you break the code with a
#    perfect match!

# There are a few things you will have to discover for yourself for this game!
# Here are some useful hints:

# Try to figure out what this code is doing and how it might be useful to you
import random
digits = list(range(10))
random.shuffle(digits)
digits = [str(i) for i in digits]
target = ''.join(digits[:3])

correct = False

while correct == False:

    match = 0
    close = 0
    nope = 1

    guess = input("What is your guess? ")

    if guess == target:
        correct = True
        break

    else:
        for (g, t) in zip(guess, target):
            if g == t:
                match = 1
                print('Match')
            elif g in target:
                close = 1
                print('Close')

    if match == 0  and close == 0:
        print('Nope')





print('Congratulations, You\'ve cracked the code!')


# Think about how you will compare the input to the random number, what format
# should they be in? Maybe some sort of sequence? Watch the Lecture video for more hints!
