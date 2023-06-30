import os
import requests
import subprocess
import sys
import webbrowser

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
░▒▓██ Pobierz/zaaktualizuj klienta ██▓▒░
░▒▓██ Instalator NexusTerminal     ██▓▒░
░▒▓██ Wydano przez:   Ephidev 2023 ██▓▒░
░▒▓██████████████████████████████████▓▒░
\033[0m'''

download = '''
\033[0m''']
░▒▓████████████████►╬◄███████████████▓▒░
░▒▓██ ╔╦═╦╦══════════╦═╦╦╦════╦╦═╗ ██▓▒░
░▒▓██ ║║║║╠═╦╦╦╗╔╦══╗║╔╣╠╬═╦═╦╣╠╗║ ██▓▒░
░▒▓██ ║║║║║╩╬.╣╚╝╠╗╚╣║╚╣║║╩╣║╠╗╔╣║ ██▓▒░
░▒▓██ ║╚╩═╩═╩╩╩══╩══╝╚═╩╩╩═╩╩╝╚═╝║ ██▓▒░
░▒▓██ ╚══════════════════════════╝ ██▓▒░
░▒▓████████████████►╬◄███████████████▓▒░
░▒▓██████████████████████████████████▓▒░
░▒▓██ Instalowanie, proszę czekać..██▓▒░
░▒▓██ Proszę nie zamykkać programu ██▓▒░
░▒▓██ Błedy zgłaszać na github     ██▓▒░
░▒▓██ Wydano przez:   Ephidev 2023 ██▓▒░
░▒▓██████████████████████████████████▓▒░
'''


error = '''
\033[0m''']
░▒▓████████████████►╬◄███████████████▓▒░
░▒▓██ ╔╦═╦╦══════════╦═╦╦╦════╦╦═╗ ██▓▒░
░▒▓██ ║║║║╠═╦╦╦╗╔╦══╗║╔╣╠╬═╦═╦╣╠╗║ ██▓▒░
░▒▓██ ║║║║║╩╬.╣╚╝╠╗╚╣║╚╣║║╩╣║╠╗╔╣║ ██▓▒░
░▒▓██ ║╚╩═╩═╩╩╩══╩══╝╚═╩╩╩═╩╩╝╚═╝║ ██▓▒░
░▒▓██ ╚══════════════════════════╝ ██▓▒░
░▒▓████████████████►╬◄███████████████▓▒░
░▒▓██████████████████████████████████▓▒░
░▒▓██Instalowanie, się nie powiodło██▓▒░
░▒▓██ Czy ponowić próbę instalacji?██▓▒░
░▒▓██                              ██▓▒░
░▒▓██ Wydano przez:   Ephidev 2023 ██▓▒░
░▒▓██████████████████████████████████▓▒░
'''

def handle_error(download, error):
    print("\nWystąpił błąd:")
    print(error)
    print("[1] Spróbuj ponownie od początku programu")
    print("[2] Zgłoś błąd na GitHub")
    print("[3] Wyjdź z programu")
    choice = input("Wybierz opcję: ")

    if choice == '1':
        subprocess.run(['clear'])
        main()
    elif choice == '2':
        subprocess.run(['clear'])
        print("Błąd zgłoszony na GitHub.")
        github_url = "https://github.com/Pawelv5/NexusClient/issues/new"
        webbrowser.open(github_url)
        sys.exit(0)
    elif choice == '3':
        subprocess.run(['clear'])
        print("Wyjście z programu.")
        sys.exit(0)
    else:
        print("Niepoprawny wybór.")
        handle_error(download, error)

def main():
    try:
        subprocess.run(['clear'])
        print(logo)
        print("Witaj w instalatorze NexusTerminal!\n")
        print("[1] Pobierz/zaaktualizuj klienta NexusTerminal")
        print("[2] Wyjdź z programu")

        choice = input("Wybierz opcję: ")

        if choice == '1':
            print("Pobieranie/aktualizowanie klienta NexusTerminal...")
            print("Proszę czekać...")
            print("Proszę nie zamykać programu.")

            # Adres URL repozytorium
            repo_url = "https://github.com/Pawelv5/NexusClient/archive/main.zip"

            # Nazwa pliku, który zostanie pobrany
            zip_file_name = "nexus.zip"

            # Pobieranie pliku ZIP
            download = True
            response = requests.get(repo_url)
            with open(zip_file_name, "wb") as file:
                file.write(response.content)

            # Rozpakowywanie pliku ZIP
            import zipfile

            with zipfile.ZipFile(zip_file_name, "r") as zip_ref:
                zip_ref.extractall()

            # Przenoszenie plików .py do bieżącego folderu
            import shutil

            folder_name = "NexusClient-main"  # Nazwa folderu wypakowanego z pliku ZIP

            for root, dirs, files in os.walk(folder_name):
                for file in files:
                    if file != "nexus.py" and file.endswith(".py"):
                        shutil.move(os.path.join(root, file), file)

            # Usuwanie niepotrzebnych plików i folderów
            os.remove(zip_file_name)
            shutil.rmtree(folder_name)

            # Uruchamianie skryptu nexus.py
            subprocess.run(["python", "nexus.py"])

        elif choice == '2':
            subprocess.run(['clear'])
            print("Anulowano instalację.")
            sys.exit(0)
        else:
            print("Niepoprawny wybór.")
            handle_error(download=False, error="Niepoprawny wybór.")

    except Exception as error:
        handle_error(download=True, error=error)

if __name__ == '__main__':
    main()

