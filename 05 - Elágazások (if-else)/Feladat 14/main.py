from os import system

x: int = None
y: int = None
z: int = None
maradeky: int= None
maradekz: int = None

print("Kérem az első számot: (X)")
x = int(input(""))
print("Kérem a második számot: (Y)")
y = int(input(""))
print("Kérem a harmadik számot: (Z)")
z = int(input(""))

maradeky= x % y
maradekz= x % z

system('cls')

if(maradeky == 0 and maradekz == 0):
    print("X osztható a másik kettő számmal")
elif(maradeky == 0 and maradekz != 0):
    print("X osztható y-nal")
elif(maradeky != 0 and maradekz == 0):
    print("X osztható Z-vel")
else:
    print("Nem oszható semelyik számmal sem")

