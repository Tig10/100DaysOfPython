from art import logo

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
    "money": 0,
}

coffee = ['☕']


def choice(selection, dic):
    for key in dic:
        if key == selection:
            selected = MENU[selection]
            return selected
    return False


def report():
    units = ['ml', 'g', '$']
    r_list = []
    for key, value in resources.items():
        if key == 'milk' or key == 'water':
            value = str(value) + units[0]
        elif key == 'coffee':
            value = str(value) + units[1]
        elif key == 'money':
            value = units[2] + str(value)
        result = f'\t{key}:\t{value}'
        r_list.append(result)
    return r_list


def check_resources(resources_dic, order_dic):
    if order_dic:
        for key in resources_dic.keys():
            if key in order_dic['ingredients']:
                if resources_dic[key] < order_dic['ingredients'][key]:
                    return key
            else:
                return False


def process_coins():
    print('Please insert coins for your purchase: ')
    q_coins = float(input('quarters, $0.25: '))
    d_coins = float(input('dimes, $0.10: '))
    n_coins = float(input('nickles, $0.05: '))
    p_coins = float(input('pennies, $0.01: '))
    total = 0.25*q_coins + 0.10*d_coins + 0.05*n_coins + 0.01*p_coins
    return total


def check_trans(total_payment, order_dic):
    cost = order_dic['cost']
    if total_payment < cost:
        return False
    elif total_payment > cost:
        return True


def resource_update(resources_dic, order_dic):
    if order_dic:
        for key in resources_dic.keys():
            if key in order_dic['ingredients']:
                resources_dic[key] = resources_dic[key] - order_dic['ingredients'][key]


print(logo)
running = True
while running:
    prompt = input('What would you like a coffee? (Type: espresso/latte/cappuccino): ')
    if prompt == 'off':
        running = False
    elif prompt == 'report':
        report = report()
        for i in report:
            print(i)
    elif prompt == 'latte' or 'espresso' or 'cappuccino':
        order = choice(prompt, MENU)
        if not order:
            print('That choice is not available. Please try again.')
            continue
        resources_check = check_resources(resources, order)
        if resources_check:
            print(f'Sorry, there\'s not enough {resources_check} '
                  f'for that drink. Choose a different one or try again later.')
            continue
        payment = process_coins()
        print(payment)
        payment_check = check_trans(payment, order)
        if not payment_check:
            print(f'Sorry that\'s not enough money. ${payment} refunded.')
        else:
            price = order['cost']
            change = payment - price
            if change > 0:
                print(f'Here is ${change:.2f} in change.')
            resources['money'] += price
            resource_update(resources, order)
            print(f'Here is your {prompt} {coffee[0]} ')



