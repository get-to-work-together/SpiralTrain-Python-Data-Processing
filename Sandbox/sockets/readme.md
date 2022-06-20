## Korte toelichting bij socket demo

###### Peter Anema in oktober 2019

Deze socket demo bestaat uit twee gedeeltes: een server en een client.

De **server** (ok wel listener genoemd) wordt als eerste opgestart en wacht op binnenkomende verbindingen van clients. De verbindingen wordt gelegd via een IP adres op een bij gespecificeerde port. Nadat er een verbinding gemaakt is met een client kan er een uitwisseling van berichten tussen de client en server plaatsvinden.

In deze demo neemt de server het initiatief en stuurt een prompt naar de client en wacht op antwoord. Na het verwerken van het antwoord wordt er door de server opnieuw een prompt gestuurd. Een client die verbinding heeft gemaakt ontvangt de prompt van de server. De gebruiker kan een antwoord geven die weer terug wordt gestuurd naar de server.

Er zijn twee varianten van een server. De eerste variant (socket_listener.py) kan met slechts één client tegelijk verbonden zijn. De tweede variant (socket_listener_multithread.py) kan verbinding maken met meerdere clients. Voor iedere client die een verbinding maakt wordt een aparte thread aangemaakt de separaat de communicatie met die client afhandeld.

De **client** maakt bij het opstarten verbinding met de server. Het is natuurlijk belangrijk dat de gebruikte ip-adres en port overeenkomen met de ip-address en port die bij de server worden gebruikt. In deze demo wacht de client vervolgens op een bericht vanuit de server. Op dit bericht kan de gebruiker een antwoord geven. Het antwoord wordt verstuurd naar de server en de client wacht opnieuw op een volgend bericht. Er zijn twee soorten clients geïmplementeerd in deze demo. Een client die werkt met het console (socket_client.py) en een client die werkt met een GUI (socket_client.gui.py). Bij de console client worden de berichten vanuit de server weergegeven op de console en kan de gebruik een antwoord invoeren. Als de return toets wordt ingedrukt wordt het ingevoerde antwoord verstuurd naar de server. Bij de GUI client verschijnen de berichten vanuit de server in een aparte tekstvak en is een tweede tekstvak waarin een antwoord kan worden ingevoerd. Door op de 'Send' knop te drukken wordt het antwoord verstuurd naar de server.

Bij de multithread server kunnen meerdere clients afzonderlijk van elkaar verbinding maken en berichten uitwisselen. Meestal ullen de verschillende clients wordt uitgevoerd op verschillende computers met verschillende gebruikers. Het is mogelijk op een computer meerdere clients te draaien. Dit is bijvoorbeeld handig bij het testen van de applicatie. De verschillende clients dienen dan in afzonderlijke terminal sessies te worden opgestart. Dit is het beste te doen vanuit een console met de opdracht: python socket_client.py of python socket_client_gui.py.

Zowel de server als de client is de socket communicatie geïmplementeerd met behulp van de socket package. Bij de server wordt daarnaast gebruik gemaakt van de threading package om de aparte threads te realiseren. De GUI client is geïmplementeerd met tkinter.

De bestanden:
- **socket_client.py**: De console based client
- **socket_client_gui.py**: Een client met een tkinter GUI
- **socket_listener.py**: De single client server
- **socket_listener_multithread.py**: De multithreaded server
- **readme.md** : Dit bestand. Een markdown file.