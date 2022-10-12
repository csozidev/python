name: str = None
letter: str = None

from os import system

print("Kérem adja meg a teljes nevét: ")
name = str(input(""))

print("Nyomjon le egy gombot  billentyűzetén: ")
letter = str(input(""))

system('cls')

print(f"{name} Ön a/az {letter} gombot nyomta le")
