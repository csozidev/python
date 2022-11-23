from os import system

print("Előételek:")

print("Zöldségleves [1]:")
print("Húsleves [2]:")
print("Gyümölcsleves [3]:")

print("Melyik előételt fogyasztottad:")
eloetel = int(input(""))

print("Főétel:")

print("Sült csirkecomb [1]:")
print("Sült csirkemell [2]:")
print("Rakott zöldség [3]:")
print("Spagetti [4]:")
print("Pizza [5]:")

print("Melyik főételt fogyasztottad:")
foetel = int(input(""))

print("Köret:")

print("Rizs [1]:")
print("Pároltzöldség [2]:")
print("Gyümölcs [3]:")
print("Sültkrumpli [4]:")
print("Saláta [5]:")
print("Kóla [6]:")

print("Melyik körettel fogyasztottad:")
koret = int(input(""))

if (eloetel == 1 and foetel == 4 and koret == 3 or koret == 5 and foetel != 5 and foetel != 3):
    ertekeles = str("Kiváló")
elif (eloetel == 1 and foetel == 2 and koret != 4 and koret == 1):
    ertekeles = str("Fitnesz menü")
elif (eloetel == 2 and foetel == 1 and koret == 4 or koret == 5 and foetel != 5 and foetel != 3):
    ertekeles = str("Vasárnapi menü")
elif (foetel == 5 or foetel == 4 and koret == 3 or koret == 6 and foetel != 3 and koret != 2):
    ertekeles = str("Napi menü")
else:
    ertekeles = str("Menü nem értékelhető")

system('cls')

print(f"A mai menü értékelése: {ertekeles}")

if(eloetel == 1):
    eloeteltext = str("Zöldségleves")
elif(eloetel == 2):
    eloeteltext = str("Húsleves")
elif(eloetel == 3):
    eloeteltext = str("Gyűmölcsleves")
else:
    eloeteltext = str("Nem értelmezhető")

if(foetel == 1):
    foeteltext = str("Sült csirkecomb")
elif(foetel == 2):
    foeteltext = str("Sült csirkemell")
elif(foetel == 3):
    foeteltext = str("Rakott zöldség")
elif(foetel == 4):
    foeteltext = str("Spagetti")
elif(foetel == 5):
    foeteltext = str("Pizza")
else:
    foeteltext = str("Nem értelmezhető")

if(koret == 1):
    korettext = str("Rizs")
elif(koret == 2):
    korettext = str("Pároltzöldség")
elif(koret == 3):
    korettext = str("Gyümölcs")
elif(koret == 4):
    korettext = str("Sültkrumpli")
elif(koret == 5):
    korettext = str("Saláta")
elif(koret == 6):
    korettext = str("Kóla")
else:
    korettext = str("Nem értelmezhető")



print(f"Előétel: {eloeteltext}\nFőétel: {foeteltext}\nKöret: {korettext}\n")