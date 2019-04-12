# RailNL door Koffie-uit-G

## Introductie
*Het probleem:* 
Er zijn tientallen stations in Nederland, waaronder een aantal kritieke stations. Kritieke stations zijn de stations die per se bereden moeten worden in een bepaalde dienstregeling. Nu is het aan ons om verschillende trajecten uit te zetten die ervoor zorgen dat (minimaal) deze kritieke stations en diens connecties bereden worden. Dit zullen wij uitzetten voor het spoor van Noord- en Zuid-Holland en vervolgens voor geheel Nederland. Een aantal belangrijke voorwaarden voor Noord en Zuid-Holland zijn: er mogen maximaal zeven trajecten rijden om de stations te bereiken, en ieder traject mag maximaal 120 minuten duren. Voor het spoor van heel Nederland mogen dit maximaal twintig trajecten zijn binnen een tijdsspan van 180 minuten per traject.
Wanneer wij een werkend algoritme hebben ontwikkeld, willen we deze gaan verbeteren. Een dienstregeling is kwalitatief beter dan een andere dienstregeling wanneer er met minder trajecten meer kritieke stations bezocht kunnen worden.

## Methoden

*K = p*10000 - (T*20 + Min/10)* 

Dit is de formule waarmee de kwaliteit van een dienstregeling kan worden berekend. Hier staat p voor de fractie van bereden kritieke verbindingen (tussen 0 en 1), de T staat voor de hoeveelheid trajecten en Min staat voor de totale lengte in minuten van de dienstregeling. 

*UML* 

Voor ons programma hebben wij vier klassen opgesteld. Het station, het spoor, de dienstregeling en het traject.
- Het station bestaat uit de naam van het station, en de connecties + minuten ervan. Tevens bevat het station een boolean waarde of deze kritiek is. 
- Het spoor zet alle stations en connecties uit. Zie dit als een soort blauwdruk die de dienstregeling kan gebruiken om de trajecten op uit te zetten.
- De dienstregeling kan aan de hand van het spoor trajecten uitzetten. Deze houdt verschillende dingen bij: de totale lengte van het traject, de totale hoeveelheid aan trajecten die zijn uitgezet en de kwaliteit. Tevens houdt de dienstregeling bij welke connecties al bezocht zijn. Met zijn functies kan deze klasse deze waardes toevoegen. 
- Het traject bevat een maximale lengte die het mag rijden, de tijd die het traject al heeft afgelegd en een lijst met bezochte stations die worden doorgegeven aan de dienstregeling.

*Algoritmes*

Voor nu hebben wij een aantal algoritmen geselecteerd die wij willen gaan implementeren om de kwaliteit van de dienstregeling zo goed mogelijk te maken:
- Brute force. Dit algoritme gebruikt geen shortcuts om de kwaliteit te verbeteren. Hierom is dit goed voor ons om een start te maken met onze dienstregeling. 
- Uniform costs (Dijkstra’s algoritme): Dit algoritme focust zich op het vinden van de kortste paden op het spoor. Dit algoritme kiest eerst het unvisited en kortste pad, en berekent de tijd om een buurpad te bereiken. 
- Greedy. Dit algoritme kiest per node de beste route, en kijkt vervolgens pas verder. Dit is het grote verschil tussen Uniform costs en greedy. 
- Hill climber. Dit algoritme begint met een random solution, en maakt vervolgens verbeteringen aan deze dienstregeling. 
(Evolutionary algorithms)

## Resultaten

*De formule*

In het geval van NH en ZH is de maximale score K=p (p=1) *10000 - (T (T = 7 ) * 20 + Min (Min = 7*120)/10) = 9776. Waarbij alle kritieke stations bezocht zijn. 
Alle kritieke connecties bij elkaar zijn 297 minuten, en in de ideale wereld zouden we dat dus in drie trajecten (297/120) moeten kunnen afleggen. In dit geval zou de kwaliteit van NH en ZH dit zijn: K = p(p=1) * 10000 -( T (T=3) * 20 + Min (Min = 297)/10) = 9969,7.
Helaas is dit in het echt niet mogelijk (we checked). 

## Discussie


