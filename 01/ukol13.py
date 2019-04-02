pocetRukou = int(input('Kolik máš rukou? '))
if pocetRukou >= 10:
    print('Zručnost patří k tvým největším přednostem')
elif pocetRukou >= 5:
    print('Vřele vítáme zástupce z řad hlavonožců.')
elif pocetRukou >= 3:
    print('Nezdvojily se ti některé počty?')
elif pocetRukou >= 2:
    print('A není jich málo Antone Pavloviči?')
elif pocetRukou >= 0:
    print('Nedá se nic dělat, zapoj více nohy.')    
else:
    print('Zkus je přepočítat znovu.')