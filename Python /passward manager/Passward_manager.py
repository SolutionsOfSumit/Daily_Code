from cryptography.fernet import Fernet


'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)  #here wb stands for write bytes mode
'''

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

master_pwd = input("what is the master passward? ")
key = load_key() + master_pwd.encode()
fer = Fernet(key)


def view():
    with open('password.txt','r') as f: #here we are using mode 'r' because we are jsut reading the file over here
        for line in f.readlines():
            data = line.rstrip() #rstrip will remove the new line character which is \n
            user, password = data.split("|") #split will look for the character given it as parameter and split them accordingly in a list format
            print("User", user, "\n Password:", fer.decrypt(password.encode()).decode)


def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open('password.txt','a') as f: #here 'a' is a mode which means append and there are many modes which are "r" which is to read the file and "w" wich is to create and write the file.
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode + "\n")

while True:

    mode = input("Would you like to see old passward (view) or store new one (add) and to quit the program (Q)" ).lower()

    if mode ==  "q":
        break

    elif mode == "view":
        view()

    elif mode == "add":
        add()

    else:
        print("select from the given options. ")
        continue