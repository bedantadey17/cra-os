import platform,os

def clear():
    '''Clear Function'''
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')