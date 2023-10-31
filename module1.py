
print('Welkom. Berichten hier laten?')

import random
stations = ['Amsterdam','DenHaag','Utrecht']
station=random.choice(stations)
print(stations)


from datetime import datetime
now = datetime.now()
print(now.strftime("%Y-%m-%d %H:%M"))
datum=now.strftime("%Y-%m-%d")
tijd=now.strftime("%H:%M")



vraag = input('Wil je anoniem? vul ja of nee: \n')
if vraag == 'ja':
    naam = 'anoniem'
    bericht=input('hoi, u mag berichten hier laten! Tip: maximaal 140 woorden\n')


else:
    naam = input ('Wat is je naam?')
    bericht= input(f'hoi!{naam},u mag berichten hier laten! Tip: maximaal 140 woorden\n')


f=open("stationzuil.csv",'a')
f.write(f'{naam};{bericht};{datum};{tijd};{station} \n')
f.close()


print('Bedankt voor je reactie.')

