k = (input("Zadej klíč: "))
cisla = list(range(1,28))
cisla = [str(x) for x in cisla]
while not k in cisla:
    print("Zadejte do klíče číslo")
    k = (input("Zadej klíč od 1 do 27: "))
else:
    int_k = int(k)
plain_text = input("Zadej text: ")
plain_text = plain_text.lower()
cipher_text = ""
for znak in plain_text:
    i = ord(znak)
    if (i < ord("a")):
        i = 32
    elif (i + int_k > ord("z")):
        i = i + int_k 
        i = i - 26   
    else:
        i = i + int_k
    znak = chr(i)
    cipher_text = cipher_text + znak

print("Šifra:", cipher_text)
