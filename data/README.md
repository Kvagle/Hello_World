Describes the data directory and datasets

    Det er brukt ulike teknikker for å lese inn dataen inn i koden som: requests.get() for henting av JSON – data, (weather_data.json) for videre bruk og lagring i JSON – fil, konvertering til CSV for enklere databehandling med Pandas (weather_data.csv) og for å trekke ut relevante data bruker vi pandasql.sqldf() for SQL – analyse.

   formatet vil gjøre dataen betraktelig enklere for bruk i analyseverktøy som Pandas og SQL. Videre vil en reduksjon av filstørrelsen forbedre ytelsen på koden ettersom kun de nødvendige detaljene trekkes ut på grunn av en effektiv datahåndtering. Til slutt, ved å trekke ut spesifikke målinger med SQL som luftfuktighet og vind, vil dette produsere bedre innsikt i datasettene.