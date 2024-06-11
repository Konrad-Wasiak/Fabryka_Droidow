from typing import List

class Batch:
    def __init__(self, nazwa: str, numer_produkcji: int, ilosc_droidow: int, umiejetnosci_specjalne: List[str], wersja_oprogramowania: str, rodzaj_klasy: str, kolor: str):
        self.nazwa: str = f"{nazwa}_{numer_produkcji}"
        self.ilosc_droidow: int = ilosc_droidow
        self.umiejetnosci_specjalne: List[str] = umiejetnosci_specjalne
        self.wersja_oprogramowania: str = wersja_oprogramowania
        self.rodzaj_klasy: str = rodzaj_klasy
        self.kolor: str = kolor