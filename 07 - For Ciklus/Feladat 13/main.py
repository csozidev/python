min = int(input("Kérem az első számot (min)"))
max = int(input("Kérem a második számot (max)"))
atlan: int = 0
os: int = 0

for i in range(min, max, 1):
    if i%2 == 0:
        os = os + i
    else:
        atlan = atlan + i
if os > atlan:
    print("A páros számok összege nagyobb")
elif atlan > os:
    print("A páratlan számok összege nagyobb")
else:
    print("Ugyan annyi a páros és páratlan számok összege")