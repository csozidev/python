from os import system

x: int = None
maradek2: int = None
maradek5: int = None

print("Kérem a számot:")
x = int(input(""))

maradek2 = x % 2
maradek5 = x % 5

system('cls')

if(maradek2 == 0):
    print("Osztható 2-vel: IGAZ")
else:
    print("Osztható 2-vel: HAMIS")

if(maradek5 == 0):
    print("Osztható 5-tel: IGAZ")
else:
    print("Osztható 5-tel: HAMIS")


if(x >= 0):
    print("Pozitív")
else:
    print("Negatív")