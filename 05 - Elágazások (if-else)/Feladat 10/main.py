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

if(maradek1 == 0 and maradek2 == 0):
    print("ZIZI")
elif(maradek1 == 0 and maradek2 != 0):
    print("BIZ")
elif(maradek1 != 0 and maradek2 == 0):
    print("BAZ")
else:
    print("Nem osztható semmivel sem")