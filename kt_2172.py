import math

def loendid_17_2(a, b, n):
    x_loend = []
    y_loend = []
    h = (b - a) / (n - 1)
    for i in range(n):
        x = round(a + i * h, 2)
        if x < -3:
            y = (4 - x) / (x + 3) + 2 * math.pi
        elif -3 <= x <= 3:
            y = math.prod([x - 3, x + 3])
        else:
            y = x ** 2 + x - 7.5
        x_loend.append(x)
        y_loend.append(round(y, 2))
    return x_loend, y_loend

def karakteristikud_17_2(y_loend):
    positiivsed = [y for y in y_loend if y > 0]
    if len(positiivsed) == 0:
        print("Kõik funktsiooni väärtused on negatiivsed")
    else:
        print("Funktsiooni positiivsete väärtuste arv on", len(positiivsed))

def peaprogramm():
    a = float(input("Sisesta vahemiku algus => "))
    b = float(input("Sisesta vahemiku lõpp => "))

    if a >= b:
        print("Viga: algus peab olema väiksem kui lõpp!")
        return

    n = int(input("Sisesta jaotiste arv => "))

    x_loend, y_loend = loendid_17_2(a, b, n)

    print("Funktsiooni argumentide ja väärtuste tabel")
    for x, y in zip(x_loend, y_loend):
        print(f"{x}\t{y}")

    karakteristikud_17_2(y_loend)

peaprogramm()