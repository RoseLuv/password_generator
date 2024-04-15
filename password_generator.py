from random import randint
import tkinter as tk


def write_password(password, name, url) -> None:
    src_file = open("src_file.txt", "r")
    next(src_file)
    path = src_file.readline() # Skips the first line
    src_file.close()
    f = open(path, "a")
    f.write(name + ":" + "\n")
    f.write(password + "\n")
    f.write("URL -> " + url + "\n\n")
    f.close()
    return 

def check_password(password: str) -> bool:
    number, symbol, lowercase, uppercase = False, False, False, False
    for elem in password:
        elem_ascii = ord(elem)
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

def create_password(name, url) -> bool:
    # To ensure it actually creates the password
    while True:
        password = ""
        for _ in range(16):
            # randint range [33, 126] from ! to ~ in ascii
            password = password + chr(randint(33,126))
        
        if check_password(password):
            write_password(password, name, url)
            return True

def main() -> None:
    root = tk.Tk()
    
    tk.Label(root, text="Name of the site:", font=("Arial",20), relief="solid",borderwidth=2, height=1, width=15, anchor="w").grid(row=0,column=0, padx=10, sticky="w")
    tk.Label(root, text="Url of the site:", font=("Arial",20), relief="solid",borderwidth=2, height=1, width=15, anchor="w").grid(row=3,column=0, padx=10, sticky="w")
    tk.Label(root, height=1, width=30).grid(row=2,column=0, padx=10)
    name_input = tk.Text(root, font=("Arial", 20), relief="solid",borderwidth=2, height=1, width=16)
    name_input.grid(row=1, column=0, sticky="w", padx=10)
    
    url_input = tk.Text(root, font=("Arial", 20), relief="solid",borderwidth=2, height=1, width=30)
    url_input.grid(row=4, column=0, sticky="w", padx=10)
    
    tk.Button(root, text="Confirm", font=("Arial", 20), relief="solid", borderwidth=2, height=1, width=10,\
            command=lambda: create_password(name_input.get("1.0","end-1c"), url_input.get("1.0","end-1c"))).grid(row=5,column=0, padx=10, sticky="w")
    
    
    root.mainloop()
    return


main()
