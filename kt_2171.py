def variant_17_1(f_in, f_out, linn):
    with open(f_in, encoding="cp1257") as f:
        lines = f.readlines()

    inimesed = 0
    palgad = 0

    for line in lines:
        osad = line.strip().split("\t")
        if osad[10].lower() == linn.lower():
            inimesed += 1
            palgad += int(osad[9])

    with open(f_out, "w", encoding="utf-8") as f:
        if inimesed == 0:
            f.write("Andmed puuduvad")
        else:
            kesk_palk = round(palgad / inimesed)
            f.write(f"Failis on {inimesed} inimest, kes elavad linnas {linn} ja nende keskmine palk on {kesk_palk} €.")


def peaprogramm():
    linn = input("Sisesta mingi linn => ")
    variant_17_1("isikud.txt", "vastus.txt", linn)

    with open("vastus.txt", encoding="utf-8") as f:
        print(f.read())

peaprogramm()
