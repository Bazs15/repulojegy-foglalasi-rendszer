from abc import ABC

class Jarat(ABC):

    def __init__(self, jaratszam, celallomas, jegyar):

        self.__jaratszam = jaratszam

        self.__celallomas = celallomas

        self.__jegyar = jegyar

#Getterek
    def get_jaratszam(self):

        return self.__jaratszam

    def get_celallomas(self):

        return self.__celallomas

    def get_jegyar(self):

        return self.__jegyar

#Setter
    def set_jegyar(self, uj_ar):

        if uj_ar <= 0:

            raise ValueError("A jegyár nem lehet negatív!")

        self.__jegyar = uj_ar

    def __str__(self):

        return f"{self.__jaratszam} - {self.__celallomas} - {self.__jegyar} Ft"

class BelfoldiJarat(Jarat):

    def __init__(self, jaratszam, celallomas, jegyar):

        super().__init__(jaratszam, celallomas, jegyar)

class NemzetkoziJarat(Jarat):

    def __init__(self, jaratszam, celallomas, jegyar):

        super().__init__(jaratszam, celallomas, jegyar)