Oppgave 2

1. Hvilke åpne datakilder er identifisert som relevante for miljødata, og hva er kriteriene (f.eks. kildeautoritet, datakvalitet, tilgjengelighet, brukervennlighet osv.) for å vurdere deres pålitelighet og kvalitet?

    Datakilden vi bruker i koden for å hente værdata er MET NORWAY API. Grunnen for dette valget er på grunn av brukervennlighet, datakvalitet, høy pålitelighet og kilden er lett tilgjengelig. For det første er dataen fra MET Norway meget brukervennlig ettersom den blir levert i JSON – format som gjør det enkelt å lese inn. For det andre brukes dataen av både forskningsinstitusjoner og den offentlige sektoren, noe som gir oss stor troverdighet til datakvaliteten. For det tredje er påliteligheten til MET Norway betraktelig økt, på grunn av MET Norway er en anerkjent nasjonal institusjon for metrologisk data. Til slutt, er dataen fra institusjonen lett tilgjengelig på grunn av API er åpent.

2. Hvilke teknikker (f.eks. håndtering av CSV-filer, JSON-data) er valgt å bruke for å lese inn dataene, og hvordan påvirker disse valgene datakvaliteten og prosessen videre? 

    Det er brukt ulike teknikker for å lese inn dataen inn i koden som: requests.get() for henting av JSON – data, (weather_data.json) for videre bruk og lagring i JSON – fil, konvertering til CSV for enklere databehandling med Pandas (weather_data.csv) og for å trekke ut relevante data bruker vi pandasql.sqldf() for SQL – analyse.

    Videre vil dette påvirke datakvaliteten og prosessen ved å ha et strukturert CSV – format, optimalisert datahåndtering og SQL. Et strukturert CSV – format vil gjøre dataen betraktelig enklere for bruk i analyseverktøy som Pandas og SQL. Videre vil en reduksjon av filstørrelsen forbedre ytelsen på koden ettersom kun de nødvendige detaljene trekkes ut på grunn av en effektiv datahåndtering. Til slutt, ved å trekke ut spesifikke målinger med SQL som luftfuktighet og vind, vil dette produsere bedre innsikt i datasettene.


3. Dersom det er brukt API-er, hvilke spesifikke API-er er valgt å bruke, og hva er de viktigste dataene som kan hentes fra disse kildene?

    Begge kodene bruker API-er fra MET Norway (Meteorologisk institutt) for å hente værdata. Spesifikt brukte de API endepunktet "https://api.met.no/weatherapi/locationforecast/2.0/compact". Dette API-et gir værprognoser basert på en spesifik geografisk plassering ved hjelp av breddegrad og lengdegrad, i dette tilfellet over Oslo. Data som kan hentes fra denne API-en er for eksempel lufttrykk, luftfuktighet, lufttemperatur, vindretning og vindhastighet. Hvilke data som er viktigst vil være subjektivt utifra bruksområdet, ettersom luftfuktighet vil være viktig for en pilot, men ubetydelig for de fleste, mens lufttemperatur vil være viktig for de aller fleste.


Oppgave 3

1. Hvilke metoder vil du bruke for å identifisere og håndtere manglende verdier i datasettet?

    For å identifisere og håndtere manglende verdier i datasettet bruker vi dropna(). Grunnen til dette er at dropna() er en effektiv funksjon for å fjerne rader med manglende verdier. Videre, ettersom vi bruker pandas Dataframe for å rydde i dataen før en analyse, styrker dette vårt argument angående dropna().

2. Kan du gi et eksempel på hvordan du vil bruke list comprehensions for å manipulere dataene?

    Vi bruker list comprehensions for å gjøre tidsstemplene mer lesbare. Under kommentaren "List Comprehensions", kan man se hvordan vi har brukt list comprehensions til å bytte ut "T" i tidsstemplene med et mellomrom. På denne måte kan vi formatere datene uten å måtte bruke eksplisitte løkker, og det er mer effektivt. 

3. Hvordan kan Pandas SQL (sqldf) forbedre datamanipuleringen sammenlignet med tradisjonelle Pandas-operasjoner?

    Det finnes flere grunner for å bruke pandas SQL ovenfor tradisjonelle Pandas-operasjoner. En god grunn kan være det at SQL-syntaks er ofte mer intuitivt og lettere å lese. Et annet poeng er det at Pandas SQL forenkler kompleks datahåndtering, i det at SQL gjør det enklere å utføre operasjoner som querys og subquerys. 

4. Hvilke spesifikke uregelmessigheter i dataene forventer du å møte, og hvordan planlegger du å håndtere dem?

    1. Manglende verdier:
        Dette håndterer vi ved å fjerne rader med manglende verdier.
    2. Ekstreme eller feilaktige verdier:
        De fysiske sensorene kan gi urealistiske målinger, disse planlegger vi å filtrere ut i koden.
    3. Dupliserte rader:
        Dersom en rad blir duplisert eller gjentas flere ganger, vil vi filtrere de ut i koden.
    4. Manglende enheter eller inkonsekvent skalering:
        Dersom verdiene fra sensorene er i forskjellige måleenheter, for eksempel at vindhastigheten kommer i km/t og ikke m/s, vil vi konvertere disse verdiene slik at de blir i m/s. 


Oppgave 4

1. Hvordan kan du bruke NumPy og Pandas til å beregne gjennomsnitt, median og standardavvik for de innsamlede dataene, og hvorfor er disse statistiske målene viktige?

    For å enkelt beregne grunnleggende statistiske mål for variablene i datasettet, som lufttemperatur og vindhastighet. Kan vi bruke NumPy – funksjoner som «np.mean», «np.median» og «np.std». For å utføre våre beregninger konverterer koden relevante kolonner fra «df_cleaned» til Numpy – arrays. Dette er meget nyttig ettersom; gjennomsnitt gir et bilde av det generelle. Medianen gir et bedre mål for sentraltendens i ujevn data og er robust mot ekstreme verdier. Til slutt gir standardavviket innsikt i hvor stabile miljøforholdene er og viser variasjonen av data fra gjennomsnittet.

2. Kan du gi et eksempel på hvordan du vil implementere en enkel statistisk analyse for å undersøke sammenhengen mellom to variabler i datasettet?

    Et eksempel er å undersøke sammenhengen mellom lufttemperatur og vindhastigheten som en korrelasjonsanalyse i koden. Dette gjør vi med funksjonen «df_cleaned['Lufttemperatur'].corr(df_cleaned['Vindhastighet'])». Dette vil utgi en verdi mellom -1 og 1, som indikerer hvor sterkt og i hvilken retning variablene har samvariasjon. En negativ korrelasjon betyr at når temperaturen minker, vil dette også utspillet seg for vindhastigheten. Videre vil dette også skje for positiv korrelasjon, men omvendt for temperatur og vindhastighet.

3. Hvordan planlegger du å håndtere eventuelle skjevheter i dataene under analysen, og hvilke metoder vil du bruke for å sikre at analysen er pålitelig?

    For å håndtere eventuelle skjevheter i dataen under analysen vil vi bruke IQR – metoden (Interquatile Range). Metoden filtrerer bort ekstreme verdier i dataen rundt lufttemperatur. Dette blir oppnådd ved å identifisere og fjerne verdier før videre analyse som er utenfor IQR fra kvartalene Q1 og Q3 ganget med 1.5. Ved en slik metode reduseres risikoen for enkelbestemte ekstreme målinger forvrenger resultatene, og til slutt gjør dette analysen mer pålitelig.

4. Hvilke visualiseringer vil du lage for å støtte analysen din, og hvordan vil disse visualiseringene hjelpe deg med å formidle funnene dine?

    Visualiseringer som vil støtte analysen og hjelpe formidlingsevnen av dataen vil bestå av; søylediagram og tidsserieplott. Visualiseringene vil bistå med å gjøre statistiske funn enklere å forstå og gi visuell troverdighet for eventuelle konklusjoner som blir tatt i analysen.
    Søylediagram vil gi en rask visuell forståelse av spredningen av dataen hvor gjennomsnitt, median og standardavvik for lufttemperatur og vindhastighet sammenlignes. I tillegg vil tidsserieplott bidra til å identifisere trender og sesongvariasjoner i temperaturdataene ved å visualisere glidende gjennomsnitt av temperatur over tid.


Oppgave 5

1. Hvilke spesifikke typer visualiseringer planlegger du å lage for å representere endringer i luftkvalitet og temperaturdata, og hvorfor valgte du disse?

    For å vise ulike aspekter ved temperaturdataene blir det brukt forskjellige typer visualiseringer som; interaktiv graf, tabellvisning og tidsserieplot. Ved å kombinere interaktive og statiske former for å gjøre analysen mer tilgjengelig. Til slutt er de ulike typene visualiseringen valgt for å gi både detaljer og oversikt.
    Først for å utforske trendene på en fleksibel måte vil en interaktiv graf med gjennomsnitt av temperatur med justerbart tidsvindu utnyttes. Videre vil tabellvisning med utvalgte tidspunkter gjøre det lettere å identifisere mønstre gjennom dagen. I tillegg vil fargekoding visualisert i tabellen gi en rask visuell forståelse av temperaturtopper og soner. Til slutt, vil tidsserieplot gi god innsikt i trender og variasjoner ved hjelp av Seaborn som viser utviklingen i lufttemperatur over tid.

2. Hvordan kan Matplotlib og Seaborn brukes til å forbedre forståelsen av de analyserte dataene, og hvilke funksjoner i disse bibliotekene vil være mest nyttige?

    Ved å bruke både Matplotlib og Seaborn vil bibliotekene gi både fleksibilitet og kraft slik at det er mulig å tilpasse visualiseringene til målgruppen.
    Matplotlib har funksjoner som «plt.plot()», «plt.xticks(rotation=45)» og «plt.tight_layout()». Dette gir både god kontroll over layout og visning og brukes til den interaktive grafen, som er en tilpasset plotting. Til slutt har Seaborn funksjoner som bygger på Matplotlib. Dette gir mer estetiske standardstiler og enklere syntaks. Funksjonen «sns.lineplot()» brukes for å tegne tydelige tidsseriegrader med automatisk håndtering av datoer og utjevning av kurver.

3. Hvordan vil du håndtere og visualisere manglende data i grafene dine for å sikre at de fortsatt er informative?

    Ved å bruke Pandas og metoder som «.dropna()» for å fjerne rader med manglende verdier eller fylle inn verdier basert på tidligere observasjoner med «.fillna(method='ffill')», kan vi håndtere og visualisere manglende data.

4. Kan du beskrive prosessen for å lage interaktive visualiseringer med Widgets, Plotly eller Bokeh, og hvilke fordeler dette kan gi i forhold til statiske             visualiseringer?

    Sammen med ipywidgets og Matplotlib blir en interaktiv visualisering tegnet der brukeren kan endre på lengden på det glidende gjennomsnittet via en slider med «IntSlider». Dynamisk innsikt er en fordel med de interaktive visualiseringene. I tillegg kan brukere utforske dataen selv og tilpasse visningen til eget behov. Dette vil gjøre presentasjonen mer engasjerende. Prosessen for å lage interaktive visualiseringer er slik:
    
    1.	Definer en funksjon som tegner grafen basert på en variabel (her: window). 
    2.	Bruke interact() fra ipywidgets for å knytte funksjonen til en kontroll – widget.
    3.	Oppdatere grafen automatisk når brukeren justerer parameteren.

5. Hvordan vil du evaluere effektiviteten av visualiseringene dine i å formidle de viktigste funnene fra dataanalysen til et bredere publikum?

    Ved å bruke ulike evalueringsmetoder som; formidling, klarhet og tilgjengelighet vil visualiseringen vurderes for de viktigste funnene fra dataanalysene til et bredere publikum.
    Innenfor formidling kan det vurderes ut ifra om farger og formater brukes riktig for å fremheve viktige verdier. Videre er klarhet/tydelighet essensielt. Ved å se om er dataen er lett å forstå uten forklaring. Til slutt er tilgjengelighet viktig for å se om grafene er enkle å lese på tvers av ulike plattformer og målgrupper.

