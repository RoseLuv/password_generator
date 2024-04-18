import tkinter as tk
import sys
from random import randint


def check_password(password: str) -> bool:
    number, symbol, lowercase, uppercase = False, False, False, False
    for elem in password:
        elem_ascii = elem - 125
        if elem_ascii >= 65 and elem_ascii <= 90:
            uppercase = True
        elif elem_ascii >= 97 and elem_ascii <= 122:
            lowercase = True
        elif elem_ascii >= 48 and elem_ascii <= 57:
            number = True
        else:
            symbol = True

        if uppercase and lowercase and number and symbol:
            return True
    return False

def write_password(password:str, name:str) -> None:
    f = open("passwords.txt", "a")
    f.write(name + "\n")
    for item in password:
        f.write('%d' % item)
        f.write(" ")
    f.write("\n")
    f.close()
    return 

def create_password():
    while True:
        password = []
        for _ in range(16):
            password.append((randint(33,126) + 125))
        if check_password(password):
            return password

def pswd_in():
    site = input("In - Enter site name:\n")
    password = create_password()
    write_password(password, site)
    return


def pswd_get():
    site = input("Get - Enter site name:\n")
    f = open("passwords.txt", "r")
    line = f.readline()
    while line.strip() != site:
        line = f.readline()
    
    password = f.readline()
    f.close()
    password = password.split()
    for i in range(16):
        password[i] = chr(int(password[i]) - 125)
    password = ''.join(password)
    print(password)
    return

def pswd_list():
    f = open("passwords.txt", "r")
    line = f.readline()
    while line.strip() != '':
        print(line)
        line = f.readline()
        line = f.readline()
    f.close()

FUNCTIONS = {
    "get": pswd_get,
    "in": pswd_in,
    "list": pswd_list
}

def main():
    print("Available commands:\n\
                            Get - prints the password onto the stdout\n\
                            In - creates a password for a site and encodes it onto a txt file.\n\
                            List - Prints the names of sites that have a password")

    while True:
        command = input("Enter command ('quit' to exit): ").lower()
        if command == "quit":
            break
        
        if command in FUNCTIONS:
            FUNCTIONS[command]()
        else:
            print("Unknown command.")


if __name__ == "__main__":
    main()