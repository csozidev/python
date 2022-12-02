from os import system

print("Kérem az első ellenállás értékét: ")
r1 = int(input(""))
print("Kérem a második ellenállás értékét:")
r2 = int(input(""))
print("Az ellenállások soros, vagy párhuzamos kapcsoláson vannak? (S/P)")
kotes = str(input("")).lower().strip()

system('cls')

match kotes:
    case "p":
        p = (r1 + r2)/(r1 * r2)
        print(f"Az eredő ellenállás: {p}")
    case "s":
        s = r1 + r2
        print(f"Az eredő ellenállás: {s}")