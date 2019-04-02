from math import pi
def obsah_elipsy(delka_poloosy_a, delka_poloosy_b):
    return pi*delka_poloosy_a*delka_poloosy_b 

print("Obsah elipsy je: ", obsah_elipsy(3, 5))

def obsah_eliptickeho_valce(delka_poloosy_a, delka_poloosy_b, vyska):
    return obsah_elipsy(delka_poloosy_a, delka_poloosy_b)*vyska

print("Obsah eliptického válce je: ", obsah_eliptickeho_valce(3,5,6))
    