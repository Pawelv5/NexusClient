#!/usr/bin/python3
# -*- coding: utf-8 -*-

import requests
import subprocess

subprocess.run(['clear'])

class Colors:
    green = "\033[32m"  # change color to green


logo = Colors.green + '''
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
   ░░░░░░░░░░░╔╦╦═╦═╦═╦╦═╦╗░░░░░░░░░░░
   ░░░░░░░░░░░║║╠═╣╩╬═╣║░║║░░░░░░░░░░░
   ░░░░░░░░░░░║║║║║╦╣║║║╔╝║░░░░░░░░░░░
   ░░░░░░░░░░░║╚╩╩╩╝╚═╩╩╝.║░░░░░░░░░░░
   ░░░░░░░░░░░╚═══════════╝░░░░░░░░░░░
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

    print(f"Information about IP address: {ip}\n")
    print("[~] [Internet Service Provider]:", data.get('isp', '[~] [No information about ISP!]'))
    print("[~] [Organization]:", data.get('org', '[~] [No information about organization!]'))
    print("[~] [City]:", data.get('city', '[~] [No information about city!]'))
    print("[~] [Country]:", data.get('country', '[~] [No information about country!]'))
    print("[~] [Region]:", data.get('region', '[~] [No information about region!]'))
    print("[~] [Continent]:", data.get('continent', '[~] [No information about continent!]'))
    print("[~] [Region / State]:", data.get('regionName', '[~] [No information about region / state!]'))
    print("[~] [Continent Code (2 letters)]:", data.get('continentCode', '[~] [No information about continent code!]'))
    print("[~] [Geographical Latitude]:", data.get('lat', '[~] [No information about geographical latitude!]'))
    print("[~] [Geographical Longitude]:", data.get('lon', '[~] [No information about geographical longitude!]'))
    print("[~] [Timezone]:", data.get('timezone', '[~] [No information about timezone!]'))
    print("[~] [Postal Code]:", data.get('zip', '[~] [No information about postal code!]'))
    print("[~] [AS Number and Organization]:", data.get('as', '[~] [No information about AS number and organization!]'))
    print("[~] [Country Code (2 letters)]:", data.get('countryCode', '[~] [No information about country code!]'))
    print("[~] [Reverse DNS IP]:", data.get('reverse', '[~] [No information about reverse DNS IP!]'))
    print("[~] [Mobile Connection]:", data.get('mobile', '[~] [No information about mobile connection!]'))
    print("[~] [Currency]:", data.get('currency', '[~] [No information about currency!]'))
    print("[~] [District (city division)]:", data.get('district', '[~] [No information about district!]'))
    print("[~] [Proxy, VPN or Tor]:", data.get('proxy', '[~] [No information about Proxy, VPN or Tor!]'))


def IPtracker():
    print(logo)
    print("IP Tracker")

    while True:
        if not check_internet_connection():
            print("Internet connection is required to run this program.")
            print("[1] Retry connection")
            print("[2] Go back to nexus.py script")

            while True:
                choice = input("Choose an option (1 or 2): ")

                if choice == "1":
                    if check_internet_connection():
                        print("Connected to the internet.")
                        break
                    else:
                        print("Failed to establish internet connection. Try again.")
                elif choice == "2":
                    print("Going back to nexus.py script.")
                    subprocess.run(['python', 'nexus.py'])
                    return
                else:
                    print("Invalid choice. Try again.")

        print("Choose an option and wait:")
        print("[1] Check information about your IP address")
        print("[2] Check information about another IP address")
        print("[3] Exit the program")

        choice = input("Choose an option (1, 2, or 3): ")

        if choice == "1":
            ip = requests.get('https://api.ipify.org').text
            get_ip_info(ip)
            input("Press Enter to continue...")
            subprocess.run(['clear'])  # Clear the terminal window (for Linux system)
            break  # Added break statement after displaying IP information
        elif choice == "2":
            ip = input("Enter the IP address: ")
            get_ip_info(ip)
            input("Press Enter to continue...")
            subprocess.run(['clear'])  # Clear the terminal window (for Linux system)
            break
        elif choice == "3":
            print("Exiting the program.")
            subprocess.run(['clear'])  # Clear the terminal window (for Linux system)
            subprocess.run(['python', 'Nexus_Client-EN.py'])
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    IPtracker()

