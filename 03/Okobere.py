from random import randrange
skore = 0
while skore <= 21:
    odpoved = int(input("Chcete rozdat kartu? Ano = 1, Ne = 2: "))
    if odpoved == 1:
        novaKarta = randrange(2, 11)    
        print("Vaše karta má hodnotu", novaKarta)
        skore = skore ++ novaKarta
        print("Vaše skóre je nyní", skore)
    elif odpoved == 2:
        print("Vaše skóre je ", skore)          
        skorePocitace = randrange(18, 22) 
        if skore > skorePocitace:
            print("Vyhrál jsi. Oponent měl:", skorePocitace)
        elif skore == skorePocitace:
            print("Je to plichta")
        else:
            print("Prohrál jsi. Oponent měl:", skorePocitace)
        break
else:
    print("Prohrál jsi") 