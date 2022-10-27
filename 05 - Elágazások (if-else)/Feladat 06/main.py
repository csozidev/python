from os import system
import sys

x: int = None
y: int = None
z: int = None

print("Kérem az első számot:")
x = int(input(""))
print("Kérem a második számot:")
y = int(input(""))
print("Kérem a harmadik számot:")
z = int(input(""))

system('cls')

if (x > y and x > z):
    if (y > z):
        print(f"{z}, {y}, {x}")
    else:
        print(f"{y}, {z}, {x}")
elif (y > x and y > z):
    if (x > z):
        print(f"{z}, {x}, {y}")
    else:
        print(f"{z}, {x}, {y}")
else:
    if (y > x):
        print(f"{x}, {y}, {z}")
    else:
        print(f"{y}, {x}, {z}")