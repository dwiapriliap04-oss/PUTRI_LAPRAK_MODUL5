def MaxBilangan(a, b, c, d):
    max_value = a
    if b > max_value:
        max_value = b
    if c > max_value:
        max_value = c
    if d > max_value:
        max_value = d
    return max_value

def main():
    a, b, c, d = map(int, input().split())
    max_value = MaxBilangan(a, b, c, d)
    print("Nilai maksimum dari keempat bilangan tersebut adalah:", max_value)

if __name__ == "__main__":
    main()