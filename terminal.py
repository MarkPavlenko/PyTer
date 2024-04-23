# Kind of a sudo command but its name is super and it gives use you "supercommands" that a normal user can't use. Password is SECRETCOMMAND
def supercommand():
    password = "SECRETCOMMAND"
    enter = input("What's the secret password? Say it:")
    if enter == password:
        # If the password is correct, you can use the commands above:
        while True:
            command = input("You're in super mode. Type any supercommand:").strip().lower()
            if command == "type":
                typed_text = input("Type something:")
                return typed_text
            elif command == "superexit":
                return "Superexiting..."
            elif command == "superhelp":
                return "type, superexit, superhelp,"
            else:
                print("No such command in super mode.")
    else:
        return "Wrong password! You can't use the super command without the password."

def pmdmcalc():
    operation = input("hint: + - / *. Type the symbol here: ").strip()

    if operation in ["+", " +"]:
        num1 = float(input("Number 1: "))
        num2 = float(input("Number 2: "))
        return f"Result: {num1 + num2}"

    elif operation in ["-", " -"]:
        num1 = float(input("Number 1: "))
        num2 = float(input("Number 2: "))
        return f"Result: {num1 - num2}"

    elif operation in ["/", " /"]:
        num1 = float(input("Number 1: "))
        num2 = float(input("Number 2: "))
        return f"Result: {num1 / num2}"

    elif operation in ["*", " *"]:
        num1 = float(input("Number 1: "))
        num2 = float(input("Number 2: "))
        return f"Result: {num1 * num2}"

    else:
        return "Your symbol is not supported in PMDMcalc. Please try again with another symbol."

def handle_command(command):
    command = command.strip().lower()
    # Help command lets you see all the commands in PyTerm.
    if command == "help":
        return "Available commands: help, exit, info, pmdm, super"
    # Exit command helps you exit the PyTerm application.
    elif command == "exit":
        return "Exiting..."
    # Info command lets you know the version of PyTerm and other data.
    elif command == "info":
        return """
PPPP   y   y  TTTTT  EEEE  RRRR  M   M
P   P   y y     T    E     R   R MM MM
PPPP     y      T    EEE   RRRR  M M M
P        y      T    E     R  R  M   M
P        y      T    EEEE  R   R M   M

        PyTerm v1.0-stable
        Python: v3.8
        Created: Twenty-Third April 2024
        Operating System: MacOS
        """
    # PMDM command lets you use PMDMcalc directly from PyTerm.
    elif command == "pmdm":
        return pmdmcalc()
    # Told about super at the start.
    elif command == "super":
        return supercommand()
    # If there's no commands that you entered, it shows an error.
    else:
        return "PyTerm: unknown command"

# Lets you use the terminal without ending it every time when entered a command.
while True:
    user_input = input()
    output = handle_command(user_input)
    print(output)
    if user_input.lower().strip() == "exit":
        break