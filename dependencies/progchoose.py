import dependencies.clearmod as clear
import dependencies.calc as calc
import dependencies.wallp as wallp
import time,os

def get_username():
    username_file_path = os.path.join(".nec", "creds")
    if os.path.exists(username_file_path):
        with open(username_file_path, "r") as file:
            return file.readline().strip()
    else:
        return None

def store_username(username):
    folder_path = ".nec"
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    username_file_path = os.path.join(folder_path, "creds")
    with open(username_file_path, "w") as file:
        file.write(username)

def progchooser():
    a = get_username()

    if a is None:
        a = input("Enter your username: ")
        store_username(a)

    print(f"Welcome, {a}!")
    print("Choose any program of your wish using the numbers.")
    print("Enter anything else to shut down Cra-OS.")
    print()
    print("""
    0 - Change Wallpaper
    1 - Simple Calculator
    2 - """)
    print()

    choice = input("Enter your choice > ")

    if choice == "0":
        clear.clear()
        print("Now loading [Change Wallpaper]...")
        time.sleep(5)
        clear.clear()
        wallp.wallp()
        
    elif choice == "1":
        clear.clear()
        print("Now loading [Simple Calculator]...")
        time.sleep(5)
        clear.clear()
        calc.calc()
