tah_pocitace = 'kámen'
tah_cloveka = input('kámen, nůžky, nebo papír? ')

if tah_pocitace == tah_cloveka:
    print('Plichta.')
elif tah_pocitace != tah_cloveka and tah_cloveka != 'nůžky': 
    print('Vyhrála jsi!')
elif tah_pocitace != tah_cloveka and tah_cloveka != 'papír':   
    print('Počítač vyhrál.')
else:
    print('Nerozumím.')
