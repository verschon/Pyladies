

strana = float(input("Zadej číslo "))
cislo_je_spravne = strana > 0
if cislo_je_spravne:
    print("Obvod čtverce se stranou", strana, "cm je", strana * 4, "cm")
    print("Obsah čtverce se stranou", strana, "cm je", strana * strana, "cm")
else:
    print("Strana musí být kladná")


