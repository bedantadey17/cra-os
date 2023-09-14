# Main File for the Project

import time,getpass
import dependencies.clearmod as clear
import dependencies.progchoose as progchoose

print("""
      Welcome to Cra-OS, a parody of ArcOS!
      Cra-OS is supposed to be a different distro of ArcOS, which has a GUI.
      On Cra-OS, there is no GUI! Everything is CLI-based, including your mother!!!
      
      Currently Cra-OS is very lackluster, unlike ArcOS, which is drier than your pe-
      Enjoy Cra-OS, I hope you will like it! You can even use it as a daily driver!
      
      """)
print("Version: 0.0.2")
print("(c) Bedanta Dey 1930-2023 | All rights reserved.")
print()
print()


def login():
    global user
    print("Let's get your Cra-OS account. This makes Cra-OS more secure and easy to use.")
    print("If you do not have a Cra-OS account, you can just sign up. Same thing.")
    print("")
    user = input("Enter a username > ")
    pword = getpass.getpass("Enter a password > ")

    if user == pword:
        print("Password cannot be same as username!")
        time.sleep(2)
        clear.clear()
        login()
    elif " " in pword:
        print("Password may not contain spaces!")
        time.sleep(2)
        clear.clear()
        login()
    else:
        print("Now Loading...")
        # with open(os.path.join('essentials', "creds"), "w") as file:
        #     file.write(f"Username: {user}\nPassword: {pword}")
        progchoose.store_username(user)
        time.sleep(5)
        clear.clear()
        progchoose.progchooser()
login()
