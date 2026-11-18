def hitung(nilai1, nilai2):
    selisih = nilai1 - nilai2
    if selisih < 0:
        return -selisih
    return selisih

def mutlak(angka):
    if angka < 0:
        return -angka
    return angka

def main():

    inputs = list(map(int, input().split()))
    a = inputs[0]
    c= inputs[1]   
    b = inputs[2]
    d = inputs[3]

    Hasil = hitung(a, b) + hitung(c, d)
    print(mutlak(Hasil))

if __name__ == "__main__":
    main()