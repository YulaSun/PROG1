import datetime
print('Welkom. Berichten?')
print('Er zijn station Amsterdam, Den Haag, Utrecht!')
station= input('Welke station ben je? \n')


from datetime import datetime
tijd=datetime.now()
print('Het is nu:', tijd)

vraag = input('Wil je anoniem? vul ja of nee: \n')
if vraag == 'ja':
    naam = 'anoniem'
    bericht=input('hoi, u mag berichten hier laten! Tip: maximaal 140 woorden\n')


else:
    naam = input ('Wat is je naam?')
    bericht= input(f'hoi!{naam},u mag berichten hier laten! Tip: maximaal 140 woorden\n')

f=open("C:/Users/yulas/Documents/stationzuilen.txt",'a')
f.write(f'{naam};{bericht};{tijd},{station}')
f.close()

print('Bedankt voor je reactie.')