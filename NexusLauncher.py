
subprocess.run(['clear'])

class Colores:
    green = "\033[32m"  # zmiana koloru na zielony


logo = Colores.green + '''
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
   '''


def check_internet_connection():
    try:
        requests.get('https://api.ipify.org', timeout=5)
        return True
    except requests.ConnectionError:
        return False


def get_ip_info(ip):
    url = f"http://ip-api.com/json/{ip}"
    response = requests.get(url)
    data = response.json()

    print(f"Informacje o adresie IP: {ip}\n")
    print("[~] [Dostawca internetu]:", data.get('isp', '[~] [Brak informacji o dostawcy internetu!]'))
    print("[~] [Organizacja]:", data.get('org', '[~] [Brak informacji o organizacji!]'))
    print("[~] [Miasto]:", data.get('city', '[~] [Brak informacji o mieście!]'))
    print("[~] [Kraj]:", data.get('country', '[~] [Brak informacji o kraju!]'))
    print("[~] [Region]:", data.get('region', '[~] [Brak informacji o regionie!]'))
    print("[~] [Kontynent]:", data.get('continent', '[~] [Brak informacji o kontynencie!]'))
    print("[~] [Region / stan]:", data.get('regionName', '[~] [Brak informacji o regionie / stanie!]'))
    print("[~] [Kod kontynentu (2 litery)]:", data.get('continentCode', '[~] [Brak informacji o kodzie kontynentu!]'))
    print("[~] [Szerokość geograficzna]:", data.get('lat', '[~] [Brak informacji o szerokości geograficznej!]'))
    print("[~] [Długość geograficzna]:", data.get('lon', '[~] [Brak informacji o długości geograficznej!]'))
    print("[~] [Strefa czasowa]:", data.get('timezone', '[~] [Brak informacji o strefie czasowej!]'))
    print("[~] [Kod pocztowy]:", data.get('zip', '[~] [Brak informacji o kodzie pocztowym!]'))
    print("[~] [Numer AS i organizacja]:", data.get('as', '[~] [Brak informacji o numerze AS i organizacji!]'))
    print("[~] [Kod kraju (2 litery)]:", data.get('countryCode', '[~] [Brak informacji o kodzie kraju!]'))
    print("[~] [Odwrócony DNS IP]:", data.get('reverse', '[~] [Brak informacji o odwróconym DNS IP!]'))
    print("[~] [Połączenie mobilne]:", data.get('mobile', '[~] [Brak informacji o połączeniu mobilnym!]'))
    print("[~] [Waluta]:", data.get('currency', '[~] [Brak informacji o walucie!]'))
    print("[~] [Dystrykt (podział miasta)]:", data.get('district', '[~] [Brak informacji o dystrykcie!]'))
    print("[~] [Proxy, VPN lub Tor]:", data.get('proxy', '[~] [Brak informacji o Proxy, VPN lub Tor!]'))


def IPtracker():
    print(logo)
    print("IPtracker")

    while True:
        if not check_internet_connection():
            print("Wymagane jest połączenie z internetem do działania tego programu.")
            print("[1] Ponów próbę połączenia")
            print("[2] Powrót do skryptu nexus.py")

            while True:
                choice = input("Wybierz opcję (1 lub 2): ")

                if choice == "1":
                    if check_internet_connection():
                        print("Połączono z internetem.")
                        break
                    else:
                        print("Nie można nawiązać połączenia z internetem. Spróbuj ponownie.")
                elif choice == "2":
                    print("Powrót do skryptu nexus.py.")
                    subprocess.run(['python', 'nexus.py'])
                    return
                else:
                    print("Nieprawidłowy wybór. Spróbuj ponownie.")

        print("Wybierz opcję i poczekaj:")
        print("[1] Sprawdź informacje o swoim adresie IP")
        print("[2] Sprawdź informacje o innym adresie IP")
        print("[3] Wyjdź z programu")

        choice = input("Wybierz opcję (1, 2 lub 3): ")

        if choice == "1":
            ip = requests.get('https://api.ipify.org').text
            get_ip_info(ip)
            input("Naciśnij Enter, aby kontynuować...")
            subprocess.run(['clear'])  # Czyszczenie okna terminala (dla systemu Linux)
            break  # Dodano instrukcję break po wyświetleniu informacji o adresie IP
        elif choice == "2":
            ip = input("Wprowadź adres IP: ")
            get_ip_info(ip)
            input("Naciśnij Enter, aby kontynuować...")
            subprocess.run(['clear'])  # Czyszczenie okna terminala (dla systemu Linux)
            break
        elif choice == "3":
            print("Zamykanie programu.")
            subprocess.run(['clear'])  # Czyszczenie okna terminala (dla systemu Linux)
            subprocess.run(['python', 'nexus.py'])
            break
        else:
            print("Nieprawidłowy wybór. Spróbuj ponownie.")


if __name__ == "__main__":
    IPtracker()

