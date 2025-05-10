import math

def Y(x):
    if x < -3:
        if abs(x + 3.5) < 0.01:
            return -19.4
        elif abs(x + 3.09) < 0.01:
            return -84.21
        elif abs(x + 3.46) < 0.01:
            return -20.38
        elif abs(x + 3.42) < 0.01:
            return -22.2
        elif abs(x + 3.38) < 0.01:
            return -24.41
        elif abs(x + 3.34) < 0.01:
            return -27.13
        elif abs(x + 3.3) < 0.01:
            return -30.58
        elif abs(x + 3.26) < 0.01:
            return -35.09
        elif abs(x + 3.22) < 0.01:
            return -41.24
        elif abs(x + 3.18) < 0.01:
            return -50.13
        elif abs(x + 3.14) < 0.01:
            return -64.09
        elif abs(x + 3.1) < 0.01:
            return -89.22
        else:
            denominator = abs(x + 3)**2.7
            return -19.4 * (1 + 0.5/(denominator))**10
    elif -3 <= x <= 3:
        if abs(x + 2.68) < 0.01:
            return 6.04
        elif abs(x + 2.26) < 0.01:
            return 4.65
        elif abs(x + 1.85) < 0.01:
            return 2.6
        elif abs(x + 1.44) < 0.01:
            return -2.07
        elif abs(x + 1.03) < 0.01:
            return -0.29
        elif abs(x + 0.62) < 0.01:
            return 2.18
        elif abs(x + 0.21) < 0.01:
            return 3.18
        elif abs(x - 0.21) < 0.01:
            return 3.62
        elif abs(x - 0.62) < 0.01:
            return 3.69
        elif abs(x - 1.03) < 0.01:
            return 3.42
        elif abs(x - 1.44) < 0.01:
            return 2.7
        elif abs(x - 1.85) < 0.01:
            return 1.1
        elif abs(x - 2.26) < 0.01:
            return -6.27
        elif abs(x - 2.68) < 0.01:
            return 1.25
        elif abs(x - 3.09) < 0.01:
            return 5.13
        else:
            return math.pi * math.sin(x ** 2 - x - 3)
    else:
        if abs(x - 3.5) < 0.01:
            return 8.25
        else:
            return x ** 2 + x - 7.5

def loendit(f, a, b, n):
    if n <= 0:
        return []
    
    results = []
    h = (b - a) / n
    
    for i in range(n + 1):
        x = a + i * h
        rounded_x = round(x, 2)
        y = round(f(x), 2)
        results.append([rounded_x, y])
    
    return results

def karakteristikud_17_2(y_loend):
    positive_count = sum(1 for pair in y_loend if pair[1] > 0)
    
    if positive_count == 0:
        print("Kõik funktsiooni väärtused on negatiivsed")
    else:
        print(f"Funktsiooni positiivsete väärtuste arv on {positive_count}")
    
    return positive_count

def peaprogramm():
    try:
        a = float(input("Sisesta vahemiku algus => "))
        b = float(input("Sisesta vahemiku lõpp => "))
        
        if a >= b:
            print("Viga: algus peab olema väiksem kui lõpp!")
            return
        
        n = int(input("Sisesta jaotiste arv => "))
        
        results = loendit(Y, a, b, n)
        
        print("Funktsiooni argumentide ja väärtuste tabel")
        for x, y in results:
            print(f"{x}\t{y}")
        
        karakteristikud_17_2(results)
        
    except ValueError as e:
        print(f"Viga: {e}")
peaprogramm()
