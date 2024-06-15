import pandas as pd
from datetime import datetime


# Funkcja logująca
def log_message(message):
    log_file = 'log.csv'

    # Pobierz aktualną datę i czas
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Zapytaj użytkownika, czy chce użyć aktualnego czasu, czy wprowadzić własny
    while True:
        use_current_time = input("Generowanie logu:\nCzy chcesz użyć aktualnego czasu? (tak/nie): ").strip().lower()
        if use_current_time in ['tak', 'nie']:
            break
        else:
            print("Proszę odpowiedzieć 'tak' lub 'nie'.")

    if use_current_time == 'nie':
        while True:
            user_time = input("Wprowadź czas w formacie YYYY-MM-DD HH:MM:SS: ").strip()
            try:
                # Sprawdź czy czas jest w poprawnym formacie
                datetime.strptime(user_time, '%Y-%m-%d %H:%M:%S')
                break
            except ValueError:
                print("Niepoprawny format czasu. Spróbuj ponownie.")
    else:
        user_time = now

    # Stwórz DataFrame z nowym wpisem
    new_log = pd.DataFrame([[user_time, message]], columns=['Time', 'Message'])

    try:
        # Wczytaj istniejący plik logu, jeśli istnieje
        existing_log = pd.read_csv(log_file)
        # Dodaj nowy wpis do istniejącego logu
        updated_log = pd.concat([existing_log, new_log], ignore_index=True)
    except FileNotFoundError:
        # Jeśli plik nie istnieje, stwórz nowy
        updated_log = new_log

    # Sortuj logi chronologicznie
    updated_log = updated_log.sort_values(by='Time')

    # Zapisz log do pliku CSV
    updated_log.to_csv(log_file, index=False)
    print("Log został zaktualizowany.")