# Wczytywanie z pliku
plik = open('dane_6_1.txt')
r = plik.readlines()
plik.close()

# Wczytywanie do listy
slowa = []
for i in r:
    slowa.append(i.strip())

# Szyfrowanie słów
szyfr = []
for i in slowa:
    s = ''
    for j in i:
        lit = ord(j)
        for k in range(107):
            lit += 1
            if lit == 91:
                lit = 65
        s += chr(lit)
    szyfr.append(s)

# Wypisywanie slow
for i in szyfr:
    print(i)
