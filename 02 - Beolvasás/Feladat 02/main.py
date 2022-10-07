name: str = None
bday: str = None

from http.client import BAD_GATEWAY
from importlib import import_module
from os import system

name = str(input("Kérem adja meg a teljes nevét: "))
bday = str(input("Kérem adja meg a születési dátumát: "))

system('cls')

print(f"{name} Ön {bday} született")