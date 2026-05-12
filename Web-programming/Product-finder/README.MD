# Description / Kuvaus
## English
A lightweight web app for searching products from a JSON warehouse dataset.
The JSON dataset used in this project was generated with AI (Microsoft Copilot) specifically for this exercise.

## Suomi
Kevyt web‑sovellus, joka hakee tuotteita varaston JSON‑datasta ja näyttää ne taulukossa.
Hakutoiminto tukee sekä normaalia hakua että osittaishakua %‑merkillä.

Tässä projektissa käytetty JSON‑data on generoitu tekoälyllä (Microsoft Copilot) tätä harjoitusta varten.

## Features / Ominaisuudet
### English
- Search by product name
- Partial search with % (e.g. %kaapeli)
- Sorting A–Z / Z–A
- JSON data loading
### Suomi
- Haku tuotteen nimellä
- Osittaishaku %‑merkillä
- Lajittelu A–Z / Z–A
- JSON‑datan lataus

## Search Logic / Hakulogiikka
### English
The search bar supports two modes:

Normal search:  
Matches products whose names start with the typed text.
Example: typing co matches coffee, cookies, etc.

Partial search using %:  
If the search term starts with %, the program performs a substring search.
Example: %milk matches almond milk, milk chocolate, etc.

### Suomi
Hakukenttä tukee kahta hakutapaa:

Normaali haku:  
Etsii tuotteita, joiden nimi alkaa kirjoitetulla tekstillä.
Esim. co löytää coffee, cookies jne.

Osittaishaku %‑merkillä:  
Jos hakutermi alkaa %‑merkillä, tehdään osahaku.
Esim. %milk löytää almond milk, milk chocolate jne.

## Preview / Esikatselu
## Normal search
![Normal search](preview1.png)

### Partial search (%)
![Partial search](preview2.png)

## Sorting/Lajittelu
### English

You can sort products using the select menu: A–Z or Z–A.
Clicking an option sorts the product list alphabetically.
### Suomi
Tuotteet voi järjestää valikosta: A–Z tai Z–A.
Vaihtoehtoa klikkaamalla tuotteet menevät aakkosjärjestykseen.

## Installation & Usage / Asennus ja käyttö
### English
1. Clone or download the project.
2. Ensure the JSON file (warehouse.json) is saved in UTF‑8 encoding.
3. Open index.html in a browser.
4. The product table will load automatically, and search/sort features are immediately usable.

### Suomi
1. Lataa tai kloonaa projekti.
2. Varmista, että JSON‑tiedosto (warehouse.json) on tallennettu UTF‑8‑muodossa.
3. Avaa index.html selaimessa.
4. Tuotetaulukko latautuu automaattisesti, ja haku/järjestäminen toimii heti.




## Folder Structure / Kansiot
```
Product Finder/
│── index.html
│── styles.css
│── script.js
│── warehouse.json
└── README.md
```

## Technologies Used/Käytetyt teknologiat
### English:  
This project is built with simple, modern web technologies:
- HTML
- CSS
- JavaScript
-JSON data

### Suomi:  
Tämä projekti on toteutettu kevyillä ja moderneilla web‑teknologioilla:
-HTML
-CSS
-JavaScript
-JSON data
