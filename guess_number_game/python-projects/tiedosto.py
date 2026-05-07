from colorama import Fore, Back, Style
import random

# Tulostetaan pelin nimi käyttäjälle
print(Fore.MAGENTA + "Tervetuloa!\n" + Style.RESET_ALL + Fore.BLUE +
      "Tehtävänäsi on arvata luku 1-100 välillä" + Style.RESET_ALL)

# Arvotaan luku 1-100 väliltä
guess = random.randint(1, 100)

# Alustetaan running muuttuja
running = True

# Alustetaan laskuri joka pitää kirjaa arvauksista
counter = 0

# While silmukka pyörii niin kauan kunnes luku arvataan oikein
while running:
    try:
        # Pyydetään käyttäjää arvaamaan luku
        number = int(input("Anna luku:\n"))
        # Kasvatetaan laskuria yhdellä
        counter += 1
        # Jos luku ei ole 1-100 välillä, ilmoitetaan käyttäjälle, että hänen arvaamansa luku ei ole 1-100 välillä
        if number < 1 or number > 100:
            print("Arvaamasi luku ei ole 1-100 välillä")
        # Jos luku on suurempi kuin arvottu luku, tulostetaan liian suuri luku
        elif number > guess:
            print(Back.BLUE + "Liian suuri luku" + Style.RESET_ALL)
        elif number < guess:
            print(Back.RED + "Liian pieni luku" + Style.RESET_ALL)
        # Muussa tapauksessa luku on oikein, lopetetaan silmukka
        elif number == guess:
            print(Back.GREEN + f"Arvasit oikein {counter} arvauksella, luku on {guess}")
            running = False
    except ValueError:
        print("Syötä luku 1-100 välillä")
