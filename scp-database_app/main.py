import hashlib
import pwinput
import time
from users import *


def replace_line(file_name, line_num, text):
    lines = open(file_name, 'r').readlines()
    lines[line_num] = text
    out = open(file_name, 'w')
    out.writelines(lines)
    out.close()

amount = amount

def signin():
    global amount
    amount += 1
    replace_line('users.py', 0, f'amount = {amount}\n')
    enc_amount = hashlib.sha1(str(amount).encode()).hexdigest()

    inp_username = input('USERNAME: ').encode()
    enc_username = hashlib.sha1(inp_username).hexdigest()

    time.sleep(1)

    inp_pass = pwinput.pwinput('PASSWORD: ').encode()
    enc_pass = hashlib.sha1(inp_pass).hexdigest()

    # Append-adds at last
    file1 = open("users.py", "a") # append mode
    file1.write('\n' + f'_{amount} = ' + '{' + f'\'username\' : \'{enc_username}\', \'password\' : \'{enc_pass}\'' + '}' + '\n')
    file1.close()

    users = user
    users.append(f'_{amount}')

    replace_line('users.py', 2, f'user = {users}\n')

def login():
    pass

signin()