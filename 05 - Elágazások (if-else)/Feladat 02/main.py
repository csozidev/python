from os import system

number: int = None

print("Kérem a számot")
number = int(input(""))

system('cls')

if (number >= 0):
    print("Pozitív")
else:
    print("Negatív")