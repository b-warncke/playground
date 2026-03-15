"""Simple Calculator App"""
"""Test"""

import operator

ops = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '**': operator.pow,
    '%': operator.mod,
}


def safe_float(value):
    try:
        return float(value)
    except ValueError:
        raise ValueError('Invalid number: %r' % value)


def calculate(a, operator_symbol, b):
    if operator_symbol not in ops:
        raise ValueError(f"Unsupported operator: {operator_symbol}")
    if operator_symbol == '/' and b == 0:
        raise ZeroDivisionError('Cannot divide by zero')
    return ops[operator_symbol](a, b)


def print_menu():
    print('\nPython Simple Calculator')
    print('Supported operators: +  -  *  /  **  %')
    print('Enter expressions like: 2 + 2, 5**3, 10 / 4')
    print('Type q or quit to exit.')


def main():
    print_menu()

    while True:
        expression = input('> ').strip()
        if expression.lower() in ('q', 'quit', 'exit'):
            print('Goodbye!')
            break

        # basic split parsing
        parts = expression.split()
        if len(parts) == 3:
            x_str, op, y_str = parts
        else:
            # fallback to minimal parsing for no spaces (e.g., 2+2, 3**2)
            for candidate in sorted(ops.keys(), key=len, reverse=True):
                if candidate in expression:
                    x_str, y_str = expression.split(candidate, 1)
                    op = candidate
                    break
            else:
                print('Invalid expression format. Use <num> <op> <num>.')
                continue

        try:
            x = safe_float(x_str)
            y = safe_float(y_str)
            result = calculate(x, op, y)
            print('= ', result)
        except Exception as e:
            print('Error:', e)


if __name__ == '__main__':
    main()

