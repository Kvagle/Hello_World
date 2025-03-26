Oppgave 2
1. Hvilke åpne datakilder er identifisert som relevante for miljødata, og hva er kriteriene (f.eks. kildeautoritet, datakvalitet, tilgjengelighet, brukervennlighet osv.) for å vurdere deres pålitelighet og kvalitet?


2. Hvilke teknikker (f.eks. håndtering av CSV-filer, JSON-data) er valgt å bruke for å lese inn dataene, og hvordan påvirker disse valgene datakvaliteten og prosessen videre?


3. Dersom det er brukt API-er, hvilke spesifikke API-er er valgt å bruke, og hva er de viktigste dataene som kan hentes fra disse kildene?

Begge kodene bruker API-er fra MET Norway (Meteorologisk institutt) for å hente værdata. Spesifikt brukte de API endepunktet "https://api.met.no/weatherapi/locationforecast/2.0/compact". Dette API-et gir værprognoser basert på en spesifik geografisk plassering ved hjelp av breddegrad og lengdegrad, i dette tilfellet over Oslo. Data som kan hentes fra denne API-en er for eksempel lufttrykk, luftfuktighet, lufttemperatur, vindretning og vindhastighet. Hvilke data som er viktigst vil være subjektivt utifra bruksområdet, ettersom luftfuktighet vil være viktig for en pilot, men ubetydelig for de fleste, mens lufttemperatur vil være viktig for de aller fleste. 

Oppgave 3
1. Hvilke metoder vil du bruke for å identifisere og håndtere manglende verdier i datasettet?

2. Kan du gi et eksempel på hvordan du vil bruke list comprehensions for å manipulere dataene?

3. Hvordan kan Pandas SQL (sqldf) forbedre datamanipuleringen sammenlignet med tradisjonelle Pandas-operasjoner?

4. Hvilke spesifikke uregelmessigheter i dataene forventer du å møte, og hvordan planlegger du å håndtere dem?