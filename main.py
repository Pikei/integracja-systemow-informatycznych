import Lab1.menuLab1 as lab1
import Lab2.menuLab2 as lab2
import Lab3.lab3 as lab3
import Lab4.meteo as lab4


def menu():
    print("1. Lab 1")
    print("2. Lab 2")
    print("3. Lab 3")
    print("4. Lab 4")
    match (input("Choose option: ")):
        case "1":
            lab1.start()
        case "2":
            lab2.start()
        case "3":
            lab3.start()
        case "4":
            lab4.meteo()
        case _:
            import time
            print("\nWrong option!\n")
            time.sleep(1)
            menu()


if __name__ == '__main__':
    menu()
