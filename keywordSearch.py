import csv
import pandas as pd
import re
import matplotlib.pyplot as plt
from datetime import date, datetime
import datetime as dt
import matplotlib.dates as mdates
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px



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

#print(keywordDF)
korona_count = len(keywordDF.index)
print("Ukupan broj vijesti za korona tematiku: ", korona_count)


#1. podkategorija = cijepivo

cijepivoDF = keywordDF[(keywordDF['Naslov'].str.contains('.cjepiv.|.Pfizer.|.BionTech.|.Sputnik. V|.AstraZenec.|.Modern.|.Johnson & Johnson.|.simptom. cijepiv.|.cijepljenj.|.raspored.|.treć* doz.', case = False, na = False)) & (keywordDF['Naslov'].str.contains('.Covid.|.koronavirus.|.koron.|.samoizolacij.|.pandemij.|.COVID-19.|.Pfizer.|.BionTech.|.Sputnik V.|.AstraZeneca.', case = False, na = False)) |
                    (keywordDF['Podnaslov'].str.contains('.cjepiv.|.Pfizer.|.BionTech.|.Sputnik. V|.AstraZenec.|.Modern.|.Johnson & Johnson.|.simptom. cijepiv.|.cijepljenj.|.raspored.|.treć* doz.', case = False, na = False)) & (keywordDF['Podnaslov'].str.contains('.Covid.|.koronavirus.|.koron.|.samoizolacij.|.pandemij.|.COVID-19.|.Pfizer.|.BionTech.|.Sputnik V.|.AstraZeneca.', case = False, na = False)) |
                    (keywordDF['Tekst'].str.contains('.cjepiv.|.Pfizer.|.BionTech.|.Sputnik. V|.AstraZenec.|.Modern.|.Johnson & Johnson.|.simptom. cijepiv.|.cijepljenj.|.raspored.|.treć* doz.', case = False, na = False)) & (keywordDF['Tekst'].str.contains('.Covid.|.koronavirus.|.koron.|.samoizolacij.|.pandemij.|.COVID-19.|.Pfizer.|.BionTech.|.Sputnik V.|.AstraZeneca.', case = False, na = False)) |
                    (keywordDF['Link'].str.contains('.cjepiv.|.Pfizer.|.BionTech.|.Sputnik. V|.AstraZenec.|.Modern.|.Johnson & Johnson.|.simptom. cijepiv.|.cijepljenj.|.raspored.|.treć* doz.', case = False, na = False)) & (keywordDF['Link'].str.contains('.Covid.|.koronavirus.|.koron.|.samoizolacij.|.pandemij.|.COVID-19.|.Pfizer.|.BionTech.|.Sputnik V.|.AstraZeneca.', case = False, na = False)) |
                    (keywordDF['Tagovi'].str.contains('.cjepiv.|.Pfizer.|.BionTech.|.Sputnik. V|.AstraZenec.|.Modern.|.Johnson & Johnson.|.simptom. cijepiv.|.cijepljenj.|.raspored.|.treć* doz.', case = False, na = False)) & (keywordDF['Tagovi'].str.contains('.Covid.|.koronavirus.|.koron.|.samoizolacij.|.pandemij.|.COVID-19.|.Pfizer.|.BionTech.|.Sputnik V.|.AstraZeneca.', case = False, na = False))]


cijepivo_count = len(cijepivoDF.index)
print("Ukupan broj vijesti vezanih uz cijepljenje: ", cijepivo_count)

#2. podkategorija = mjere

# df[(df['col_name'].str.contains('apple')) & (df['col_name'].str.contains('banana'))]

mjereDF = keywordDF[(keywordDF['Naslov'].str.contains('.nov* mjer.|.epidemiološk* mjer.|.covid potvrd.|.stožer* civiln* zaštit.|.mask.|.razma.|.kapacitet.|.preporu.|.okupljanj.', case = False, na = False)) & (keywordDF['Naslov'].str.contains('.Covid.|.koronavirus.|.koron.|.samoizolacij.|.pandemij.|.COVID-19.|.Pfizer.|.BionTech.|.Sputnik V.|.AstraZeneca.', case = False, na = False)) |
                    (keywordDF['Podnaslov'].str.contains('.nov* mjer.|.epidemiološk* mjer.|.covid potvrd.|.stožer* civiln* zaštit.|.mask.|.razma.|.kapacitet.|.preporu.|.okupljanj.', case = False, na = False)) & (keywordDF['Podnaslov'].str.contains('.Covid.|.koronavirus.|.koron.|.samoizolacij.|.pandemij.|.COVID-19.|.Pfizer.|.BionTech.|.Sputnik V.|.AstraZeneca.', case = False, na = False)) |
                    (keywordDF['Tekst'].str.contains('.nov* mjer.|.epidemiološk* mjer.|.covid potvrd.|.stožer* civiln* zaštit.|.mask.|.razma.|.kapacitet.|.preporu.|.okupljanj.', case = False, na = False)) & (keywordDF['Tekst'].str.contains('.Covid.|.koronavirus.|.koron.|.samoizolacij.|.pandemij.|.COVID-19.|.Pfizer.|.BionTech.|.Sputnik V.|.AstraZeneca.', case = False, na = False)) |
                    (keywordDF['Link'].str.contains('.nov* mjer.|.epidemiološk* mjer.|.covid potvrd.|.stožer* civiln* zaštit.|.mask.|.razma.|.kapacitet.|.preporu.|.okupljanj.', case = False, na = False)) & (keywordDF['Link'].str.contains('.Covid.|.koronavirus.|.koron.|.samoizolacij.|.pandemij.|.COVID-19.|.Pfizer.|.BionTech.|.Sputnik V.|.AstraZeneca.', case = False, na = False)) |
                    (keywordDF['Tagovi'].str.contains('.nov* mjer.|.epidemiološk* mjer.|.covid potvrd.|.stožer* civiln* zaštit.|.mask.|.razma.|.kapacitet.|.preporu.|.okupljanj.', case = False, na = False)) & (keywordDF['Tagovi'].str.contains('.Covid.|.koronavirus.|.koron.|.samoizolacij.|.pandemij.|.COVID-19.|.Pfizer.|.BionTech.|.Sputnik V.|.AstraZeneca.', case = False, na = False))]

Link = keywordDF['Link']

mjere_count = len(mjereDF.index)
#print("Link: {}".format(Link))
print("Ukupan broj vijesti vezanih uz mjere: ", mjere_count)

#3. podkategorija = broj zarazenih

zarazeniDF = keywordDF[(keywordDF['Naslov'].str.contains('.respirator.|.preminu.|.nov* sluč.|.oporavi.|.aktivn.|.slučaj.|.samoizolacij.', case = False, na = False)) & (keywordDF['Naslov'].str.contains('covid*|koronavirus*|koron*|COVID-19|samoizolacij*|pandemij*|Pfizer*|BionTech|Sputnik V|AstraZeneca', case = False, na = False)) |
                    (keywordDF['Podnaslov'].str.contains('.respirator.|.preminu.|.nov* sluč.|.oporavi.|.aktivn.|.slučaj.|.samoizolacij.', case = False, na = False)) & (keywordDF['Podnaslov'].str.contains('covid*|koronavirus*|koron*|COVID-19|samoizolacij*|pandemij*|Pfizer*|BionTech|Sputnik V|AstraZeneca', case = False, na = False)) |
                    (keywordDF['Tekst'].str.contains('.respirator.|.preminu.|.nov* sluč.|.oporavi.|.aktivn.|.slučaj.|.samoizolacij.', case = False, na = False)) & (keywordDF['Tekst'].str.contains('covid*|koronavirus*|koron*|COVID-19|samoizolacij*|pandemij*|Pfizer*|BionTech|Sputnik V|AstraZeneca', case = False, na = False)) |
                    (keywordDF['Link'].str.contains('.respirator.|.preminu.|.nov* sluč.|.oporavi.|.aktivn.|.slučaj.|.samoizolacij.', case = False, na = False)) & (keywordDF['Link'].str.contains('covid*|koronavirus*|koron*|COVID-19|samoizolacij*|pandemij*|Pfizer*|BionTech|Sputnik V|AstraZeneca', case = False, na = False)) |
                    (keywordDF['Tagovi'].str.contains('.respirator.|.preminu.|.nov* sluč.|.oporavi.|.aktivn.|.slučaj.|.samoizolacij.', case = False, na = False)) & (keywordDF['Tagovi'].str.contains('covid*|koronavirus*|koron*|COVID-19|samoizolacij*|pandemij*|Pfizer*|BionTech|Sputnik V|AstraZeneca', case = False, na = False))]

zarazeni_count = len(zarazeniDF.index)
print("Ukupan broj vijesti vezanih uz broj zarazenih: ", zarazeni_count)

#4. podkategorija = Tko je najviše u medijima

medijiDF = keywordDF[(keywordDF['Naslov'].str.contains('Božinović|Capak|Beroš|Markotić', case = False, na = False)) & (keywordDF['Naslov'].str.contains('covid*|koronavirus*|koron*|COVID-19|samoizolacij*|pandemij*|Pfizer*|BionTech|Sputnik V|AstraZeneca', case = False, na = False)) |
                    (keywordDF['Podnaslov'].str.contains('Božinović|Capak|Beroš|Markotić', case = False, na = False)) & (keywordDF['Podnaslov'].str.contains('covid*|koronavirus*|koron*|COVID-19|samoizolacij*|pandemij*|Pfizer*|BionTech|Sputnik V|AstraZeneca', case = False, na = False)) |
                    (keywordDF['Tekst'].str.contains('Božinović|Capak|Beroš|Markotić', case = False, na = False)) & (keywordDF['Tekst'].str.contains('covid*|koronavirus*|koron*|COVID-19|samoizolacij*|pandemij*|Pfizer*|BionTech|Sputnik V|AstraZeneca', case = False, na = False)) |
                    (keywordDF['Link'].str.contains('Božinović|Capak|Beroš|Markotić', case = False, na = False)) & (keywordDF['Link'].str.contains('covid*|koronavirus*|koron*|COVID-19|samoizolacij*|pandemij*|Pfizer*|BionTech|Sputnik V|AstraZeneca', case = False, na = False)) |
                    (keywordDF['Tagovi'].str.contains('Božinović|Capak|Beroš|Markotić', case = False, na = False)) & (keywordDF['Tagovi'].str.contains('covid*|koronavirus*|koron*|COVID-19|samoizolacij*|pandemij*|Pfizer*|BionTech|Sputnik V|AstraZeneca', case = False, na = False))]

df[df['Kategorija']=='eTV'].count()


mediji_count = len(medijiDF.index)
print("Ukupan broj vijesti vezanih uz medije: ", mediji_count)

neklasificirani_count = korona_count - cijepivo_count - mjere_count - zarazeni_count - mediji_count
klasificirani_count = cijepivo_count + mjere_count + zarazeni_count + mediji_count

print("\nFORMULA:\n")
print(" {} (ukupan broj zapisa)\n-{} (cjepivo)\n-{} (mjere)\n-{} (zarazeni)\n-{} (mediji)\n------------------------------\n{} (neklasificirani)\n{} (uspješno klasificiranih)\n\n".format(korona_count, cijepivo_count, mjere_count, zarazeni_count, mediji_count, neklasificirani_count, klasificirani_count))

kategorije = df['Kategorija'].value_counts()
mmm = keywordDF['Kategorija'].value_counts()

pd_combined = [kategorije, mmm]
result = pd.concat(pd_combined, axis=1)

result.columns=["Ukupno","COVID-19"]
result['COVID-19'] = result['COVID-19'].fillna(0)
result = result.astype({'COVID-19':'int'})

print("TABLIČNI PRIKAZ: \n")
print(result)

result.plot(kind='bar', ylabel='Broj clanaka')
# set the title
plt.title('Usporedba utjecaja COVID-19 na eVarazdin')
plt.tick_params(axis='x', labelrotation=45)
plt.show()

fig = px.bar(result, y=result.index, x=result.columns, text_auto='.2s',
            title="Pregled po kategorijama: Udio COVID-19 objava po kategorijama")

fig.show()








mjeseci = df['Datum'].value_counts()
nnn = keywordDF['Datum'].value_counts()

pd_combined = [mjeseci, nnn]
rezultat = pd.concat(pd_combined, axis=1)
rezultat.index.name = 'Datum'
rezultat.columns=["Ukupno","COVID-19"]
rezultat['COVID-19'] = rezultat['COVID-19'].fillna(0)
rezultat = rezultat.astype({'COVID-19':'int'})
print("TABLIČNI PRIKAZ: \n")
print(rezultat)

rezultat.reset_index()

fig = px.line(rezultat, x=rezultat.index, y=rezultat.columns, title='Udio COVID-19 članaka na sveukupne objave portala eVaraždin ')

fig.update_xaxes(
    rangeslider_visible=True,
    rangeselector=dict(
        buttons=list([
            dict(count=1, label="1m", step="month", stepmode="backward"),
            dict(count=6, label="6m", step="month", stepmode="backward"),
            dict(count=1, label="YTD", step="year", stepmode="todate"),
            dict(count=1, label="1y", step="year", stepmode="backward"),
            dict(step="all")
        ])
    )
)
fig.show()




# initialize data of lists.
novi_data = {'Kategorije': ['Cjepivo', 'Mjere', 'Zarazeni', 'Poznate osobe'],
        'Vrijednosti': [cijepivo_count, mjere_count, zarazeni_count, mediji_count]}

# Create DataFrame
novi_df = pd.DataFrame(novi_data)

# Print the output.
print(novi_df)


fig = px.pie(novi_df, values='Vrijednosti', names='Kategorije',
             title='Usporedba po kategorijama',
             hover_data=['Vrijednosti'], labels={'Vrijednosti':'Ukupan broj članaka'})
fig.update_traces(textposition='inside', textinfo='percent+label')
fig.show()



