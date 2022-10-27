from os import system
import sys

num: int = None
maradek1: int = None
maradek2: int = None

print("Kérem a számot:")
num = int(input(""))

system('cls')

maradek1 = num % 2
maradek2 = num % 3

if(maradek1 == 0):
    if(maradek2 == 0):
        print("ZIZI")
    else:
        print("BIZ")
else:
    if(maradek2 == 0):
        print("BAZ")
    else:
        print("Nem osztható semmivel sem")
