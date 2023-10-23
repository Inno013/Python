import pandas as pd
from fuzzywuzzy import fuzz

# import os
# print(os.listdir('Pertemuan-6/'))
# membaca data dan simpan ke variabel df/dataframe
df = pd.read_csv('Pertemuan-6/room_type.csv')
print(df.head(15))

# def get_ratio(row):
#   string1 = row['Expedia']
#   string2 = row['Booking.com']
#   partial_rasio = fuzz.partial_ratio(string1, string2)
#   return partial_rasio

# rasionya = df.apply(get_ratio, axis=1)
# rasionya.head(15)