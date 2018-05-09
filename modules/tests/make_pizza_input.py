def make_pizza(size, *toppings):
    """Puts together a virtual pizza based on a user's input"""
    print("\nMaking a " + str(size) + "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping.title())
        

print("Enter 'q' at anytime to quit.")

intro = raw_input("We are going to make your favorite pizza" + "\nContinue? y/n ")


print("\nPIZZA ONE")

make_pizza(
    int(raw_input("size: ")),
    raw_input("1st topping: ")
    )
           
print("\nPIZZA TWO")

make_pizza(
    int(raw_input("size: ")),
    raw_input("1st topping: "),
    raw_input("2nd topping: "),
    raw_input("3rd topping: ")
           )
           
