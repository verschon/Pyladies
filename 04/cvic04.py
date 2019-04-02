zaznamy = ['pepa novák', 'Jiří Sládek', 'Ivo navrátil', 'jan Poledník']
spravne = []
spatne = []

for zaznam in zaznamy:
    jmeno, prijmeni = zaznam.split()
    if not jmeno [0].islower() and not prijmeni[0].islower():
        spravne.append(zaznam)
    else:
        spatne.append(zaznam)
print(spravne)
print(spatne)

zaznamy = ['pepa novák', 'Jiří Sládek', 'Ivo navrátil', 'jan Poledník']
spravne_zaznamy = []
spatne_zaznamy = []
opravene_zaznamy = []

for zaznam in zaznamy:
    jmeno, prijmeni = zaznam.split()
    if not jmeno[0].islower() and not prijmeni[0].islower():
        spravne_zaznamy.append(zaznam)     
    elif jmeno[0].islower() or prijmeni[0].islower():
        spatne_zaznamy.append(zaznam) 
        jmeno = jmeno.capitalize()
        prijmeni = prijmeni.capitalize()
        opravene_zaznamy.append(jmeno +" " + prijmeni)

print(spatne_zaznamy)
print(spravne_zaznamy)  
print(opravene_zaznamy)

kosik = {"jablko":"červené","hruška":"zelené","broskev":"oranžová", "banan":"zluty"}
shnily_kosik = {}  
for ovoce, barva in kosik.items():
    shnily_kosik[ovoce] = "hnědo-{}".format(barva)
print(shnily_kosik)
