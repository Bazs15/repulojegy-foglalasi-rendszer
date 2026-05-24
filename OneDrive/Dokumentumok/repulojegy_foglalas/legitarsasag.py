from foglalas import JegyFoglalas

class LegiTarsasag:

    def __init__(self, nev):

        self.__nev = nev

        self.__jaratok = []

        self.__foglalasok = []

    def jarat_hozzaadas(self, jarat):

        self.__jaratok.append(jarat)

    def foglalas(self, utas_nev, jaratszam, datum):

        jarat = None

        for j in self.__jaratok:

            if j.get_jaratszam() == jaratszam:

                jarat = j

                break

        if jarat is None:

            raise ValueError("Nincs ilyen járat!")

        uj_foglalas = JegyFoglalas(utas_nev, jarat, datum)

        self.__foglalasok.append(uj_foglalas)

        return jarat.get_jegyar()

    def foglalas_lemondasa(self, utas_nev, jaratszam):

        for foglalas in self.__foglalasok:

            if (

                foglalas.get_utas_nev() == utas_nev

                and foglalas.get_jarat().get_jaratszam() == jaratszam

            ):

                self.__foglalasok.remove(foglalas)

                return True

        raise ValueError("A foglalás nem található!")

    def foglalasok_listazasa(self):

        if len(self.__foglalasok) == 0:

            print("Nincs foglalás!")

        for foglalas in self.__foglalasok:

            print(foglalas)

    def jaratok_listazasa(self):

        for jarat in self.__jaratok:

            print(jarat)