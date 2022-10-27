from os import system
import sys

num: int = None
maradek1: int = None
maradek2: int = None

print("Kérem a számot:")
num = int(input(""))

system('cls')

maradek1 = num % 4
maradek2 = num % 6

if(maradek1 == 0):
    if (maradek2 == 0):
        print("A szám osztható 4-el és 6-tal is")
    else:
        print("A szám csak 4-el osztható")
else:
    if (maradek2 == 0):
        print("A szám csak 6-tal osztható")
    else:
        print("A szám sem 4-el sem 6-tal nem osztható")