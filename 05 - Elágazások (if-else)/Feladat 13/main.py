from os import system

number: int = None

print("Kérem a számot")
number = int(input(""))

system('cls')

if (number > 0 and number <= 9):
    print("Egyjegyű szám")
elif(number >= 10 and number <= 99):
    print("Kétjegyű szám")
elif(number >= 100 and number <= 999):
    print("Háromjegyű szám")
else:
    print("Valamilyen másmilyen szám")