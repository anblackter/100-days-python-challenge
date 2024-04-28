from menu import Menu, MenuItem
from coffe_maker import CoffeeMaker
from money_machine import MoneyMachine


is_on = True
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
while is_on:
    choice = input(f"What would you like? ({menu.get_items()}): ")

    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(order_name=choice)
        if coffee_maker.is_resource_sufficient(drink=drink):
            if money_machine.make_payment(cost=drink.cost):
                coffee_maker.make_coffee(order=drink)