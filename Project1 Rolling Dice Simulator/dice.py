import random


x = "y"
while x == "y":
    print("======= ** Rolling Dice Simulator ** =======")
    number = random.randint(1,6)
    print("Numeber is : ",number)
    if number == 1 :
        print("--------")
        print("|      |")
        print("|  0   |")
        print("|      |")
        print("--------")

    if number == 2 :
        print("--------")
        print("|      |")
        print("|  0   |")
        print("|  0   |")
        print("--------")

    if number == 3 :
        print("--------")
        print("|  0   |")
        print("|  0   |")
        print("|  0   |")
        print("--------")

    if number == 4 :
        print("--------")
        print("|0    0|")
        print("|      |")
        print("|0    0|")
        print("--------")

    if number == 5 :
        print("--------")
        print("|0    0|")
        print("|  0   |")
        print("|0    0|")
        print("--------")
    if number == 6 :
        print("--------")
        print("|0    0|")
        print("|0    0|")
        print("|0    0|")
        print("--------")

    x = input("Press -y- to roll it again or -n- to exit \n :- ")
