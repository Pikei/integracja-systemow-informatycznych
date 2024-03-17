import random
import csv
from bs4 import BeautifulSoup
import requests

from Lab2.Cat import Cat
from Lab2.Dog import Dog
from Lab2.Fox import Fox


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
            print("6. House offers")


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

