import os
import requests
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
░▒▓██ Pobierz/zaaktualizuj klienta ██▓▒░
░▒▓██ Instalator NexusTerminal     ██▓▒░
░▒▓██ Wydano przez:   Ephidev 2023 ██▓▒░
░▒▓██████████████████████████████████▓▒░
\033[0m'''

def main():
    print(logo)
    print("Witaj w instalatorze NexusTerminal!")
    print("[1] Rozpocznij instalację")
    print("[2] Anuluj")
    choice = input("Wybierz opcję: ")

    if choice == '1':
        # Adres URL repozytorium
        repo_url = "https://github.com/Pawelv5/NexusClient/archive/main.zip"

        # Nazwa pliku, który zostanie pobrany
        zip_file_name = "nexus.zip"

        # Pobieranie pliku ZIP
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
        print("Anulowano instalację.")
    else:
        print("Niepoprawny wybór.")

if __name__ == '__main__':
    main()

