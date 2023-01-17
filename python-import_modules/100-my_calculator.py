#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    import calculator_1
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a, b, operator = int(argv[1]), int(argv[3]), argv[2]
    if operator == '+':
        result = a + b
    elif operator == '-':
        result = a - b
    elif operator == '*':
        result = a * b
    elif operator == '/':
        result = a // b
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    print(a, operator, b, '=', result)
