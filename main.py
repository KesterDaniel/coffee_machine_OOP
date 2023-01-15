# Making the coffee machine using OOP

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee = CoffeeMaker()
menu = Menu()
payment = MoneyMachine()


machine_on = True

while machine_on:
    user_input = input("What would you like to order? espresso/latte/cappuccino: ")
    if user_input == "report":
        coffee.report()
        payment.report()
    elif user_input == "off":
        machine_on = False
    else:
        order_item = menu.find_drink(user_input)
        if order_item is not None:
            drink_available = coffee.is_resource_sufficient(order_item)
            if drink_available:
                item_cost = order_item.cost
                payment_success = payment.make_payment(item_cost)
                if payment_success:
                    coffee.make_coffee(order_item)





