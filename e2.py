import csv

with open("files/weather.csv") as file:
    data = list(csv.reader(file))
    print(data)

city = input("Enter a city: ")

for row in data:
    if row[0] == city:
        print(row)
