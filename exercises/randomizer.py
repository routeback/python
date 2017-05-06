#!/usr/bin/python3

# Randomizer - Picks a number one through five, with one being the lucky number.

import random

oneinfive = (1, 2, 3, 4, 5)

if (random.choice(oneinfive)) == 1:
	print("Success! Your number was selected.")
elif (random.choice(oneinfive)) == 2 or 3 or 4 or 5:
	print("Fail! Your number was not selected.")
