Oppgave 2

1. Hvilke åpne datakilder er identifisert som relevante for miljødata, og hva er kriteriene (f.eks. kildeautoritet, datakvalitet, tilgjengelighet, brukervennlighet osv.) for å vurdere deres pålitelighet og kvalitet?

    Datakilden vi bruker i koden for å hente værdata er MET NORWAY API. Grunnen for dette valget er på grunn av brukervennlighet, datakvalitet, høy pålitelighet og kilden er lett tilgjengelig. For det første er dataen fra MET Norway meget brukervennlig ettersom den blir levert i JSON – format som gjør det enkelt å lese inn. For det andre brukes dataen av både forskningsinstitusjoner og den offentlige sektoren, noe som gir oss stor troverdighet til datakvaliteten. For det tredje er påliteligheten til MET Norway betraktelig økt, på grunn av MET Norway er en anerkjent nasjonal institusjon for metrologisk data. Til slutt, er dataen fra institusjonen lett tilgjengelig på grunn av API er åpent.

2. Hvilke teknikker (f.eks. håndtering av CSV-filer, JSON-data) er valgt å bruke for å lese inn dataene, og hvordan påvirker disse valgene datakvaliteten og prosessen videre? 

    Det er brukt ulike teknikker for å lese inn dataen inn i koden som: requests.get() for henting av JSON – data, (weather_data.json) for videre bruk og lagring i JSON – fil, konvertering til CSV for enklere databehandling med Pandas (weather_data.csv) og for å trekke ut relevante data bruker vi pandasql.sqldf() for SQL – analyse.

    Videre vil dette påvirke datakvaliteten og prosessen ved å ha et strukturert CSV – format, optimalisert datahåndtering og SQL. Et strukturert CSV – format vil gjøre dataen betraktelig enklere for bruk i analyseverktøy som Pandas og SQL. Videre vil en reduksjon av filstørrelsen forbedre ytelsen på koden ettersom kun de nødvendige detaljene trekkes ut på grunn av en effektiv datahåndtering. Til slutt, ved å trekke ut spesifikke målinger med SQL, som luftfuktighet og vind, vil dette produsere bedre innsikt i datasettene.


3. Dersom det er brukt API-er, hvilke spesifikke API-er er valgt å bruke, og hva er de viktigste dataene som kan hentes fra disse kildene?

    Begge kodene bruker API-er fra MET Norway (Meteorologisk institutt) for å hente værdata. Spesifikt brukte de API endepunktet "https://api.met.no/weatherapi/locationforecast/2.0/compact". Dette API-et gir værprognoser basert på en spesifik geografisk plassering ved hjelp av breddegrad og lengdegrad, i dette tilfellet over Oslo. Data som kan hentes fra denne API-en er for eksempel lufttrykk, luftfuktighet, lufttemperatur, vindretning og vindhastighet. Hvilke data som er viktigst vil være subjektivt utifra bruksområdet, ettersom luftfuktighet vil være viktig for en pilot, men ubetydelig for de fleste, mens lufttemperatur vil være viktig for de aller fleste.


Oppgave 3

1. Hvilke metoder vil du bruke for å identifisere og håndtere manglende verdier i datasettet?

    For å identifisere og håndtere manglende verdier i datasettet bruker vi dropna(). Grunnen til dette er at dropna() er en effektiv funksjon for å fjerne rader med manglende verdier. Videre, ettersom vi bruker pandas Dataframe for å rydde i dataen før en analyse, styrker dette vårt argument angående dropna().

2. Kan du gi et eksempel på hvordan du vil bruke list comprehensions for å manipulere dataene?

    

3. Hvordan kan Pandas SQL (sqldf) forbedre datamanipuleringen sammenlignet med tradisjonelle Pandas-operasjoner?

4. Hvilke spesifikke uregelmessigheter i dataene forventer du å møte, og hvordan planlegger du å håndtere dem?