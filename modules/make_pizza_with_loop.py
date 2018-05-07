import pizza

print("Enter 'q' at anytime to quit.")

while True:
    intro = raw_input("We are going to make your favorite pizza" + "\nContinue? y/n ")

    size = raw_input("\nPlease enter pizza size: ")
    if size == 'q':
        exit()

    toppings = raw_input("Please enter toppings you would like on your pizza" +
                         "\t\nIf multiple, separate values with a comma. " +
                         "\n")
    if toppings == 'q':
        exit()

    pizza.make_pizza(size, toppings)

# works okay, but need to figure out how to output toppings on separate lines

