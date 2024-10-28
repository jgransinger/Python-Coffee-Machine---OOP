from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

cafe_machine = CoffeeMaker()
cafe_menu = Menu()
cafe_money = MoneyMachine()

power_on = True

while power_on:
    customer_order = input("What would you like to drink? (latte, cappuccino, or espresso): \n")
    if customer_order == "report":
        cafe_machine.report()
        cafe_money.report()
    if customer_order == "off":
        power_on = False
        print("Powering off... Goodbye.")
    else:
        menu_item = cafe_menu.find_drink(customer_order)
        if menu_item:
            if cafe_machine.is_resource_sufficient(menu_item):
                if cafe_machine.is_resource_sufficient(menu_item):
                    cafe_money.make_payment(menu_item.cost)
                    cafe_machine.make_coffee(menu_item)





