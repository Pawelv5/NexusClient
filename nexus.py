import subprocess

subprocess.run(['clear'])
logo = '''
\033[34m
░▒▓████████████████►╬◄███████████████▓▒░
░▒▓██ ╔╦═╦╦══════════╦═╦╦╦════╦╦═╗ ██▓▒░
░▒▓██ ║║║║╠═╦╦╦╗╔╦══╗║╔╣╠╬═╦═╦╣╠╗║ ██▓▒░
░▒▓██ ║║║║║╩╬.╣╚╝╠╗╚╣║╚╣║║╩╣║╠╗╔╣║ ██▓▒░
░▒▓██ ║╚╩═╩═╩╩╩══╩══╝╚═╩╩╩═╩╩╝╚═╝║ ██▓▒░
░▒▓██ ╚══════════════════════════╝ ██▓▒░
░▒▓████████████████►╬◄███████████████▓▒░
░▒▓██████████████████████████████████▓▒░
░▒▓██ Wersja 1.0(oficjalne wydanie)██▓▒░
░▒▓██                              ██▓▒░
░▒▓██                              ██▓▒░
░▒▓██ Wydano przez:   Ephidev 2023 ██▓▒░
░▒▓██████████████████████████████████▓▒░
\033[0m'''

def main():
    print(logo)
    print("Witaj w kliencie Nexus!")
    print("[1] Uruchom InfoIP")
    print("[2] Uruchom Passford creator")
    print("[3] Wyjdź z programu")
    choice = input("Wybierz opcję: ")
    
    if choice == '1':
        subprocess.run(['clear'])  # Czyszczenie okna terminala (dla systemu Linux)
        subprocess.run(['python', 'Iphacker.py'])
    elif choice == '2':
        subprocess.run(['clear'])  # Czyszczenie okna terminala (dla systemu Linux)
        subprocess.run(['python', 'passford.py'])
    elif choice == '3':
        print("Wyjście z programu.")
    else:
        print("Niepoprawny wybór.")

if __name__ == '__main__':
    main()
