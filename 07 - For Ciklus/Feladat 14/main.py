min = int(input("Kérem az első számot (min)"))
max = int(input("Kérem a második számot (max)"))
ot: int = 0
het: int = 0

for i in range(min, max, 1):
    if i%5 == 0:
        ot = ot + i
    elif i%7 == 0:
        het = het + i
if ot > het:
    print("Az öttel osztható számok összege nagyobb")
elif het > ot:
    print("A héttel osztható számok összege nagyobb")
else:
    print("Ugyan annyi a héttel osztható számok és az ttel osztható számok összege")