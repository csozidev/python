name: str = None
bday: str = None

from http.client import BAD_GATEWAY
from importlib import import_module
from os import system

print("Kérem adja meg a teljes nevét: ")
name = str(input(""))

print("Kérem adja meg a születési dátumát: ")
bday = str(input(""))

system('cls')

print(f"{name} Ön {bday} született")