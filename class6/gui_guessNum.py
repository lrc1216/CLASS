# Listinig_6-5.py
# Copyright Warren Sande, 2009
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version 61  ----------------------------

# Number Guess game using Easygui
import random, easygui

secret = random.randint(1, 99)        #pick a secret number
guess = 0
tries = 0

easygui.msgbox("""AHOY!  I'm sun, and I have a secret!
It is a number from 1 to 99.  I'll give you 6 tries.""")

# keep trying until they guess it or run out of turns
# while guess != secret and tries < 6:
for tries in range(6):
    guess = easygui.integerbox("What's your guess, classmate?")  # get the guess
    if not guess: break
    if guess < secret:
        easygui.msgbox(str(guess) + "it is too low, 小家伙!")
    elif guess > secret:
        easygui.msgbox(str(guess) + "it is too high, 运气真差!")
    elif guess == secret:
        break
    # tries = tries + 1                                       # used up one try

if guess == secret:
    easygui.msgbox("Ye got it!  Found my secret, 真是幸运儿!")
else:
    easygui.msgbox("No more guesses!  Better luck next time, classmate!")

