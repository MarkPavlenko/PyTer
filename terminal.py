def handle_command(command):
    if command == "help":
        return "Available commands: help, exit, info"
    elif command == "exit":
        return "Exiting..."
    elif command == "info":
        art = """
PPPP   y   y  TTTTT  EEEE  RRRR  M   M
P   P   y y     T    E     R   R MM MM
PPPP     y      T    EEE   RRRR  M M M
P        y      T    E     R  R  M   M
P        y      T    EEEE  R   R M   M
"""
        return art
    else:
        return "PyTerm: unknown command"

# Main loop to keep the terminal running
while True:
    user_input = input()
    output = handle_command(user_input)
    print(output)
    if user_input == "exit":
        break