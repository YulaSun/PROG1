from datetime import datetime
import psycopg2

# vragen naar moderatornummer en naam
moderatornummer = int(input('Wat is jou moderatornummer?'))
naam = input('Wat is jou naam?')

# verbinden met sql database
connection_string = "host='172.187.168.178' dbname='stationzuil' user='postgres' password='01250'"
with psycopg2.connect(connection_string) as conn:
    with conn.cursor() as cursor:
        # zoek in sql of moderatornummer en naam overeenkomen/bestaan
        moderatornummer1 = "SELECT moderatornummer FROM moderator WHERE naam = %s;"
        cursor.execute(moderatornummer1, (naam,))
        result = cursor.fetchone()

        if result:
            # wel overeenkomen, dan mag de moderator verder berichten lezen
            moderatornummer_database = result[0]
            if moderatornummer == moderatornummer_database:
                print('Brichten box is open.')
                f = open("stationzuil.csv", 'r')
                list = f.readlines()
                f.close()

                for bericht in list:
                    # met 'sep=;' wordt csv bestand verdeeld met ';'
                    if bericht != 'sep=;\n':
                        bericht = bericht.strip().split(';')
                        print(bericht)
                        print(f'naam:{bericht[0]}, bericht:\n{bericht[1]}')
                        beoordeling = input('goedkeuren of afkeuren?')

                        # de moderator mag niet iets anders invoeren dan goedkeuren of afkeuren
                        while beoordeling != 'goedkeuren' and beoordeling != 'afkeuren':
                            beoordeling = input('Voer nog een keer in, aub.')

                        naam = bericht[0]
                        test = bericht[1]
                        datum = bericht[2]
                        tijd = bericht[3]
                        station = bericht[4]

                        now = datetime.now()
                        beoordelingsdatum = now.strftime("%Y-%m-%d")
                        beoordelingstijd = now.strftime("%H:%M")


                        # voeg data toe in sql
                        query = """INSERT INTO Bericht (moderatornummer, naam, datum, tijd, station, bericht, beoordeling, beoordelingsdatum, beoordelingstijd) 
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);"""
                        data = (
                            moderatornummer, naam, datum, tijd, station, test, beoordeling, beoordelingsdatum,
                            beoordelingstijd)
                        cursor.execute(query, data)

                with open("stationzuil.csv", 'w') as fw:
                    fw.write("sep=;\n")

            # komt niet overeen, afsluiten
            else:
                print('Moderatornummer bestaat niet of moderatornummer komt niet overeen met uw naam. \nOpnieuw aub.')

        # komt niet overeen, afsluiten
        else:
            print('Moderatornummer bestaat niet of moderatornummer komt niet overeen met uw naam. \nOpnieuw aub.')





