# Kind of a sudo command but its name is super and it gives use you "supercommands" that a normal user can't use. Password is SECRETCOMMAND

def supercommand(command):
    password = "SECRETCOMMAND"
    enter = input("What's the secret password? Say it:")
    if enter == password:
# If the password is correct, you can use the commands above:
# Type command is repeating what you wrote.
        if command == "type":
            input("Type something:")
            return input()
# Superexit command let's you exit the super command without ending the application.
        elif command == "superexit":
            return "Superexiting..."
# I integrated my own calculator program named PMDMcalc in PyTerm.
    
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
# Help command let's you see all the commands in PyTerm.
    if command == "help":
        return "Available commands: help, exit, info, pmdm, super"
# Exit command helps you exit the PyTerm application.
    elif command == "exit":
        return "Exiting..."
# Info command let's you know the version of PyTerm and other data.
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
# PMDM command let's you use PMDMcalc directly from PyTerm.
    elif command == "pmdm":
        return pmdmcalc()
# Told about super at the start.
    elif command == "super":
        return supercommand(command)
# If there's no commands that you entered, it shows an error.
    else:
        return "PyTerm: unknown command"
# Let's you use the terminal without ending it everytime when entered a command.
while True:
    user_input = input()
    output = handle_command(user_input)
    print(output)
    if user_input.lower().strip() == "superexit":
        handle_command()
    if user_input.lower().strip() == "exit":
        break