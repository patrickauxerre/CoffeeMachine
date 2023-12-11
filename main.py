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

money = .0


def display_resources():
    """
    Display all the resources in the coffee machine
    :return:
    """
    sufix_str = ""
    for r in resources:
        if r == "water" or r == "milk":
            sufix_str = "ml"
        elif r == "coffee":
            sufix_str = "g"
        print(f"{r}: {resources[r]}{sufix_str}")
    print("money : $" + str(money))


def get_coins(coin_name):
    while True:
        try:
            n = int(input(f"Number of {coin_name} coins: "))
            return n
        except:
            print("Invalid number...")


def get_cash():
    n1 = get_coins("quarter")
    n2 = get_coins("dimes")
    n3 = get_coins("nickles")
    n4 = get_coins("cent")
    return 0.25 * n1 + 0.1 * n2 + 0.05 * n3 + 0.01 * n4


while True:
    user_choice = input("What would you like? (espresso/latte/cappuccino):")
    if user_choice == "off":
        break
    if user_choice == "report":
        display_resources()
    else:
        if user_choice in MENU:
            enough_resource = True
            for r in resources:
                if r in MENU[user_choice]["ingredients"] and resources[r] < MENU[user_choice]["ingredients"][r]:
                    print(f"Sorry, there is not enough {r}")
                    enough_resource = False
                    break
            if enough_resource:
                user_money = get_cash()
                if user_money < MENU[user_choice]["cost"]:
                    print("Sorry that's not enough money. Money refunded.")
                else:
                    money += MENU[user_choice]["cost"]
                    for r in resources:
                        if r in MENU[user_choice]["ingredients"]:
                            resources[r] -= MENU[user_choice]["ingredients"][r]
                    if user_money > MENU[user_choice]["cost"]:
                        change = '{0:.2f}'.format(user_money - MENU[user_choice]["cost"])
                        print(f"Here is ${change} dollars in change.")
                    print(f"Here is your {user_choice}. Enjoy!. ☕")
        else:
            print("Invalid choice...")