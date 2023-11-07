print('Welkom. Berichten hier laten?')


# random een station halen
import random

stations = ['Arnhem', 'Almere', 'Amersfoort', 'Almelo', 'Alkmaar', 'Apeldoorn', 'Assen', 'Amsterdam', 'Boxtel', 'Breda', 'Dordrecht', 'Delft', 'Deventer','Enschede', 'Gouda', 'Groningen', 'Den Haag', 'Hengelo', 'Haarlem', 'Helmond', 'Hoorn', 'Heerlen', 'Den Bosch', 'Hilversum', 'Leiden', 'Lelystad', 'Leeuwarden', 'Maastricht', 'Nijmegen', 'Oss', 'Roermond', 'Roosendaal', 'Sittard', 'Tilburg', 'Utrecht', 'Venlo', 'Vlissingen', 'Zaandam', 'Zwolle', 'Zutphen']
station=random.choice(stations)
print(station)

# huidig datum en tijd halen
from datetime import datetime
now = datetime.now()
print(now.strftime("%Y-%m-%d %H:%M"))
datum=now.strftime("%Y-%m-%d")
tijd=now.strftime("%H:%M")

# met if en else: anoniem of naam opslaan
vraag = input('Wil je anoniem? vul ja of nee: \n')
if vraag == 'ja':
    naam = 'anoniem'
    bericht=input('hoi, u mag berichten hier laten! Tip: maximaal 140 woorden\n')

else:
    naam = input ('Wat is je naam?')
    bericht= input(f'hoi!{naam},u mag berichten hier laten! Tip: maximaal 140 woorden\n')

# open csv bestand en slagen informatie op
f=open("stationzuil.csv",'a')
f.write(f'{naam};{bericht};{datum};{tijd};{station} \n')
f.close()


print('Bedankt voor je reactie.')

