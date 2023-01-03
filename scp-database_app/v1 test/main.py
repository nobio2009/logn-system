from acinfo import *
import scpscraper as scps
import pwinput
import os
import time
import hashlib

def startup():
    os.system('clear')

    print('SCP FOUNDATION DATABASE')

    time.sleep(1)

    os.system('clear')

    option()

def option():
    login_options = ['login']
    sign_in_options = ['signin', 'sign in']

    choice = input('(LOGIN) OR (SIGN IN): ').lower()

    if choice in login_options:
        login()
    elif choice in sign_in_options:
        print('SIGN IN')
        
    else:
        print('NOT AN OPTION')
        time.sleep(0.5)
        os.system('clear')
        option()


def  login():
    while True:
        input_user = input('USERNAME: ').encode()
        enc_user = hashlib.sha1(input_user).hexdigest()

        if enc_user == username:
            break
        else:
            print('UNKNOWN USER IF YOU WANT TO')

    while True:
        time.sleep(0.5)
        os.system('clear')

        input_password = pwinput.pwinput().encode()
        enc_password = hashlib.sha1(input_password).hexdigest()

        if enc_password == password:
            print('SUCCESSFULLY LOGGED IN')
            break
        else:
            print('INCORRECT PASSWORD')
            time.sleep(1)
            os.system('clear')

def signin():

    user = input('USERNAME: ').encode()
    enc_user = hashlib.sha1(user).hexdigest()
    
    time.sleep(0.5)

    passw = pwinput.pwinput().encode()
    enc_pass = hashlib.sha1(passw).hexdigest

    f = open('acinfo.py', 'w')
    f.write(f'username = \'{enc_user}\'' + '\n')
    f.write(f'password = \'{enc_pass}\'' + '\n')
    f.close()

    login()

startup()