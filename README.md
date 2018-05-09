# pizza_py
Basic example of storing your own functions in a module to use in another program  

*in production*  

#### Objectives  
Storing your own function(s) in a module to use in another program.  

* Directory navigation
* Executing files from other files

## How to use this Repository  

The files in this repo can be run as-is. To practice for yourself, follow the detailed directions below along with the directions found on *Pizza_Module.py*  

Directions:  

#### 1. Clone (or fork) this repository on your local machine.  

```  
git clone https://github.com/joetechem/pizza_py
```  

#### 2. Navigate to the local repository  

```  
cd pizza_py  
```  

#### 3. Create your own folder and navigate to it  

```  
mkdir myFolderName  
cd myFolderName
```  

#### 4. Follow the steps from the Pizza_Module.pdf file:  
  4a. Create a new folder called *modules*, `cd` into this new folder  
  4b. Create a new Python file called pizza.py (this is where your function will go)
  4c. After making the function, create a new file in the same directory, make_pizza.py  
  
#### 4a  

```  
mkdir modules  
cd modules  
```  

#### pizza.py  
```python  
def make_pizza(size, *toppings):
    """Puts together a virtual pizza based on a user's input"""
    print("\nMaking a " + str(size) + "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping.title())
```  

#### make_pizza.py  
Change the pizza size and their list of toppings to your favorites!  

```python  
import pizza

print("Enter 'q' at anytime to quit.")

intro = raw_input("We are going to make your favorite pizza" + "\nContinue? y/n ")

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'peppers', 'legos')
```  

#### Execute the make_pizza.py file  
Once run, the file first imports *pizza.py* to use the make_pizza() function. The last two lines of *make_pizza.py* each call the make_pizza() function and pass two arguments to it, the pizza `size` and a list of `toppings`.  

## The Takeaway  

The idea is to understand how modules are used. There are a slew of already-made modules you can use from the Python Package Index: [https://pypi.org/](https://pypi.org/). When you use these modules, you don't have to concern yourself with all the code behind them. You only have to focus on how to import and use them in your own programs. This enables you to work more efficiently, as you don't have to reinvent the wheel.  

When you create your own function (or functions), you can use them in your other programs without having to write the code over again. You can simply use `import`. Just make sure the file you want to import can be found by the file you are calling it from. A simple way to make this happen is to ensure the file imported is in the same directory as the file you are importing it from.  

*To be updated: steps on using the pizza_py pygame files*  
