import random
import csv
from bs4 import BeautifulSoup
import requests
import re

from Lab2.Cat import Cat
from Lab2.Dog import Dog
from Lab2.Fox import Fox
from Lab2.Home import Home


def start():
    print("Choose option")
    print("1. Class inheritance")
    print("2. Longest word in file")
    print("3. Password generator")
    print("4. IP Addresses")
    print("5. Save URL")
    print("6. House offers")

    match input("Choose option: "):
        case "1":
            classInheritance()
        case "2":
            longestWord()
        case "3":
            passwordGenerator()
        case "4":
            ipAddresses()
        case "5":
            urls()
        case "6":
            homeOffers()


def classInheritance():
    name = input("Name your dog: ")
    age = input("How old is your Dog?: ")
    sex = input("What gender is your dog? (m/f): ")
    breed = input("Does your dog can breed? (t/f): ")
    dog = Dog(name, age, sex, breed)

    name = input("Name your cat: ")
    age = input("How old is your cat?: ")
    sex = input("What gender is your cat? (m/f): ")
    breed = input("Does your cat can breed? (t/f): ")
    cat = Cat(name, age, sex, breed)

    name = input("Name your fox: ")
    age = input("How old is your fox?: ")
    sex = input("What gender is your fox? (m/f): ")
    fox = Fox(name, age, sex)

    dog.sound()
    cat.sound()
    fox.sound()

def longestWord():
    with open("Lab2/test.txt") as file:
        data = file.read().replace("\n", " ")
        text = data.split(" ")
        word = text[0]
        for i in range(0, len(text)):
            if len(text[i]) > len(word):
                word = text[i]
    print(f"Longest word in text is: {word} and has length: {len(word)}")


def passwordGenerator():
    lettersUpperCase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lettersLowerCase = "abcdefghijklmnopqrstuvwxyz"
    data = ""
    for i in range(0, 1000):
        password = ""
        for j in range(0, 6):
            match (random.randint(1, 3)):
                case 1:
                    password += lettersUpperCase[random.randint(0, len(lettersUpperCase)-1)]
                case 2:
                    password += lettersLowerCase[random.randint(0, len(lettersLowerCase)-1)]
                case 3:
                    password += str(random.randint(0, 9))
        data += f"{i+1}: {password}\n"
        text_file = open("Lab2/Passwords.txt", "w")
        text_file.write(data)
        text_file.close()


def ipAddresses():
    with open('Lab2/Addresses.csv', 'w', newline='') as csvfile:
        data = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        data.writerow(["pc_name", "ip_address"])
        for i in range(1, 101):
            data.writerow([f"P{i}", f"172.30.2.{str(i)}"])


def urls():
    url = 'https://www.google.com/'
    response = requests.get(url)
    html = response.text

    soup = BeautifulSoup(html, features="html.parser")
    links = soup.find_all('a')
    for link in links:
        print(link)


def homeOffers():
    url = ('https://www.otodom.pl/pl/wyniki/sprzedaz/mieszkanie/pomorskie/gdynia/gdynia/gdynia?priceMax=600000'
           '&viewType=listing')
    headers = {
        'authority': 'www.google.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,/;q=0.8,'
                  'application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'max-age=0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/115.0.0.0'
                      'Safari/537.36',
    }
    response = requests.get(url, headers=headers)
    html = response.text
    soup = BeautifulSoup(html,  features="html.parser")

    end = len(soup.select('p[data-cy="listing-item-title"]'))
    home_offers = {}
    with open('names.csv', 'w', newline='') as csvfile:
         ['first_name', 'last_name']

    with open('Lab2/home.csv', 'w', newline='',  encoding='UTF8') as csvfile:
        fieldnames = ["Number", "Name", "Address", "Price", "Price for square meter", "Apartment area"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for i in range(0, end):
            arr = soup.select('p[data-cy="listing-item-title"]')
            title = arr[i].get_text()
            arr = soup.select('p[data-testid="advert-card-address"]')
            address = arr[i].get_text()
            arr = soup.select("span.ev8qziy1.css-2ih7x0.e1a3ad6s0")
            temp = str(arr[i].get_text())
            price = temp.replace(u'\xa0', u" ")
            arr = soup.select("dl.css-uki0wd.e12r8p6s1 dd")
            price_for_m2 = ""
            m2 = ""
            for j in range(0, len(arr)):
                temp = str(arr[j].get_text())
                if temp.__contains__("zł/m²"):
                    temp = temp.replace(u'\xa0', u" ")
                    price_for_m2 = temp
                elif temp.__contains__(" m²"):
                    temp = temp.replace(u'\xa0', u" ")
                    m2 = temp
            home_offers[i+1] = Home(title, address, price, price_for_m2, m2)
            # fieldnames = ["Number", "Name", "Address", "Price", "Price for square meter", "Apartment area"]

            writer.writerow({"Number": str(i+1), "Name": str(title), "Address": str(address), "Price": str(price), "Price for square meter": str(price_for_m2), "Apartment area": str(m2)})
            # data.writerow([f"{i+1}", f"{title}", f"{address}", f"{price}", f"{price_for_m2}", f"{m2}"])
            home_offers[i+1].print_values()








