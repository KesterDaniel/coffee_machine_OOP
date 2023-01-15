# Making the coffee machine using OOP

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


machine_on = True

while machine_on:
    user_input = input("What would you like to order? espresso/latte/cappuccino: ")
    if user_input == "report":
        CoffeeMaker.report()