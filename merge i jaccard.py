from configparser import Interpolation
import glob
from matplotlib.pyplot import axis
import pandas as pd
import re
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
from sklearn.metrics import jaccard_score


path = 'WordFrequency' 
all_files = glob.glob(path + "/*.csv")

#print(all_files)

lista = []
for filename in all_files:
    df = pd.read_csv(filename, index_col= None, header= 0)
    ime =re.sub("[^0-9-]","",filename)
    df['razdbolje'] = ime
    lista.append(df)

df = pd.concat(lista, axis = 0, ignore_index= True)
df.to_csv("Frekvencije_mjesecno.csv")

#print(lista)
for csv in lista:
    for csv2 in lista:
        print(csv.iloc[:,0])
        print("Drugi: ")
        print(csv2.iloc[:,0])
        print(jaccard_score(csv.iloc[:,0], csv2.iloc[:,0], average= "micro"))
