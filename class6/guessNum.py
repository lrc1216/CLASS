# Listing_1-2.py
# Copyright Warren Sande, 2009
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version 61  ----------------------------

# Number Guess game

import random

secret = random.randint(1, 99)     # pick a secret number
guess = 0
tries = 0

print ("AHOY!  I'm Richie, and I have a secret!")
print ("It is a number from 1 to 99.  I'll give you 6 tries. ")

# try until they guess it or run out of turns[[]]
while guess != secret and tries < 6:
    guess = int(eval(input("What's yer guess? ")) )      # get the player's guess cvf
    if guess < secret:
        print ("Too low, 运气真差!")
    elif guess > secret:
        print ("Too high, 笨蛋!")
    tries = tries + 1                         # used up one try

# print message at end of game    
if guess == secret:
    print ("你真是幸运儿!  Found my secret, ye did!")
else:
    print ("对不起，挑战失败  Better luck next time, matey!")
    print(("The secret number was", secret))
