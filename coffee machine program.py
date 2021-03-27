import time

MENU = {
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
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}



resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

'''takes in the amount of coins inserted and returns the total'''
def calculate_amount():
    print("Please insert coins:")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.10
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total



def check_quantity(ingredients):
    for item in ingredients:
        if ingredients[item] > resources[item]:
            print(f"Sorry, there is not enough {item}")
            return False
    return True

#def calculate_return(total_inserted, price):




profit = 0

water = 300
milk = 200
coffee = 100


continue_program = True

while continue_program:

    print("\n\nWelcome to the Coffeemaker")
    choice = input("What would you like? (1.espresso/2.latte/3.cappuccino) : ")
    if choice == "report":
        print(f"Milk: {milk}\n Water: {water}\n Coffee: {coffee}\n Money: {profit}")
    elif choice == "off":
        print("Turning the machine off")
        time.sleep(3)
        print("Goodbye!..")
        continue_program = False
    else:
        drink = MENU[choice]

        #if tank does not have ENOUGH:
        if check_quantity(drink["ingredients"]):
            total_amount = calculate_amount()
            price = drink["cost"]
            if price > total_amount:
                print( "Sorry, that's not enough money. Money refunded.")
            else:
                if price == total_amount:
                    print( "Thank you for the exact change.")
                elif price < total_amount:
                    refund_amount = total_amount - price
                    print(f"Here is your  ${round(refund_amount, 2)} change")
                for item in drink["ingredients"]:
                    resources[item] -= drink["ingredients"][item]

                print("Brewing your coffee.....")
                time.sleep(5)
                print(f"Thank you. Enjoy your {choice}")

                #reduce the coffee, milk, water and add the money in the total_amount of the money made

'''


'''