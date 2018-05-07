import pizza

print("Enter 'q' at anytime to quit.")

intro = raw_input("We are going to make your favorite pizza" + "\nContinue? y/n ")

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'peppers', 'legos')
