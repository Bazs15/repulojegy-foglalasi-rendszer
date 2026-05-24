from jarat import BelfoldiJarat, NemzetkoziJarat

from legitarsasag import LegiTarsasag

def alap_adatok_betoltese():

    legitarsasag = LegiTarsasag("Python Air")

    # Járatok
    j1 = BelfoldiJarat("B101", "Debrecen", 15000)

    j2 = BelfoldiJarat("B102", "Szeged", 12000)

    j3 = NemzetkoziJarat("N201", "London", 75000)

    legitarsasag.jarat_hozzaadas(j1)

    legitarsasag.jarat_hozzaadas(j2)

    legitarsasag.jarat_hozzaadas(j3)

    # 6 foglalás
    legitarsasag.foglalas("Kiss Péter", "B101", "2026-06-01")

    legitarsasag.foglalas("Nagy Anna", "B101", "2026-06-02")

    legitarsasag.foglalas("Tóth Béla", "B102", "2026-06-03")

    legitarsasag.foglalas("Szabó Éva", "N201", "2026-06-04")

    legitarsasag.foglalas("Kovács János", "N201", "2026-06-05")

    legitarsasag.foglalas("Varga Lili", "B102", "2026-06-06")

    return legitarsasag

def menu():

    legitarsasag = alap_adatok_betoltese()

    while True:

        print("\n===== REPÜLŐJEGY FOGLALÁSI RENDSZER =====")

        print("1 - Járatok listázása")

        print("2 - Jegy foglalása")

        print("3 - Foglalás lemondása")

        print("4 - Foglalások listázása")

        print("0 - Kilépés")

        valasztas = input("Válassz: ")

        try:

            if valasztas == "1":

                legitarsasag.jaratok_listazasa()

            elif valasztas == "2":

                nev = input("Utas neve: ")

                jaratszam = input("Járatszám: ")

                datum = input("Dátum (YYYY-MM-DD): ")

                ar = legitarsasag.foglalas(

                    nev,

                    jaratszam,

                    datum

                )

                print(f"Sikeres foglalás! Ár: {ar} Ft")

            elif valasztas == "3":

                nev = input("Utas neve: ")

                jaratszam = input("Járatszám: ")

                legitarsasag.foglalas_lemondasa(

                    nev,

                    jaratszam

                )

                print("Foglalás sikeresen törölve!")

            elif valasztas == "4":

                legitarsasag.foglalasok_listazasa()

            elif valasztas == "0":

                print("Kilépés...")

                break

            else:

                print("Érvénytelen menüpont!")

        except Exception as hiba:

            print(f"Hiba történt: {hiba}")

menu()