min = int(input("Kérem az első számot (min)"))
max = int(input("Kérem a második számot (max)"))

for i in range(min, max, 1):
    if i%2 == 1:
        print(i)