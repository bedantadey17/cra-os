import time
import dependencies.clearmod as clear
import dependencies.progchoose as progchoose

def wallp():
    '''Wallpaper Changer'''
    print("Choose your desired wallpaper from the list below:")
    print()
    print("""
    1 - Sunset Valley
    2 - Blissful Spikes
    3 - Serene Mountains
    4 - Blue Rhododendrons
    5 - Sussy Impostor
    6 - Ruined Towers
    7 - Defiled Church
    8 - Neu-Berlin
    9 - Endermensch's Lair      
    
    NOTE: Due to this being a CLI-based app, no wallpaper can be seen. This is purely a cosmetic change.
          
    """)

    wallch = input("Enter wallpaper number > ")

    if wallch == "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9":
        clear.clear()
        print("Now applying wallpaper...")
        time.sleep(2)
        print("Wallpaper successfully applied!")
        print()


    print("Would you like to run the program again or return to the chooser? (run / return)")
    choice = input("Enter your choice here > ")

    if choice == "run":
        clear.clear()
        print("Now loading...")
        time.sleep(2)
        wallp()
    elif choice == "return":
        clear.clear()
        progchoose.progchooser()
