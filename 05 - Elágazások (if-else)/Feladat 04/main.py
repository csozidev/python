from os import system

x: int = None
y: int = None

print("Kérem az első számot:")
x = int(input(""))
print("Kérem a második számot:")
y = int(input(""))

system('cls')

if (x > y):
    print("Az első szám a nagyobb")
elif (x == y):
    print("A két szám egyenlő")
else:
    print("A második szám a nagyobb")