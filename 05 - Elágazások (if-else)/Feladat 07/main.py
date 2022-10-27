from os import system
import sys

num: int = None
maradek: int = None

print("Kérem a számot:")
num = int(input(""))

system('cls')

maradek = num % 5

if(maradek == 0):
    print("A szám osztható 5-tel")
else:
    print("A szám NEM osztható 5-tel")