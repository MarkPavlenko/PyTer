def handle_command(command):
    if command == "help":
        return "Available commands: help, exit"
    elif command == "exit":
        return "Exiting..."
    else:
        return "PyTer: unknown command"
    if command == "info":
        art = ""

while True:
    user_input = input()
    output = handle_command(user_input)
    print(output)
    if user_input == "exit":
        break

handle_command()