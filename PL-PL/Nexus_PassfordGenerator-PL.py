import random
import string
import subprocess
import sys

subprocess.run(['clear'])

class Colors:
    yellow = "\033[93m"  # zmiana koloru na żółty

logo = Colors.yellow + '''
   ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
   ░░░░░░░░░▄▀█▀█▄██████████▄▄░░░░░░░░
   ░░░░░░░░▐██████████████████▌░░░░░░░
   ░░░░░░░░███████████████████▌░░░░░░░
   ░░░░░░░▐███████████████████▌░░░░░░░
   ░░░░░░░█████████████████████▄░░░░░░
   ░░░░▄█▐█▄█▀█████████████▀█▄█▐█▄░░░░
   ░░▄██▌██████▄█▄█▄█▄█▄█▄█████▌██▌░░░
   ░▐████▄▀▀▀▀████████████▀▀▀▀▄███░░░░
   ░▐█████████▄▄▄▄▄▄▄▄▄▄▄▄██████▀░░░░░
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
    choice = input("Program xclip nie jest zainstalowany. Czy chcesz go zainstalować? [Tak/Nie]: ")
    if choice.lower() == 'tak':
        subprocess.run(['sudo', 'apt-get', 'install', 'xclip'])
        return True
    else:
        print("Nie zainstalowano programu xclip.")
        return False

def main():
    while True:
        print(logo)
        print("[1] Hasło PIN")
        print("[2] Normalne Hasło")
        print("[3] Bezpieczne hasło")
        print("[4] Wyjdź z programu")
        choice = input("Wybierz rodzaj hasła: ")
        
        if choice == '1':
            length = int(input("Podaj długość hasła: "))
            password = generate_pin(length)
        elif choice == '2':
            length = int(input("Podaj długość hasła: "))
            password = generate_password(length)
        elif choice == '3':
            length = int(input("Podaj długość hasła: "))
            password = generate_secure_password(length)
        elif choice == '4':
            print("Naura!")
            subprocess.run(['clear'])  # Czyszczenie okna terminala (dla systemu Linux)
            subprocess.run(['python', 'nexus.py'])
        else:
            print("Niepoprawny wybór.")
            continue
        
        print("Wygenerowane hasło:", password)
        
        while True:
            print("[1] Skopiuj hasło")
            print("[2] Powrót do menu")
            option = input("Wybierz opcję: ")
            
            if option == '1':
                if not check_xclip_installed():
                    if not install_xclip():
                        break
                subprocess.run(['xclip', '-selection', 'clipboard'], input=password, text=True)  # Skopiowanie hasła do schowka w systemie (Linux)
                print("Hasło zostało skopiowane.")
                break
            elif option == '2':
                subprocess.run(['python', 'passford.py'])
            else:
                print("Niepoprawny wybór.")
                continue
        
        break

if __name__ == '__main__':
    main()

