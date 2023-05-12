# Generator przykladowych plikow

import pandas as pd
from random import uniform
from random_words import RandomWords
file_length = 1000
names = []
latitudes = []
longitudes = []
rw = RandomWords()

for i in range(file_length):
    col1 = rw.random_words()
    col2 = [round(uniform(-90, 90), 6)]
    col3 = [round(uniform(-180, 180), 6)]
    names.append(col1[0])
    latitudes.append(col2[0])
    longitudes.append(col3[0])

df = pd.DataFrame({
    'Name': names,
    'Latitude': latitudes,
    'Longitude': longitudes
})
df.to_excel('file1.xlsx', index=False)
