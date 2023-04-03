shopping_list = ["kg of pasta", "bottles of fine white wine", "loaves of bread", "apples", "pints of milk", "bananas"]

def print_shopping_list (list):
    number = 1
    print("I need to buy")
    for item in list:
        print(str(number) + " " + item)
        
        if number == 5:
            print("and")
        number += 1
    
print_shopping_list(shopping_list)