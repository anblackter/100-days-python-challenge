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

coins = {
    "penny": 0.01,
    "nickel": 0.05,
    "dime": 0.1,
    "quarter": 0.25
}

total_money = 0

def get_resources() -> str:
    """Returns The formatted information about the current resources"""

    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    return f"Water: {water}ml\nMilk: {milk}ml\nCoffe: {coffee}g\nMoney: ${total_money}"


def consume_resources(water: int, milk: int, coffee: int) -> None:
    """Updates the current values for each resource according to the given:
        :param water: Water to be consumed
        :param milk: Milk to be consumed
        :param cofee: coffee to be consumed
    """

    resources["water"] = resources["water"] - water
    resources["milk"] = resources["milk"] - milk
    resources["coffee"] = resources["coffee"] - coffee


def check_resources(water: int, milk: int, coffee: int) -> bool:
    """Checks if the current resources are sufficient to prepare the drink
        :param water: Water to be consumed
        :param milk: Milk to be consumed
        :param cofee: coffee to be consumed

        :returns: True or False whether the resources are sufficient or not
        :rtype: bool
    """

    if resources["water"] < water:
        print("Sorry there is not enough water")
        return False
    elif resources["milk"] < milk:
        print("Sorry there is not enough milk")
        return False
    elif resources["coffee"] < coffee:
        print("Sorry there is not enough coffee")
        return False
    else:
        return True


def update_money(total_money: float, money: float) -> None:
    """Updates the global variable total_money
        :param total_money: The global variable to update
        :param money: Money to be added
    """

    total_money += money
    return total_money


def get_coins():
    """Get the coins from the user and returns it:
        :returns: The amount of coins per category
        :rtype: (float)
    """

    penny = float(input("How many pennies? "))
    nickel = float(input("How many nickels? "))
    dime = float(input("How many dimes? "))
    quarter = float(input("How many quarters? "))

    return penny, nickel, dime, quarter

def process_coins(penny: float, nickel: float, dime: float, quarter: float, drink: str) -> str:
    """Processes the coins
        :param penny: Amount of pennies
        :param nickel: Amount of nickels
        :param dime: Amount of dimes
        :param quarter: Amoun of quarters
        :param drink: Chossen drink

        :returns: The formatted answer after process coins
        :rtype: str
    """

    global total_money
    cost = MENU[drink]["cost"]
    pennies = coins["penny"] * penny
    nickels = coins["nickel"] * nickel
    dimes = coins["dime"] * dime
    quarters = coins["quarter"] * quarter
    pay = pennies + nickels + dimes + quarters

    if pay < cost:
        return "Sorry that's not enough money. Money refunded."
    else:
        total_money = update_money(total_money, cost)
        change = pay - cost
        return f"Here is ${change} in change"

def make_coffe(water: int, milk: int, coffee: int, drink: str) -> str:
    """Makes the coffe, consumes the resources:
        :param water: Water to be consumed
        :param milk: Milk to be consumed
        :param coffee: Cofee to be consumed
        :param drink: Drink to be prepared

        :returns: The drink
        :rtype: str
    """

    consume_resources(water, milk, coffee)
    return f"Here is your {drink} ☕. Enjoy!"

def coffe_machine():
    """Main method to run the coffee-machine"""

    continue_preparing = True
    while continue_preparing:
        drink = input("What would you like? (espresso/latte/cappuccino): ")
        if drink == 'espresso':
            water = MENU["espresso"]["ingredients"]["water"]
            milk = 0
            coffee = MENU["espresso"]["ingredients"]["coffee"]
        elif drink == 'latte':
            water = MENU["latte"]["ingredients"]["water"]
            milk = MENU["latte"]["ingredients"]["milk"]
            coffee = MENU["latte"]["ingredients"]["coffee"]
        elif drink == 'cappuccino':
            water = MENU["cappuccino"]["ingredients"]["water"]
            milk = MENU["cappuccino"]["ingredients"]["milk"]
            coffee = MENU["cappuccino"]["ingredients"]["coffee"]
        elif drink == 'report':
            print(get_resources())
            coffe_machine()
        else:
            continue_preparing = False
            break
        enough_resources = check_resources(water, milk, coffee)
        if enough_resources:
            penny, nickel, dime, quarter = get_coins()
            enough_money = process_coins(penny, nickel, dime, quarter, drink)
            print(enough_money)
            if enough_money.find('not enough money') < 0:
                print(make_coffe(water, milk, coffee, drink))

coffe_machine()
