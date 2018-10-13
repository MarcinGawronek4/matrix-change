print("Nazwa pliku z macierza:")

sciezka = input()
m = []
n = []
with open(sciezka, "r") as plik:
    linijka = plik.readline()
    linijkaSplit = list(map(int, linijka.split(' ')))
    m.append(linijkaSplit)
    while linijka:
        linijka = plik.readline()
        if linijka == "":
            break
        linijkaSplit = list(map(int, linijka.split(" ")))
        m.append(linijkaSplit)

i = len(m)
j = len(m[0])

if i != j:
    print("Macierz nie jest kwadratowa")
    exit()
else:
    w = 0
    for x in m:
        w += 1
        for b in range(w, j):
            if x[b] != 0:
                print("Macierz nie jest trójkątna dolna")
                exit()


n = [[0]*z + [1] + [0]*(i-z-1) for z in range(i) ]

for a in range(i):
    for b in range(i):
        if b==a:
            if m[a][b] != 1:
                e = m[a][b]
                for f in range(0,i):
                    m[a][f] = (m[a][f])*(1 / e)
                    n[a][f] = (n[a][f]) * (1 / e)

for a in range(i):
    for b in range(i):
        if b != a:
            if m[a][b] != 0:
                e = a
                z = m[a][b]
                for f in range(0,i):
                    m[a][f] = m[b][f]*(-z)+m[a][f]
                    n[a][f] = n[b][f]*(-z)+n[a][f]

print(n)