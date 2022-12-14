min = int(input("Kérem az első számot (min)"))
max = int(input("Kérem a második számot (max)"))
paros: int = 0
paratlan: int = 0
avarage: float = 0

for i in range(min, max, 1):
    if (i%2 == 0):
        os = os + i
    else:
        atlan = atlan + i
avarage = (os + atlan)/2
print(f"Az átlaf: {avarage}")