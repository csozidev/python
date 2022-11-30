from os import system
import math

print("Téglalap hossza: ")
a = int(input(""))
print("Téglalap szélessége: ")
b = int(input(""))
print("Kiszámolandó: (t/k/a)")
algorithm = str(input(""))

system('cls')

match algorithm:
  case "t":
    i = a * b
    print(f"A téglalap területe: {i}")
  case "k":
    i = a + a + b + b
    print(f"A téglalap kerülete: {i}")
  case "a":
    i = math.sqrt( math.pow(a, 2) + math.pow(a, 2))
    print(f"A téglalap átlója: {i}")
  case _:
    print("Érvénytelen")
  