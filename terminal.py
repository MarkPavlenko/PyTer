# I integrated my own calculator program named PMDMcalc in PyTerm. Isn't it cool?

def pmdmcalc():
    operation = input("hint: + - / *. Type the symbol here: ").strip()

    if operation == "+" or operation == " +":
        num1 = float(input("Number 1: "))
        num2 = float(input("Number 2: "))
        result = num1 + num2
        return f"Result: {result}"

    elif operation == "-" or operation == " -":
        num1 = float(input("Number 1: "))
        num2 = float(input("Number 2: "))
        result = num1 - num2
        return f"Result: {result}"

    elif operation == "/" or operation == " /":
        num1 = float(input("Number 1: "))
        num2 = float(input("Number 2: "))
        result = num1 / num2
        return f"Result: {result}"

    elif operation == "*" or operation == " *":
        num1 = float(input("Number 1: "))
        num2 = float(input("Number 2: "))
        result = num1 * num2
        return f"Result: {result}"

    else:
        return "Your symbol is not supported in PMDMcalc. Please try again with another symbol."

def handle_command(command):
    command = command.strip().lower()
    if command == "help":
        return "Available commands: help, exit, info, pmdm"
    elif command == "exit":
        return "Exiting..."
    elif command == "info":
        return ("""
PPPP   y   y  TTTTT  EEEE  RRRR  M   M
P   P   y y     T    E     R   R MM MM
PPPP     y      T    EEE   RRRR  M M M
P        y      T    E     R  R  M   M
P        y      T    EEEE  R   R M   M

        PyTerm v1.0-stable
        Python: v3.8
        Created: Twenty-Third April 2024
        Operating System: MacOS
        """)
    elif command == "pmdm":
        return pmdmcalc()
    else:
        return "PyTerm: unknown command"

while True:
    user_input = input()
    output = handle_command(user_input)
    print(output)
    if user_input.lower().strip() == "exit":
        break