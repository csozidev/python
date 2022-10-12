brand: str = None
model: str = None
type: str = None
kobcentiangolul: int = None
year: int = None

from os import system

print("Add meg a kedvenc autód modellét: ")
model = str(input(""))

print("Típusát: ")
type = str(input(""))

print("Köbcentijét: ")
kobcentiangolul = int(input(""))

print("Megjelenési évét: ")
year = int(input(""))

print("Márkáját: ")
brand = str(input(""))

system('cls')

print(f"Márka: {brand} \n Modell: {model} \n Típus: {type} \n Köbcenti: {kobcentiangolul} \n Megjelenési év: {year}")