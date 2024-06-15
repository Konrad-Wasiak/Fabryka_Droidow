import sys
import pandas as pd
from batch import Batch
from log import log_message

def wyswietl_menu():
    print("Wybierz opcję:")
    print("1. Dodanie nowego batcha")
    print("2. Pomalowanie batcha")
    print("3. Szkolenie batcha")
    print("4. Wyświetlenie logu")
    print("5. Dodanie czegoś do logu")
    print("6. Wyświetlenie stanu magazynu")
    print("7. Wyjście z aplikacji")


def dodaj_nowy_batch(batchy):
    nowy_batch = Batch.stworz_nowy_batch()
    batchy.append(nowy_batch)
    print(f"Utworzono nowy batch: {nowy_batch.nazwa}")


def maluj_batch(batchy):
    nazwa = input("Podaj nazwę batcha do pomalowania: ")
    kolor = input("Podaj nowy kolor: ")
    for batch in batchy:
        if batch.nazwa == nazwa:
            batch.maluj_droidy(kolor)
            break
    else:
        print(f"Batch o nazwie {nazwa} nie został znaleziony.")


def szkol_batch(batchy):
    nazwa = input("Podaj nazwę batcha do szkolenia: ")
    umiejetnosc = input("Podaj nową umiejętność: ")
    for batch in batchy:
        if batch.nazwa == nazwa:
            batch.szkol_droidy(umiejetnosc)
            break
    else:
        print(f"Batch o nazwie {nazwa} nie został znaleziony.")


def wyswietl_log():
    try:
        with open('log.csv', 'r') as file:
            print(file.read())
    except FileNotFoundError:
        print("Plik logu nie został znaleziony.")


def dodaj_do_logu():
    wiadomosc = input("Podaj wiadomość do dodania do logu: ")
    log_message(wiadomosc)
    print("Wiadomość została dodana do logu.")



def pokaz_magazyn():
    batchy = Batch.wczytaj_z_csv()
    if not batchy:
        print("Brak batchy w magazynie.")
        return
    data = {
        "Nazwa": [batch.nazwa for batch in batchy],
        "Ilość droidów": [batch.ilosc_droidow for batch in batchy],
        "Umiejętności specjalne": [", ".join(batch.umiejetnosci_specjalne) for batch in batchy],
        "Wersja oprogramowania": [batch.wersja_oprogramowania for batch in batchy],
        "Rodzaj klasy": [batch.rodzaj_klasy for batch in batchy],
        "Kolor": [batch.kolor for batch in batchy]
    }
    df = pd.DataFrame(data)
    df.to_csv('batche.csv', index=False)
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    print(df)

def main():
    batchy = []
    while True:
        wyswietl_menu()
        wybor = input("Wybierz opcję (1-7): ")

        try:
            if wybor == '1':
                dodaj_nowy_batch(batchy)
            elif wybor == '2':
                maluj_batch(batchy)
            elif wybor == '3':
                szkol_batch(batchy)
            elif wybor == '4':
                wyswietl_log()
            elif wybor == '5':
                dodaj_do_logu()
            elif wybor == '6':
                pokaz_magazyn()
            elif wybor == '7':
                print("Dziękujemy za skorzystanie z aplikacji. Do widzenia!")
                sys.exit()
            else:
                print("Nieprawidłowy wybór, spróbuj ponownie.")
        except (ValueError, IndexError, AttributeError):
            continue


if __name__ == "__main__":
    main()