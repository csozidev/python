from os import system
import sys

x: int = None
y: int = None
maradek: int = None

print("Kérem az első számot:")
x = int(input(""))
print("Kérem a második számot:")
y = int(input(""))

system('cls')

maradek = x % y

if(maradek == 0):
    print("Az első szám osztható a második számmal")
else:
    print("Az első szám NEM osztható a második számma")