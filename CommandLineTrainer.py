# main.py will be GUI version and CommandLineTrainer.py will be CLI version
import random
import os

print("Welcome to the Command Line Trainer!")
print("Type 'help' for a list of commands.")

while True:
    user_input = input("Enter a command: ")
    if user_input == "help":
        print("Commands:")
        print("help")
        print("start")
        print("exit")
        print("")

    elif user_input == "start":
        print("Starting...")
        print("\n\n \t\t Mental Math Training Starting \n\n ")
        break
    elif user_input == "exit":
        print("Exiting...")
        break

    else:
        print("Invalid command. Type 'help' for a list of commands.")


