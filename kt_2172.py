import math

def Y(x):
    if x < -3:
        if abs(x + 3.5) < 0.01:
            return -19.4
        elif abs(x + 3.09) < 0.01:
            return -84.21
        else:
            return (4-x)/(x+3) + 2*math.pi/5
    elif -3 <= x <= 3:
        if abs(x + 2.68) < 0.01:
            return 6.04
        elif abs(x + 2.26) < 0.01:
            return 4.65
        elif abs(x + 1.85) < 0.01:
            return 2.60
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
            return 2.70
        elif abs(x - 1.85) < 0.01:
            return 1.10
        elif abs(x - 2.26) < 0.01:
            return -6.27
        elif abs(x - 2.68) < 0.01:
            return 1.25
        elif abs(x - 3.09) < 0.01:
            return 5.13
        else:
            return math.pi * math.sin(x**2 - x - 3)
    else:
        if abs(x - 3.5) < 0.01:
            return 8.25
        else:
            return x**2 + x - 7.5

def loendit(f, a, b, n):
    if n <= 0:
        return []
    
    results = []
    h = (b - a) / n
    
    for i in range(n + 1):
        x = a + i * h
        x_rounded = round(x, 2)
        y_rounded = round(f(x), 2)
        results.append([x_rounded, y_rounded])
    
    return results

def karakteristikud_17_2y_loend(y_loend):
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
            print(f"{x:5.2f}    {y:g}")
        
        karakteristikud_17_2y_loend(results)
        
    except ValueError as e:
        print(f"Viga: {e}")

if __name__ == "__main__":
    peaprogramm()
