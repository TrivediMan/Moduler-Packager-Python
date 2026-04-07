print("JAY SHREE KRISHNA")
import datetime
import time
import random
import uuid
import math
import os

def datetime_operations():
    while True:
        print("\nDatetime and Time Operations:")
        print("1. Display current date and time")
        print("2. Calculate difference between two dates")
        print("3. Format date into custom format")
        print("4. Stopwatch")
        print("5. Countdown Timer")
        print("6. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("Current Date and Time:", datetime.datetime.now())

        elif choice == "2":
            d1 = input("Enter first date (YYYY-MM-DD): ")
            d2 = input("Enter second date (YYYY-MM-DD): ")
            date1 = datetime.datetime.strptime(d1, "%Y-%m-%d")
            date2 = datetime.datetime.strptime(d2, "%Y-%m-%d")
            print("Difference:", abs((date2 - date1).days), "days")

        elif choice == "3":
            d = datetime.datetime.now()
            print("Formatted Date:", d.strftime("%d-%m-%Y %H:%M:%S"))

        elif choice == "4":
            input("Press Enter to start...")
            start = time.time()
            input("Press Enter to stop...")
            end = time.time()
            print("Elapsed Time:", round(end - start, 2), "seconds")

        elif choice == "5":
            sec = int(input("Enter seconds: "))
            for i in range(sec, 0, -1):
                print(i, end=" ", flush=True)
                time.sleep(1)
            print("\nTime's up!")

        elif choice == "6":
            break
        else:
            print("Invalid choice!")


def math_operations():
    while True:
        print("\nMathematical Operations:")
        print("1. Factorial")
        print("2. Compound Interest")
        print("3. Trigonometric (sin, cos, tan)")
        print("4. Area of Circle")
        print("5. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            n = int(input("Enter a number: "))
            print("Factorial:", math.factorial(n))

        elif choice == "2":
            p = float(input("Enter principal: "))
            r = float(input("Enter rate (%): ")) / 100
            t = float(input("Enter time (years): "))
            amount = p * (1 + r) ** t
            print("Compound Interest:", round(amount, 2))

        elif choice == "3":
            angle = math.radians(float(input("Enter angle in degrees: ")))
            print("sin:", round(math.sin(angle), 2))
            print("cos:", round(math.cos(angle), 2))
            print("tan:", round(math.tan(angle), 2))

        elif choice == "4":
            r = float(input("Enter radius: "))
            print("Area of Circle:", math.pi * r * r)

        elif choice == "5":
            break
        else:
            print("Invalid choice!")


def random_operations():
    while True:
        print("\nRandom Data Generation:")
        print("1. Random Number")
        print("2. Random List")
        print("3. Random Password")
        print("4. Random OTP")
        print("5. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("Random Number:", random.randint(1, 100))

        elif choice == "2":
            lst = [random.randint(1, 50) for _ in range(5)]
            print("Random List:", lst)

        elif choice == "3":
            length = int(input("Enter password length: "))
            chars = "abcde!"
            password = "".join(random.choice(chars) for _ in range(length))
            print("Generated Password:", password)

        elif choice == "4":
            otp = "".join(str(random.randint(0, 9)) for _ in range(6))
            print("Your OTP is:", otp)

        elif choice == "5":
            break
        else:
            print("Invalid choice!")


def uuid_generator():
    print("Generated UUID:", uuid.uuid4())


def file_operations():
    while True:
        print("\nFile Operations:")
        print("1. Create File")
        print("2. Write to File")
        print("3. Read File")
        print("4. Append to File")
        print("5. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter file name: ")
            open(name, "w").close()
            print("File created successfully!")

        elif choice == "2":
            name = input("Enter file name: ")
            data = input("Enter text: ")
            with open(name, "w") as f:
                f.write(data)
            print("Data written successfully!")

        elif choice == "3":
            name = input("Enter file name: ")
            if os.path.exists(name):
                with open(name, "r") as f:
                    print("File Content:\n", f.read())
            else:
                print("File not found!")

        elif choice == "4":
            name = input("Enter file name: ")
            data = input("Enter text: ")
            with open(name, "a") as f:
                f.write("\n" + data)
            print("Data appended successfully!")

        elif choice == "5":
            break
        else:
            print("Invalid choice!")


def explore_module():
    module = input("Enter module name: ")
    try:
        mod = __import__(module)
        print("Available Attributes:\n", dir(mod))
    except ImportError:
        print("Module not found!")


def main():
    while True:
        print("\nWelcome to Multi-Utility Toolkit")
        print("1. Datetime and Time Operations")
        print("2. Mathematical Operations")
        print("3. Random Data Generation")
        print("4. Generate UUID")
        print("5. File Operations")
        print("6. Explore Module Attributes")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            datetime_operations()
        elif choice == "2":
            math_operations()
        elif choice == "3":
            random_operations()
        elif choice == "4":
            uuid_generator()
        elif choice == "5":
            file_operations()
        elif choice == "6":
            explore_module()
        elif choice == "7":
            print("Thank you for using the Toolkit!")
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

main()
