from os import system
day: int = None

print("A hét hanyadik napja van?")
day = int(input(""))

system('cls')

match day:
    case 1:
        print("Hétfő")
    case 2:
        print("Kedd")
    case 3:
        print("Szerda")
    case 4:
        print("Csütörtök")
    case 5:
        print("Péntek")
    case 6:
        print("Szombat")
    case 7:
        print("Vasárnap")
    case _:
        print("Nincs ilyen nap")