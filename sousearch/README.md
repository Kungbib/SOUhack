# sousearch

Minimal söktjänst för SOU-material baserad på Django och Elasticsearch.

## Installera

1. Installera nödvändiga moduler med pip install -r requirements.txt

2. Skapa en tom databas och justera inställningarna för databasen i
   settings.py

2. Skapa din egen SECRET_KEY i settings.py

3. Skapa tabellerna i databasen med python manage.py makemigrations och
   python manage.py migrate

4. Ställ in vilken katalog SOU-textfilerna ligger i i variabeln
   SOUTXTPATH i filen settings.py

4. Uppdatera settings.py med inställningar för din elasticserver under
   variabeln HAYSTACK_CONNECTIONS (främst URL)

5. Testa att webbapplikationen startar genom att köra python manage.py
   runserver

6. Skapa SOU-objekt i databasen med python manage.py import_sou_data

7. Läs in Libris-id med python manage.py collect_sou_metadata

7. Läs in textdokument i elastic med python manage.py rebuild_index

8. Starta servern lokalt med python manage.py runserver (kolla att det
   funkar)


## Uppdatera till ny version av applikationen

1. Gör git pull i katalogen för din applikation

1. Gör om steg 4 för att få in ev. databasuppdateringar.
