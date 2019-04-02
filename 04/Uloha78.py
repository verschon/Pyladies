cisla = (input("Zadej své rodné číslo ve formátu:xxxxxx/xxxx: "))
spravny_format_lomitka = cisla[6] == "/"
a = "0123456789"
spravny_format_cisel = cisla[0] in a and cisla[1] in a and cisla[2] in a and cisla[3] in a and cisla[4] in a and cisla[5] in a and cisla[7] in a and cisla[8] in a and cisla[9] in a and cisla[10] in a
# spravny_format_cisel = cisla[0] in "0123456789" and cisla[1] in "0123456789" and cisla[2] in "0123456789" and cisla[3] in "0123456789" and cisla[4] in "0123456789" and cisla[5] in "0123456789" and cisla[7] in "0123456789" and cisla[8] in "0123456789" and cisla[9] in "0123456789" and cisla[10] in "0123456789" 
while spravny_format_lomitka != True or spravny_format_cisel != True:
    print("Rodné číslo není ve správném formátu")
    break
else:
    cislo0 = int(cisla[0])
    cislo1 = int(cisla[1])
    cislo2 = int(cisla[2])
    cislo3 = int(cisla[3])
    cislo4 = int(cisla[4])
    cislo5 = int(cisla[5])
    cislo7 = int(cisla[7])
    cislo8 = int(cisla[8])
    cislo9 = int(cisla[9])
    cislo10 = int(cisla[10])
    while ((cislo0 + cislo2 + cislo4 + cislo7 + cislo9) - (cislo1 + cislo3 + cislo5 + cislo8 + cislo10))%11 != 0:
        print("Rodné číslo není zadáno správně")
        break
    else:
        if cislo2 == 0 or cislo2 == 1:
            print("Jste muž s datem narození: {}{}. {}{}. {}{}".format(cislo4, cislo5, cislo2, cislo3, cislo0, cislo1))
        elif cislo2 == 5 or cislo2 == 6:
            print("Jste žena s datem narození: {}{}. {}{}. {}{}".format(cislo4, cislo5, (cislo2-5), cislo3, cislo0, cislo1))      
        else:
            print("Zkontrolujte správnost třetí čislice")

