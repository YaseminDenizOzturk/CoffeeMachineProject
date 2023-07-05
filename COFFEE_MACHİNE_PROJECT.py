hot_drinks_menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "mocha": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    },
    "americano": {
        "ingredients": {
            "water": 175,
            "milk": 75,
            "coffee": 30,
        },
        "cost": 1.5,
        
    },

    "macchiato": {
        "ingredients": {
            "water": 130,
            "milk": 75,
            "coffee": 32,
        },
        "cost": 3.5,
        
    }
}

money = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# kaynak yeterli mi
def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"​Sorry there is not enough {item}.")
            return False
    return True

# hangi paralar
def process_coins():
    
    print("Please insert coins")
    total = int(input("how many quarters?\n ")) * 0.25
    total += int(input("how many dimes?\n ")) * 0.1
    total += int(input("how many nickles?\n ")) * 0.05
    total += int(input("how many pennies?\n ")) * 0.01
    return total

# para işlem için yeterli mi değil mi
def is_transaction_successful(money_received, drink_cost):
    
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global money
        money += drink_cost
        return True
    else:
        print("Sorry that's not enough money so money refunded.")
        return False

# kahveyi yap
def make_coffee(drink_name, order_ingredients):
    
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️ enjoy!")

def degree():
    a = input("Would you like a custom temperature setting? 'Y' or 'N' \n").lower()
    if a == "y":
        degree = int(input(f"How many degrees should your {drink_selection} be: "))
        print(f"Your {drink_selection} is {degree} degrees.")
    else:
        print("No temperature adjustment was made")
    


control_variable = True

while control_variable:
    print("Welcome!")
    print("☕️☕️☕️ I'm a very smart coffee machine! ☕️☕️☕️")
    print("I can only make hot drinks☕️")
    drink_selection = input("​What would you like?\nespresso\nlatte\nmocha\namericano\nmacchiato\nREPORT\n").lower()
    # tamir durumlarında off seçeneği kullanılarak makine kapatılıp bakım yapılabilir .
    if drink_selection == "OFF":
        control_variable = False
    elif drink_selection == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${money}")
    else:
        #a = input("Would you like a custom temperature setting? 'Y' or 'N' \n").lower()
        #if a == "y":
            #degree = int(input(f"How many degrees should your {drink_selection} be: "))
            
        drink = hot_drinks_menu[drink_selection]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                degree()
                make_coffee(drink_selection, drink["ingredients"])
                
            #print(f"Your {drink_selection} is {degree} degrees.")
        else:

            print("Good choice...")
            drink = hot_drinks_menu[drink_selection]
            if is_resource_sufficient(drink["ingredients"]):
                payment = process_coins()
                if is_transaction_successful(payment, drink["cost"]):
                    make_coffee(drink_selection, drink["ingredients"])




