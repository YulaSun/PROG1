from tkinter import *
import tkinter as tk
import psycopg2
import requests


root = tk.Tk()
image1= PhotoImage(file='fiets1.png')
image2= PhotoImage(file='lift1.png')
image3= PhotoImage(file='pr1.png')
image4= PhotoImage(file='wc1.png')


root.state('zoomed')


connection_string = "host='172.187.168.178' dbname='stationzuil' user='postgres' password='01250'"
conn = psycopg2.connect(connection_string)
cursor = conn.cursor()
cursor.execute( """ SELECT naam, datum, tijd, station, bericht from bericht WHERE beoordeling = 'goedkeuren'
ORDER BY datum DESC, tijd DESC LIMIT 5 """)

result = cursor.fetchall()

for row in result:

    naam=row[0]
    datum=row[1]
    tijd=row[2]
    station=row[3]
    bericht=row[4]

    my_frame = tk.Frame(root, borderwidth=2)
    my_frame.pack(padx=20, pady=20, side=LEFT)

    label1 = tk.Label(my_frame, text=f'{naam}  {datum},{tijd} \n {station}')
    label1.pack(side=tk.TOP, padx=10)

    label_with_image = tk.Label(my_frame)




    cursor.execute(""" SELECT ov_bike, elevator, park_and_ride, toilet from station_service WHERE station_city = %s""",(station,))


    result = cursor.fetchall()



    image1 = PhotoImage(file='fiets1.png')
    image2 = PhotoImage(file='lift1.png')
    image3 = PhotoImage(file='pr1.png')
    image4 = PhotoImage(file='wc1.png')
    image_list = [image1, image2, image3, image4]


    label_list = []

    cnt = 0
    for i in result:
        for j in i:
            if j:
                if 0 <= cnt < len(image_list):
                    image = image_list[cnt]
                    label = tk.Label(my_frame, image=image)
                    label.image = image
                    label.pack(padx=0.1, pady=0.1)
                    label_list.append(label)
                else:
                    print("Invalid index: ", cnt)
            cnt += 1

    city = station
    api_key = '81dec3a863d004ec25feb9e2bc43f1e0'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

    response = requests.get(url)
    data = response.json()
    print(data)

    weather = data["weather"]
    description = weather[0]["description"]
    weer=tk.Label(my_frame, text=f'{description}')
    weer.pack()

    label2 = tk.Label(my_frame, text=f'{bericht}', relief="solid", width=20, height=10)
    label2.pack(padx=10)





root.mainloop()

