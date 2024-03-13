import math
import random

from Lab1 import Dog, functions


def reverse():
    word: str = input("Type here: ")
    word = word[::-1]
    print(word)


def change():
    word: str = input("Type here: ")
    word = word.replace("o", "0")
    word = word.replace("O", "0")
    word = word.replace("e", "3")
    word = word.replace("E", "3")
    word = word.replace("i", "1")
    word = word.replace("I", "1")
    word = word.replace("a", "4")
    word = word.replace("A", "4")
    print(word)


def mod3():
    x: int = 1
    while x <= 50:
        if not x % 3 == 0:
            print(x)
        x += 1


def mod34():
    x: int = 1
    count: int = 0
    while x <= 50:
        if x % 3 == 0 or x % 4 == 0:
            print(x)
            count += 1
        x += 1
    print(f"There are {count} numbers from 1 to 50 that are divisible by 3 or 4")


def mod35():
    arr = []
    x: int = 1
    while x <= 100:
        if x % 3 == 0 or x % 5 == 0:
            arr.append(x)
        x += 1
    for num in arr:
        print(num)
    print(f"There are {len(arr)} numbers from 1 to 100 that are divisible by 3 or 5")

def power(number):
    print(int(math.pow(number, 3)))
def dogs():
    d1 = Dog.Dog("Carlo", 5, "brown")
    d2 = Dog.Dog("Brian", 12, "white")
    name = input("Name your dog: ")
    age: int = int(input("How old is your dog? "))
    coat_color = input("What is your dog coat color? ")
    d3 = Dog.Dog(name, age, coat_color)
    d1.sound()
    d2.sound()
    d3.sound()


def math_functions():
    print("Actions will be performed in order: A (action) B.")
    a = input("Type number A: ")
    b = input("Type number B: ")
    print("Choose action: ")
    print("+ add")
    print("- subtract")
    print("* multiply")
    print("/ divide")
    match input("Your choice: "):
        case "+":
            print(f"{a} + {b} = {functions.add(a, b)}")
        case "-":
            print(f"{a} - {b} = {functions.subtract(a, b)}")
        case "*":
            print(f"{a} * {b} = {functions.multiply(a, b)}")
        case "/":
            print(f"{a} / {b} = {functions.divide(a, b)}")


def palindrome():
    word = input("Type here: ")
    if word == word[::-1]:
        print("Your string is palindrome!")
    else:
        print("Your string is not a palindrome!")


def game():
    print("Lets play a game!")
    print("I Will choose random number from 0 to 100, and you will try to guess it")
    print("If you will guess correctly you win. If not I win.")
    print("Each time if you guess incorrectly i will give you a hint if my number is lower or higher than yours")
    print("You have 5 attempts. Good luck")
    rand = random.randint(0, 100)
    for i in range(0, 5):
        x = int(input("Your guess: "))
        if rand < x:
            print(f"My number is lower than yours. You have {5-i} more attempts")
        elif rand > x:
            print(f"My number is higher than yours. You have {5-i} more attempts")
        else:
            print("You guessed correctly. Congratulations!")
            return
    print(f"Unfortunately you lose. My number was {rand}")


def start():
    print("Choose option")
    print("1. Reverse string")
    print("2. Change letters to numbers")
    print("3. Print numbers from 1 to 50, that aren't divisible by 3")
    print("4. Print numbers from 1 to 50, that are divisible by 3 or 4")
    print("5. Print numbers from 1 to 100, that are divisible by 3 or 5")
    print("6. Print the given number to the third power")
    print("7. Create objects of class Dog")
    print("8. Math functions")
    print("9. Check if given String is a palindrome")
    print("10. Guess the number")

    match input("Choose option: "):
        case "1":
            reverse()
        case "2":
            change()
        case "3":
            mod3()
        case "4":
            mod35()
        case "5":
            mod35()
        case "6":
            x: int = int(input("Type number: "))
            power(x)
        case "7":
            dogs()
        case "8":
            math_functions()
        case "9":
            palindrome()
        case "10":
            game()






