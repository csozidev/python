name: str = None
height: float = None

from os import system

print("Kérem adja meg a teljes nevét: ")
name = str(input(""))

print("Kérem adja meg a magasságát (m): ")
height = float(input(""))

system('cls')

print(f"{name} az Ön magassága {height}m")