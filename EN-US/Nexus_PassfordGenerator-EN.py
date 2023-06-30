import random
import string
import subprocess
import sys

subprocess.run(['clear'])

class Colors:
    yellow = "\033[93m"  # change color to yellow

logo = Colors.yellow + '''
   ...
   ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
   ░░░░░░░░░▄▀█▀█▄██████████▄▄░░░░░░░░
   ░░░░░░░░▐██████████████████▌░░░░░░░
   ░░░░░░░░███████████████████▌░░░░░░░
   ░░░░░░░▐███████████████████▌░░░░░░░
   ░░░░░░░█████████████████████▄░░░░░░
   ░░░░▄█▐█▄█▀█████████████▀█▄█▐█▄░░░░
   ░░▄██▌██████▄█▄█▄█▄█▄█▄█████▌██▌░░░
   ░▐████▄▀▀▀▀████████████▀▀▀▀▄███░░░░
   ░░░░▀▀████████████████████░░░░░░░░░
   ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
   ░░░░░░░╔╦═╦═══════╦═╦════╦╦╗░░░░░░░
   ░░░░░░░║║░╠═╦══╦══╣╩╬═╦═╦╝║║░░░░░░░
   ░░░░░░░║║╔╬╝╠╗╚╬╗╚╣╦╣║║╠╣║║║░░░░░░░
   ░░░░░░░║╚╝╚═╩══╩══╩╝╚═╩╝╚═╝║░░░░░░░
   ░░░░░░░╚═══════════════════╝░░░░░░░
   ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
   ░░░░░░╔╦══╦══════════╦╦═════╗░░░░░░
   ░░░░░░║║╔═╬═╦═╦═╦═╦═╦╣╠╦═╦═╗║░░░░░░
   ░░░░░░║║╚╝║╩╣║║╩╣╠╬╝╠╗╔╣║║╠╝║░░░░░░
   ░░░░░░║╚══╩═╩╩╩═╩╝╚═╝╚═╩═╩╝.║░░░░░░
   ░░░░░░╚═════════════════════╝░░░░░░
   ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
'''

def generate_password(length):
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_pin(length):
    pin = ''.join(random.choice(string.digits) for _ in range(length))
    return pin

def generate_secure_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def check_xclip_installed():
    try:
        subprocess.run(['xclip', '-version'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
    except FileNotFoundError:
        return False

def install_xclip():
    choice = input("Program xclip is not installed. Do you want to install it? [Yes/No]: ")
    if choice.lower() == 'yes':
        subprocess.run(['sudo', 'apt-get', 'install', 'xclip'])
        return True
    else:
        print("xclip program is not installed.")
        return False

def main():
    while True:
        print(logo)
        print("[1] PIN Password")
        print("[2] Normal Password")
        print("[3] Secure Password")
        print("[4] Exit the program")
        choice = input("Choose a password type: ")
        
        if choice == '1':
            length = int(input("Enter the password length: "))
            password = generate_pin(length)
        elif choice == '2':
            length = int(input("Enter the password length: "))
            password = generate_password(length)
        elif choice == '3':
            length = int(input("Enter the password length: "))
            password = generate_secure_password(length)
        elif choice == '4':
            print("Goodbye!")
            subprocess.run(['clear'])  # Clear the terminal window (for Linux system)
            subprocess.run(['python', 'Nexus_Client-EN.py'])
        else:
            print("Invalid choice.")
            continue
        
        print("Generated password:", password)
        
        while True:
            print("[1] Copy Password")
            print("[2] Back to menu")
            option = input("Choose an option: ")
            
            if option == '1':
                if not check_xclip_installed():
                    if not install_xclip():
                        break
                subprocess.run(['xclip', '-selection', 'clipboard'], input=password, text=True)  # Copy password to clipboard (Linux)
                print("Password has been copied.")
                break
            elif option == '2':
                subprocess.run(['python', 'Nexus_PassfordGenerator-EN.py'])
            else:
                print("Invalid choice.")
                continue
        
        break

if __name__ == '__main__':
    main()

