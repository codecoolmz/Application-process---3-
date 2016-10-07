import random
import csv


first_name = ['Miklós', 'Tamás', 'Dániel', 'Mateusz', 'Attila', 'Pál', 'Sándor', 'Prezmek', 'John', 'Tim', 'Matthew',
              'Andy', 'Giancarlo']

last_name = ['Beöthy', 'Tompa', 'Salamon', 'Ostafil', 'Molnár', 'Monoczki', 'Szodoray', 'Ciacka', 'Carrey', 'Obama',
             'Lebron', 'Hamilton', 'Fisichella']

email = random.choice(first_name) + '@codecool.com'

city = ['Budapest', 'Miskolc', 'Krakow', 'Barcelona', 'New York']

phone_number = '+' + str(random.randint(1000000000, 9999999999))


with open('fake_data.csv', 'w') as f:
    writer = csv.writer(f)
    row = []
    for i in range(10000):
        row.append(random.choice(first_name))
        row.append(random.choice(last_name))
        row.append(phone_number)
        row.append(email)
        row.append(random.choice(city))
        row.append(random.randint(1, 10))
        row.append(random.randint(1960, 1995))
        writer.writerow(row)
        row = []
