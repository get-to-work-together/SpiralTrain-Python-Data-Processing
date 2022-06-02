# Opdracht 1.1 - Functie Beschrijvende Statistiek

Van een reeks getallen kunnen een aantal beschrijvende kenmerken worden afgeleid. Bijvoorbeeld het aantal getallen, het hoogste getal, het laagste, de som van de getallen en de gemiddelde van de getallen. 

In deze opdracht maak je een functie die op basis van een lijst van getallen een dictionary met kenmerken terug geeft.

### Stap 1:	Maak een lijst met een aantal willekeurige gehele getallen.
Tip: `getallen = [55, 86, 98, 13, 51, 46, 9, 60, 22, 69, 56, 17, 29, 86, 26, 88]`
Of gebruik de random library: `getallen = [random.randint(1, 100) for _ in range(20)]`

### Stap 2:	Maak een functie, bv. analyseer(), die als argument een lijst aanneemt.
Tip: def analyseer(getallen):

### Stap 3:	Maak een lege dictionary. Deze wordt in de volgende stap gevuld met verschillende statistische kenmerken.
Tip: d = {}

### Stap 4:	Bepaal in de functie de volgende berekeningen en neemt de berekende waarden op in de dictionary.
- aantal: Het aantal getallen
- minimum: Het laagste getal
- maximum: Het hoogste getal
- som: De som van de getallen
- gemiddelde: Het gemiddelde van de getallen
- mediaan: Het middelste getal als de getallen gesorteerd zijn.
- eerste_kwartiel: Het getal op een vierde van de gesorteerde getallen
- derde_kwartiel: Het getal op drie vierde van de gesorteerde getallen
Tip: b.v. `d['aantal'] = len(getallen)`
Of gebruik de statistics library: `statistcs.quantiles(getallen)`

### Stap 5:	Geef de dictionary terug als uitkomst van de functie.
Tip: return d

### Stap 6:	Test de functie door de functie aan te roepen de lijst van willekeurige getallen en het resultaat te printen.

### ★ Stap 7:	Bepaal ook de interkwartielafstand: IQR = Q3 - Q1. Voeg dit in de functie ook toe als kenmerk aan de dictionary.

### ★ Stap 8:	Op basis van het interkwartielafstand kunnen de grenzen voor outliers worden bepaald. Outliers liggen 1.5 * IQR beneden het eerste kwartiel en boven het derde kwartiel. Voeg ook deze grenzen toe aan de kenmerken die functie bepaald.

### ★ Stap 9:	Geef ook een list van outliers terug.
 
