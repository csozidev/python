name: str = None
letter: str = None

from os import system

name = str(input("Kérem adja meg a teljes nevét: "))
letter = str(input("Nyomjon le egy gombot  billentyűzetén: "))

system('cls')

print(f"{name} Ön a/az {letter} gombot nyomta le")
