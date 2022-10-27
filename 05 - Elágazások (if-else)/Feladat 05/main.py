from os import system

x: int = None
y: int = None

print("Kérem az első számot:")
x = int(input(""))
print("Kérem a második számot:")
y = int(input(""))

system('cls')

if (x > y):
    print(f"{y}, {x}")
else:
    print(f"{x}, {y}")