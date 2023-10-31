from datetime import datetime
import psycopg2

moderatornummer = int(input('Wat is jou moderatornummer?'))

f=open("stationzuil.csv",'r')
list = f.readlines()
f.close()

#print(list)


for bericht in list:

    if bericht != 'sep=;\n':
        bericht=bericht.strip().split(';')
        print(bericht)
        print(f'naam:{bericht[0]}, bericht:\n{bericht[1]}')
        beoordeling=input('goedkeuren of afkeuren?')


        while beoordeling != 'goedkeuren' and beoordeling != 'afkeuren':
            beoordeling=input('Voer nog een keer in, aub.')

        naam=bericht[0]
        test=bericht[1]
        datum=bericht[2]
        tijd=bericht[3]
        station=bericht[4]

        now = datetime.now()
        beoordelingsdatum=now.strftime("%Y-%m-%d")
        beoordelingstijd=now.strftime("%H:%M")

        connection_string = "host='localhost' dbname='Stationzuil' user='postgres' password='01250'"
        conn = psycopg2.connect(connection_string)
        cursor = conn.cursor()
        query = """INSERT INTO Bericht (moderatornummer, naam, datum, tijd, station, bericht, beoordeling, beoordelingsdatum, beoordelingstijd) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);"""
        data = (moderatornummer, naam, datum, tijd, station, test, beoordeling, beoordelingsdatum, beoordelingstijd)
        cursor.execute(query, data)
        conn.commit()
        conn.close()


fw=open("stationzuil.csv",'w')
fw.write("sep=;\n")





