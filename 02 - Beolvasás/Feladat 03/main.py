name: str = None
height: float = None

from os import system

name = str(input("Kérem adja meg a teljes nevét: "))
height = float(input("Kérem adja meg a magasságát (m): "))

system('cls')

print(f"{name} az Ön magassága {height}m")