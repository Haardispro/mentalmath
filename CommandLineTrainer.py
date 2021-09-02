# main.py will be GUI version and CommandLineTrainer.py will be CLI version
import random
import os

print("Welcome to the Command Line Trainer!")
print("Type 'help' for a list of commands.")
def Start():
    username = input("Enter your name: ")
    noOfquestions = int(input("How many questions would you like to answer? "))
    score = 0
    for i in range(noOfquestions):
        
        answer = 0
        numOne = random.randint(10,20)
        numTwo = random.randint(1,10)
        pickOperator = random.randint(1,3)
        if pickOperator == 1:
            sign = " + "
            answer = numOne + numTwo
        elif pickOperator == 2:
            sign = " - "
            answer = numOne - numTwo
        elif pickOperator == 3:
            sign = " * "
            answer = numOne * numTwo
        else:
            print ("LUL you messed up the code !")
        question = "What is " + str(numOne) + sign + str(numTwo) + " : "
        user_answer = int(input(question))
        if user_answer == answer:
            score = score + 1
        else:
            print()
            

    print(f"\n\t\tRobot Maks : {username} you got " + str(score) + f" out of {noOfquestions}")
    # Optional Code for making a file with result of your mental math score.
    # Sasta Database 
    # f = open("Result.txt", "w")
    # f.write(f"Robot Maks : {username} you got " + str(score) + f" out of {noOfquestions}")
    # os.open("Result.txt", os.O_RDWR)
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
        Start()
        print("\n\n \t\t Mental Math Training Finished \n\n ")
        break        
    elif user_input == "exit":
        print("Exiting...")
        break

    else:
        print("Invalid command. Type 'help' for a list of commands.")


