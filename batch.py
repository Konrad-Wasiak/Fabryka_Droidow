import csv
from typing import List
from log import log_message

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
            log_message(f"Umiejętność {nowa_umiejetnosc} została dodana do droidów w batchu {self.nazwa}.")
            print(f"Umiejętność {nowa_umiejetnosc} została dodana do droidów w batchu {self.nazwa}.")
        else:
            print(f"Umiejętność {nowa_umiejetnosc} już istnieje w batchu {self.nazwa}.")
            log_message(f"Umiejętność {nowa_umiejetnosc} już istnieje w batchu {self.nazwa}.")

    def maluj_droidy(self, nowy_kolor: str) -> None:
        self.kolor = nowy_kolor
        print(f"Droidy w batchu {self.nazwa} zostały pomalowane na kolor {nowy_kolor}.")
        log_message(f"Droidy w batchu {self.nazwa} zostały pomalowane na kolor {nowy_kolor}.")

    def updatuj_software(self, nowa_wersja_oprogramowania: str) -> None:
        self.wersja_oprogramowania = nowa_wersja_oprogramowania
        print( f"Wersja oprogramowania droidów w batchu {self.nazwa} została zaktualizowana do {nowa_wersja_oprogramowania}.")
        log_message( f"Wersja oprogramowania droidów w batchu {self.nazwa} została zaktualizowana do {nowa_wersja_oprogramowania}.")

    @classmethod
    def stworz_nowy_batch(cls):
        while True:
            try:
                nazwa = input("Podaj nazwę batcha: ")
                if not nazwa.isalnum():
                    raise ValueError("Nazwa batcha powinna składać się z liter i cyfr bez znaków specjalnych.")
                
                numer_produkcji = input("Podaj numer produkcji: ")
                if not numer_produkcji.isdigit():
                    raise ValueError("Numer produkcji powinien być liczbą całkowitą.")
                numer_produkcji = int(numer_produkcji)
                
                ilosc_droidow = input("Podaj ilość droidów: ")
                if not ilosc_droidow.isdigit():
                    raise ValueError("Ilość droidów powinna być liczbą całkowitą.")
                ilosc_droidow = int(ilosc_droidow)
                
                umiejetnosci_specjalne = input("Podaj umiejętności specjalne (oddzielone przecinkami): ").split(',')
                if not all(umiejetnosc.strip().isalpha() for umiejetnosc in umiejetnosci_specjalne):
                    raise ValueError("Umiejętności specjalne powinny być ciągami znaków składającymi się wyłącznie z liter.")
                
                wersja_oprogramowania = input("Podaj wersję oprogramowania: ")
                if not wersja_oprogramowania.isalnum():
                    raise ValueError("Wersja oprogramowania powinna składać się z liter i cyfr bez znaków specjalnych.")
                
                rodzaj_klasy = input("Podaj rodzaj klasy: ")
                if not rodzaj_klasy.isalpha():
                    raise ValueError("Rodzaj klasy powinien składać się z liter bez znaków specjalnych.")
                
                kolor = input("Podaj kolor: ")
                if not kolor.isalpha():
                    raise ValueError("Kolor powinien składać się z liter bez znaków specjalnych.")
                
                nowy_batch = cls(
                    nazwa=nazwa,
                    numer_produkcji=numer_produkcji,
                    ilosc_droidow=ilosc_droidow,
                    umiejetnosci_specjalne=[um.strip() for um in umiejetnosci_specjalne],
                    wersja_oprogramowania=wersja_oprogramowania,
                    rodzaj_klasy=rodzaj_klasy,
                    kolor=kolor
                )
                
                
                cls.zapisz_do_csv(nowy_batch)
                
                print(f"Batch został dodany do bazy danych.")
                log_message(f"Batch został dodany do bazy danych.")

                return nowy_batch
            except ValueError as e:
                print(f"Błąd: {e}. Spróbuj ponownie.")
                log_message(f"Błąd: {e}. Spróbuj ponownie.")

    @staticmethod
    def zapisz_do_csv(batch):
        with open('batche.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([
                batch.nazwa,
                batch.ilosc_droidow,
                ','.join(batch.umiejetnosci_specjalne),
                batch.wersja_oprogramowania,
                batch.rodzaj_klasy,
                batch.kolor
            ])
        print(f"Zapisano batch {batch.nazwa} do pliku CSV.")
        log_message(f"Zapisano batch {batch.nazwa} do pliku CSV.")

    @staticmethod
    def wczytaj_z_csv():
        batchy = []
        try:
            with open('batche.csv', mode='r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if len(row) != 6:
                        print(f"Niepoprawny wiersz w pliku CSV: {row}")
                        log_message(f"Niepoprawny wiersz w pliku CSV: {row}")
                        continue
                    nazwa, ilosc_droidow, umiejetnosci_specjalne, wersja_oprogramowania, rodzaj_klasy, kolor = row
                    try:
                        numer_produkcji = int(nazwa.split('_')[1])
                        ilosc_droidow = int(ilosc_droidow)
                        umiejetnosci_specjalne = umiejetnosci_specjalne.split(',')
                        batch = Batch(
                            nazwa=nazwa.split('_')[0],
                            numer_produkcji=numer_produkcji,
                            ilosc_droidow=ilosc_droidow,
                            umiejetnosci_specjalne=[um.strip() for um in umiejetnosci_specjalne],
                            wersja_oprogramowania=wersja_oprogramowania,
                            rodzaj_klasy=rodzaj_klasy,
                            kolor=kolor
                        )
                        batchy.append(batch)
                    except ValueError as e:
                        print(f"Błąd podczas przetwarzania wiersza: {row}. Błąd: {e}")
                        log_message(f"Błąd podczas przetwarzania wiersza: {row}. Błąd: {e}")
        except FileNotFoundError:
            print("Plik batche.csv nie został znaleziony. Zostanie utworzony nowy plik przy pierwszym zapisie.")
            log_message("Plik batche.csv nie został znaleziony. Zostanie utworzony nowy plik przy pierwszym zapisie.")
        print(f"Wczytano {len(batchy)} batchy z pliku CSV.")
        log_message(f"Wczytano {len(batchy)} batchy z pliku CSV.")
        return batchy

# Przykład użycia:
if __name__ == "__main__":
    batchy = Batch.wczytaj_z_csv()
    print(f"Wczytano batchy: {len(batchy)}")
    for batch in batchy:
        log_message(f"Batch: {batch.nazwa}, ilość droidów: {batch.ilosc_droidow}, umiejętności: {', '.join(batch.umiejetnosci_specjalne)}, wersja oprogramowania: {batch.wersja_oprogramowania}, rodzaj klasy: {batch.rodzaj_klasy}, kolor: {batch.kolor}")
        print(f"Batch: {batch.nazwa}, ilość droidów: {batch.ilosc_droidow}, umiejętności: {', '.join(batch.umiejetnosci_specjalne)}, wersja oprogramowania: {batch.wersja_oprogramowania}, rodzaj klasy: {batch.rodzaj_klasy}, kolor: {batch.kolor}")
    
    nowy_batch = Batch.stworz_nowy_batch()
    print(f"Utworzono batch: {nowy_batch.nazwa}, ilość droidów: {nowy_batch.ilosc_droidow}, umiejętności: {', '.join(nowy_batch.umiejetnosci_specjalne)}, wersja oprogramowania: {nowy_batch.wersja_oprogramowania}, rodzaj klasy: {nowy_batch.rodzaj_klasy}, kolor: {nowy_batch.kolor}")
    log_message(f"Utworzono batch: {nowy_batch.nazwa}, ilość droidów: {nowy_batch.ilosc_droidow}, umiejętności: {', '.join(nowy_batch.umiejetnosci_specjalne)}, wersja oprogramowania: {nowy_batch.wersja_oprogramowania}, rodzaj klasy: {nowy_batch.rodzaj_klasy}, kolor: {nowy_batch.kolor}")

