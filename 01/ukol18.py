print('Odpovídej "ano" nebo "ne".')
stastna_retezec = input('Jsi šťastná? ')
bohata_retezec = input('Jsi bohatá? ')

if stastna_retezec == 'ano':
    if bohata_retezec == 'ano':
        print('Gratuluji!')
    elif bohata_retezec == 'ne':
        print('Zkus míň utrácet.')
    else:
        print('Nerozumím!') 
if stastna_retezec == 'ne':
    if bohata_retezec == 'ano':
        print('Zkus se víc usmívat.')
    elif bohata_retezec == 'ne':
        print('To je mi líto.')
    else:
        print('Nerozumím!')        
