max = int(input("Kérem az első számot (max)"))
min = int(input("Kérem a második sázmot (min)"))

for i in range(max, min, -1):
    if i%2 == 0:
        print(i)