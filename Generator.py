# Generator przykladowych plikow

import pandas as pd
from random import uniform, choice
from string import ascii_lowercase
length = 1000

for i in range(length):
    names = [''.join(choice(ascii_lowercase) for j in range(10))]
    latitudes = [round(uniform(-90, 90), 6)]
    longitudes = [round(uniform(-180, 180), 6)]

df = pd.DataFrame({
    'Name': names,
    'Latitude': latitudes,
    'Longitude': longitudes
})
df.to_excel('file2.xlsx', index=False)
