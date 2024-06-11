class Batch:
    def __init__(self, nazwa, numer_produkcji, ilosc_droidow, umiejetnosci_specjalne, wersja_oprogramowania, rodzaj_klasy, kolor):
        self.nazwa = f"{nazwa}_{numer_produkcji}"
        self.ilosc_droidow = ilosc_droidow
        self.umiejetnosci_specjalne = umiejetnosci_specjalne
        self.wersja_oprogramowania = wersja_oprogramowania
        self.rodzaj_klasy = rodzaj_klasy
        self.kolor = kolor