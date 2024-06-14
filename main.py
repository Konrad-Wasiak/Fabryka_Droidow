import sys
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


def wyswietl_stan_magazynu(batchy):
    if batchy:
        for batch in batchy:
            print(
                f"Nazwa: {batch.nazwa}, Ilość droidów: {batch.ilosc_droidow}, Kolor: {batch.kolor}, Umiejętności: {batch.umiejetnosci_specjalne}, Wersja oprogramowania: {batch.wersja_oprogramowania}")
    else:
        print("Magazyn jest pusty.")


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
                wyswietl_stan_magazynu(batchy)
            elif wybor == '7':
                print("Dziękujemy za skorzystanie z aplikacji. Do widzenia!")
                sys.exit()
            else:
                print("Nieprawidłowy wybór, spróbuj ponownie.")
        except:
            continue


if __name__ == "__main__":
    main()
