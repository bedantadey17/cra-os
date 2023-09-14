import time, platform
import dependencies.clearmod as clear
import dependencies.progchoose as progchoose


def terminal_prompt():
    '''Cra-OS Terminal Emulator'''
    global command
    command = input("> ")
    comms_handler(command)

def comms_handler(command):
    if command.lower() == 'crafetch':
        print(f"""
        CRA-OS Ver. 0.0.2
        Created by Bedanta Dey
              
        _________  
        \_   ___ \      Computer Name: {platform.node()}
        /    \  \/      Platform: {platform.platform()}
        \     \____     Processor: {platform.processor()}
         \______  /     Machine Type: {platform.machine()}
                \/      Python Version: {platform.python_version()}
              
              """)
        terminal_prompt()
    if command.lower() == 'help':
        print("""
        List of available commands:
            crafetch - Displays system information
            help - Displays list of available commands
            exit - Exits terminal peacefully
            """)
        terminal_prompt()
    if command.lower() == 'exit':
        print("Terminal terminated with code (0)")
        clear.clear()
        progchoose.progchooser()
    else:
        print("Invalid command. This may happen if your command syntax is wrong or the command doesn't exist. Try 'help' for list of available commands.")
        terminal_prompt()



    # print("Would you like to run the program again or return to the chooser? (run / return)")
    # choice = input("Enter your choice here > ")

    # if choice == "run":
    #     clear.clear()
    #     print("Now loading...")
    #     time.sleep(2)
    #     terminal_prompt()
    # elif choice == "return":
    #     clear.clear()
    #     progchoose.progchooser()
