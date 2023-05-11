# Generator przykladowych plikow

import pandas as pd
import random
from random import uniform, choice
from string import ascii_lowercase
file_length = 1000
names = []
latitudes = []
longitudes = []

for i in range(file_length):
    words = random.randint(6, 15)
    col1 = [''.join(choice(ascii_lowercase) for j in range(words))]
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
df.to_excel('file2.xlsx', index=False)