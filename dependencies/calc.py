import time
import dependencies.clearmod as clear
import dependencies.progchoose as progchoose

def calc():
    '''Calculates stuff'''

    num1 = int(input("Enter a number > "))
    num2 = int(input("Enter a number > "))
    opchoice = input("Choose an operator (+,-,*,/) > ")

    if opchoice == "+":
        print(num1+num2)
    elif opchoice == "-":
        print(num1-num2)
    elif opchoice == "*":
        print(num1*num2)
    elif opchoice == "/":
        print(num1/num2)
    else:
        print("Invalid operator!")
        time.sleep(2)
        clear.clear()
        calc()

    print("Would you like to run the program again or return to the chooser? (run / return)")
    choice = input("Enter your choice here > ")

    if choice == "run":
        clear.clear()
        print("Now loading...")
        time.sleep(2)
        calc()
    elif choice == "return":
        clear.clear()
        progchoose.progchooser()
