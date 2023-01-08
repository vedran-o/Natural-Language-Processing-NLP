# III. zadatak
import csv
import pandas as pd
import re
from datetime import date, datetime
import numpy as np
from PIL import Image
from wordcloud import WordCloud, ImageColorGenerator, STOPWORDS
import seaborn as sns
from pyparsing import Regex

year_p = 0
month_p = 0
day_p = 0

year_k = 0
month_k = 0
day_k = 0

df = pd.read_csv("eVarazdin_2022-2019.csv", header=0)
df = df.drop_duplicates()

print("DATUM:\n")
while (year_p <= 2018 and month_p <= 0 and day_p <= 0):
    year_p = int(input('Pocetna godina: '))
    month_p = int(input('Pocetni mjesec: '))
    day_p = int(input('Pocetni dan: '))

    d_p = date(year_p, month_p, day_p)
    d_p = pd.to_datetime(d_p, ).date().strftime("%d.%m.%Y")
    # datetime.datetime.strptime(d, '%Y-%m-%d').strftime('%d/%m/%y')
    print(d_p)

while (year_k <= 2018 and month_k <= 0 and day_k <= 0):
    year_k = int(input('Krajnja godina: '))
    month_k = int(input('Krajnji mjesec: '))
    day_k = int(input('Krajnji dan: '))

    d_k = date(year_k, month_k, day_k)
    d_k = pd.to_datetime(d_k, ).date().strftime("%d.%m.%Y")
    # datetime.datetime.strptime(d, '%Y-%m-%d').strftime('%d/%m/%y') .strftime("%Y-%d-%m")
    print(d_k)

df['Datum'] = pd.to_datetime(df['Datum'])
mask = (df['Datum'] > d_p) & (df['Datum'] <= d_k)
pvm = df.loc[mask]
print(pvm)

df = pvm
sumator = int(year_k-year_p)

kolicina_objava = len(df.index)
print("OPIS:\n")
print("Kolicina objava u protekle {} godine: {}".format(sumator, kolicina_objava))

#broj vijesti vezanih uz korona tematiku
keywordDF = df[df['Naslov'].str.contains('.Covid.|.koronavirus.|.koron.|.samoizolacij.|.pandemij.|.COVID-19.|.Pfizer.|.BionTech.|.Sputnik V.|.AstraZeneca.', case = False, na = False, regex = True ) |
df['Podnaslov'].str.contains('.Covid.|.koronavirus.|.koron.|.samoizolacij.|.pandemij.|.COVID-19.|.Pfizer.|.BionTech.|.Sputnik V.|.AstraZeneca.', case = False, na = False, regex = True) |
df['Tekst'].str.contains('.Covid.|.koronavirus.|.koron.|.samoizolacij.|.pandemij.|.COVID-19.|.Pfizer.|.BionTech.|.Sputnik V.|.AstraZeneca.', case = False, na = False, regex = True) |
df['Link'].str.contains('.Covid.|.koronavirus.|.koron.|.samoizolacij.|.pandemij.|.COVID-19.|.Pfizer.|.BionTech.|.Sputnik V.|.AstraZeneca.', case = False, na = False, regex = True) |
df['Tagovi'].str.contains('.Covid.|.koronavirus.|.koron.|.samoizolacij.|.pandemij.|.COVID-19.|.Pfizer.|.BionTech.|.Sputnik V.|.AstraZeneca.', case = False, na = False, regex = True)]



rijeciDF = keywordDF[['Naslov','Podnaslov','Tekst','Tagovi','Datum']]
print(rijeciDF)

naslov_edit = rijeciDF['Naslov'].str.lower().str.split(expand = True)
naslov_edit =naslov_edit.melt()
naslov_edit = naslov_edit.drop(['variable'], axis = 1)
naslov_edit = naslov_edit.mask(naslov_edit.eq('None')).dropna()
naslov_lista = naslov_edit['value'].values.tolist()
print(naslov_lista)


podnaslov_edit = rijeciDF['Podnaslov'].str.lower().str.split(expand = True)
podnaslov_edit = podnaslov_edit.melt()
podnaslov_edit = podnaslov_edit.drop(['variable'], axis = 1)
podnaslov_edit = podnaslov_edit.mask(podnaslov_edit.eq('None')).dropna()
podnaslov_lista = podnaslov_edit['value'].values.tolist()
print(podnaslov_lista)


tekst_edit = rijeciDF['Tekst'].str.lower().str.split(expand = True)
tekst_edit =tekst_edit.melt()
tekst_edit = tekst_edit.drop(['variable'], axis = 1)
tekst_edit = tekst_edit.mask(tekst_edit.eq('None')).dropna()
tekst_lista = tekst_edit['value'].values.tolist()
print(tekst_lista)


tagovi_edit = rijeciDF['Tagovi'].str.lower().str.split(expand = True)
tagovi_edit =tagovi_edit.melt()
tagovi_edit = tagovi_edit.drop(['variable'], axis = 1)
tagovi_edit = tagovi_edit.mask(tagovi_edit.eq('None')).dropna()
tagovi_lista = tagovi_edit['value'].values.tolist()
print(tagovi_lista)

naslov_lista.extend(podnaslov_lista)
naslov_lista.extend(tekst_lista)
naslov_lista.extend(tagovi_lista)
print(naslov_lista)

new_list = [
    re.sub(r'[^A-Za-z0-9šŠđĐčČćĆžŽ]+', '', item) for item in naslov_lista
]

stopword = open("stopwords_ex.txt").read().splitlines()
print(stopword)

tokens_without_sw = [word for word in new_list if word not in stopword]
print(tokens_without_sw)

naslov_DF = pd.DataFrame(tokens_without_sw)
naslov_DF.replace('', np.nan, inplace=True)
naslov_DF.dropna(inplace=True)
naslov_counter = naslov_DF.value_counts()

from IPython.display import display
print("\n========= TOP 25 =========\n")
print(naslov_counter[:25])
# isplay(naslov_counter.to_string())
print("\n==========================\n")

naslov_DF.to_csv(r'analiza_rijeci.csv', header=None, index=None, sep=' ', mode='a')

print(naslov_DF)
print(type(naslov_DF))

text = open('analiza_rijeci.csv', 'r').read()
wc = WordCloud(background_color = 'white', max_words= 25, collocations= False, width = 3840, height = 2160)
wc.generate_from_text(text)
process_word = WordCloud().process_text(text)
sort = sorted(process_word.items(), key=lambda e:e[1], reverse=True)
print(sort[:25])
wc.to_file('Word_cloud_eVaraždin.png')

