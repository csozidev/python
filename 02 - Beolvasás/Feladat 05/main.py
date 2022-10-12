band: str = None
music: str = None
lenght: str = None

from os import system

band = str(input("Kérem adja meg a kedvenc együttesének nevét: "))
music = str(input("Adja meg a kedvenc számának címét: "))
lenght = str(input("Adja meg ennek a számnak a hosszát"))

system('cls')

print(f"Az ön kedven együttesének {band} a legjobb zeneszáma {music} melynek hossza {lenght} perc")