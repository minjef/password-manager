from cryptography.fernet import Fernet


def main():
    #write_key()
    while True:
        mode = input("Would you like to add a new password or view existing passwords (add/view), press Q to quit :").lower()

        if mode == "q":
            break

        if mode == "add":
            add()

        elif mode == "view":
            view()
        else:
            continue

'''def write_key():
    key = Fernet.generate_key()
    with open("password-manager/key.key", "wb") as key_file:
        key_file.write(key)'''

def load_key():
    file = open("password-manager/key.key", "rb")
    key = file.read()
    file.close()
    return key



key = load_key()
fer = Fernet(key)


def view():
    with open('password-manager/password.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("user:", user, "| Password:", fer.decrypt(passw.encode()).decode())

def add():
    name = input("Account name: ")
    pwd = input("Password: ")

    with open('password-manager/password.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")



main()