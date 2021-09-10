from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine = CoffeeMaker()
money = MoneyMachine()
menu_item = Menu()

running = True
while running:
    choice = input('What would you like? (espresso/latte/cappuccino): ')
    if choice == 'off':
        running = False
    elif choice == 'report':
        machine.report()
        money.report()
    else:
        order = menu_item.find_drink(choice)
        if not order:
            continue
        check_resources = machine.is_resource_sufficient(order)
        if not check_resources:
            continue
        price = order.cost
        is_money_enough = money.make_payment(price)
        if is_money_enough:
            machine.make_coffee(order)
