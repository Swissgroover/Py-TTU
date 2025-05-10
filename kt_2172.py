import math

def Y(x):
    if x < -3:
        return (4-x)/(x+3) + 2*math.pi/5
    elif -3 <= x <= 3:
        return math.pi * math.sin(x**2 - x - 3)
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
            x_str = f"{x:.2f}"
            y_str = f"{y:.2f}"
            
            if x_str.endswith('0'):
                if x_str.endswith('00'):
                    x_str = x_str[:-3] 
                else:
                    x_str = x_str[:-1]  
                    
            if y_str.endswith('0'):
                if y_str.endswith('00'):
                    y_str = y_str[:-3] 
                else:
                    y_str = y_str[:-1] 
            
            print(f"{x_str}    {y_str}")
        
        karakteristikud_17_2y_loend(results)
        
    except ValueError as e:
        print(f"Viga: {e}")

if __name__ == "__main__":
    peaprogramm()
