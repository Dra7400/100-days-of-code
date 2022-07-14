port csv
with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    print(data)

import pandas
