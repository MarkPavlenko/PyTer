# Kind of a sudo command but its name is super and it gives use you "supercommands" that a normal user can't use. Password is etsugenfgr.
def supercommand():
    password = "etsugenfgr"
    enter = input("Password:") 
    if enter == password:
        print("You are now in super mode.")
        while True:
            command = input().strip().lower()
            if command == "":
                continue 
            elif command == "supertype":
                typed_text = input("Type something:")
                print(typed_text + typed_text)
            elif command == "superexit":
                return "Superexiting..."
            elif command == "superinfo":
                print("""
    PPPP   y   y  TTTTT  EEEE  RRRR  M   M 
    P   P   y y     T    E     R   R MM MM       
    PPPP     y      T    EEE   RRRR  M M M       
    P        y      T    E     R  R  M   M      
    P        y      T    EEEE  R   R M   M SUPER MODE
                      
                PyTerm Supermode v1.0
                Python: v3.8
                Version Created: Twenty-Third April 2024
                Initial Day Of Creation: Twenty-Third April 2024
                Application: PyTerm v0.1-beta
                
                """)
            elif command == "superhelp":
                print("Commands: supertype, superexit, superinfo, superhelp. Add-ons: -h")
            elif command == "supertype -h":
                print("Supertype command represents everything that you wrote twice. It is similar to type command in basic-user mode but this one is showing different output.") 
            elif command == "superexit -h":
                print("Superexit command is letting you exit from the super mode. It is similar to exit command in basic-user mode but this one is exiting the supermode.") 
            elif command == "superinfo -h":
                print("Superinfo command shows you info-data about PyTerm Supermode. It is similar to info command in basic-user mode but this one is showing different info.")
            elif command == "superhelp -h":
                print("Superhelp command shows you all commands you can use in supermode. It is similar to help command in basic-user mode but this one shows different commands.")
            else:
                print("No such command in supermode.")
    else:
        print("PyTerm error: wrong password.")

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

        PyTerm v0.1-beta
        Python: v3.8
        Version Created: Twenty-Third April 2024
        Initial Day Of Creation: Twenty-Third April 2024
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