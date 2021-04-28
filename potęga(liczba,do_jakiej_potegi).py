def potega(liczba, do_jakiej_potegi) :
    if do_jakiej_potegi > 0 :
        return potega(liczba, do_jakiej_potegi-1)* liczba
    else:
        return 1

print("Jestem programem, co oblicza potęgi.")
podstawa = int(input("Podaj podstawę potęgowania:"))
wykladnik = int(input("Podaj wykładnik potęgowania:"))

wynik = potega(podstawa, wykladnik)

print(podstawa, "podniesione do", wykladnik, "potęgi to", wynik)
