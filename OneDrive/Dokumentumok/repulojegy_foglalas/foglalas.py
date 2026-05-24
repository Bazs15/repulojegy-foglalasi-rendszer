from datetime import datetime

class JegyFoglalas:

    def __init__(self, utas_nev, jarat, datum):

        self.__utas_nev = utas_nev

        self.__jarat = jarat

        try:

            self.__datum = datetime.strptime(datum, "%Y-%m-%d")

        except ValueError:

            raise ValueError("Hibás dátum formátum! (YYYY-MM-DD)")

    def get_utas_nev(self):

        return self.__utas_nev

    def get_jarat(self):

        return self.__jarat

    def get_datum(self):

        return self.__datum

    def __str__(self):

        return (

            f"Utas: {self.__utas_nev}, "

            f"Járat: {self.__jarat.get_jaratszam()}, "

            f"Célállomás: {self.__jarat.get_celallomas()}, "

            f"Dátum: {self.__datum.date()}"
        )