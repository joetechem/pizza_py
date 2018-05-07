def make_pizza(size, *toppings):
    """Puts together a virtual pizza based on a user's input"""
    print("\nMaking a " + str(size) + "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping.title())