"""
This file is an add-on to the make_pizza.py located in the top directory.

What does this program do?
	--> The program calls the make_pizza() from pizza.py
	--> After make_pizza() lists the pizza toppings,
	 the program asks the user if they would like to animate*
	 a slice taken from each pizza.
	 If yes ('y'), the program runs the pygame file in the same directory.
	 If no ('n'), the program is exited.
	 
	 *a slice from each pizza will display in a separate pygame window.
"""

import pizza

print("Enter 'q' at anytime to quit.")

intro = raw_input("We are going to make your favorite pizza" + "\nContinue? y/n ")

pizza.make_pizza(16, 'pepperoni', 'extra cheese')
pizza.make_pizza(12, 'mushrooms', 'peppers', 'olives')

bounce = raw_input("\nAnimate a slice of each pizza? y/n ")

if bounce == 'n':
    exit()
else:
	import bounce
