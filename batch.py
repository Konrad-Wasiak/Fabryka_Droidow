from typing import List

class Batch:
    def __init__(self, nazwa: str, numer_produkcji: int, ilosc_droidow: int, umiejetnosci_specjalne: List[str], wersja_oprogramowania: str, rodzaj_klasy: str, kolor: str):
        self.nazwa: str = f"{nazwa}_{numer_produkcji}"
        self.ilosc_droidow: int = ilosc_droidow
        self.umiejetnosci_specjalne: List[str] = umiejetnosci_specjalne
        self.wersja_oprogramowania: str = wersja_oprogramowania
        self.rodzaj_klasy: str = rodzaj_klasy
        self.kolor: str = kolor

    def szkol_droidy(self, nowa_umiejetnosc: str) -> None:
        if nowa_umiejetnosc not in self.umiejetnosci_specjalne:
            self.umiejetnosci_specjalne.append(nowa_umiejetnosc)
            print(f"Umiejętność {nowa_umiejetnosc} została dodana do droidów w batchu {self.nazwa}.")
        else:
            print(f"Umiejętność {nowa_umiejetnosc} już istnieje w batchu {self.nazwa}.")

    def maluj_droidy(self, nowy_kolor: str) -> None:
        self.kolor = nowy_kolor
        print(f"Droidy w batchu {self.nazwa} zostały pomalowane na kolor {nowy_kolor}.")

    def updatuj_software(self, nowa_wersja_oprogramowania: str) -> None:
        self.wersja_oprogramowania = nowa_wersja_oprogramowania
        print(
            f"Wersja oprogramowania droidów w batchu {self.nazwa} została zaktualizowana do {nowa_wersja_oprogramowania}.")