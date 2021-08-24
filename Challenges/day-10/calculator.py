from art import logo

print(logo)

# Calculator


def add(n1, n2):    # Add
    return n1 + n2


def subtract(n1, n2):   # Subtract
    return n1 - n2


def multiply(n1, n2):   # Multiply
    return n1 * n2


def divide(n1, n2):     # Divide
    return n1 / n1


operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}


def calculator():
    calculate = True
    num1 = input('What\'s the first number?: ')
    if num1 == 'quit':
        return
    num1 = float(num1)
    for symbol in operations:
        print(symbol)

    while calculate:
        operation_symbol = input('Pick an operation: ')
        num2 = float(input('What\'s the second number?: '))
        calc = operations[operation_symbol]
        answer = calc(num1, num2)

        print(f'{num1} {operation_symbol} {num2} = {answer}')
        stop_calc = input(f'Type \'y\' to continue with {answer}, or type \'n\' to exit.: ')
        if stop_calc == 'y':
            num1 = answer
        else:
            calculate = False
            calculator()


calculator()