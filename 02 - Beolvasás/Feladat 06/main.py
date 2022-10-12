movie: str = None
year: int = None
producer: str = None
maincharacter: str = None

from os import system

print("Adja meg a kedvenc filmét: ")
movie = str(input(""))
print("Annak megjelenési évét: ")
year = int(input(""))
print("Rendező nevét: ")
producer = str(input(""))
print("Főszereplő nevét: ")
maincharacter = str(input(""))

system('cls')

print(f" {year}-ban {producer} rendezésében megjelent a/az {movie} című film {maincharacter} főszereplésével!")