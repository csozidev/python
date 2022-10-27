from os import system

number: int = None

print("Kérem a számot")
number = int(input(""))

system('cls')

if (number >= -30 and number <= 40):
    print("A szám -30 és 40 között van")
else:
    print("A szám nincsen -30 és 40 között")