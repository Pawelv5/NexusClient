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
░▒▓██Version 1.0 (official release)██▓▒░
░▒▓██                              ██▓▒░
░▒▓██                              ██▓▒░
░▒▓██ Released by:   Ephidev 2023  ██▓▒░
░▒▓██████████████████████████████████▓▒░
 Please check updates and report issues
            on Nexus GitHub
\033[0m'''

def main():
    print(logo)
    print("Welcome to Nexus Client!")
    print("[1] Run InfoIP")
    print("[2] Run Passford creator")
    print("[3] Update NexusClient")
    print("[4] Exit the program")
    choice = input("Choose an option: ")
    
    if choice == '1':
        subprocess.run(['clear'])  # Clear the terminal window (for Linux system)
        subprocess.run(['python', 'Nexus_AboutIP-EN.py'])
    elif choice == '2':
        subprocess.run(['clear'])  # Clear the terminal window (for Linux system)
        subprocess.run(['python', 'Nexus_PassfordGenerator-EN.py'])
    elif choice == '3':
        subprocess.run(['clear'])  # Clear the terminal window (for Linux system)
        subprocess.run(['python', 'Nexus_Client-EN.py'])
    elif choice == '4':
        print("Exiting the program.")
    else:
        print("Invalid choice.")
        
if __name__ == '__main__':
    main()

