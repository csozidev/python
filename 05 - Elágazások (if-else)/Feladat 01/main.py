from os import system

number: int = None

print("Kérem a számot:")
number = int(input(""))

system('cls')

if (number > 0):
    print("A szám nagyobb mint 0")
elif (number == 0):
    print("A szám egyenlő a 0-val")
else: 
    print("A szám kissebb mint 0")

