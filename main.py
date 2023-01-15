# Making the coffee machine using OOP

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee = CoffeeMaker()
menu = Menu()

machine_on = True

while machine_on:
    user_input = input("What would you like to order? espresso/latte/cappuccino: ")
    if user_input == "report":
        coffee.report()
    elif user_input == "off":
        machine_on = False
    else:
        order_item = menu.find_drink(user_input)
        if order_item is not None:
            drink_available = coffee.is_resource_sufficient(order_item)
            print(drink_available)

