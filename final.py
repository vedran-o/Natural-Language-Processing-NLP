import urllib.request, sys, time
from random import randint

# Pandas
import pandas as pd

# Sleep
from time import sleep

# Beautiful Soup
from bs4 import BeautifulSoup
import requests

# Originalni CSV
import csv

# Time - benmarch
import time
from datetime import date, datetime



start_time = time.time()
pagesToGet = 1
n = 0
stranica = 1
link_stranica = 0

# Identifikator za linkove ( redni broj pronalaska linka )
pozicija = 1

# Hip str
hip_str = ''

# Odos
pos = 0

# Datum
date_pocetni = ''
year = 0
month = 0
day = 0
ex = 0
pointer = False
pos = 0
rucni_unos = True
url_1 = ''
ext = 0
unos = 0
automatic = False
# Popis linkova

"""
eTV:                        https://evarazdin.hr/etv/
Crna kronika:               https://evarazdin.hr/crna-kronika/
Sport:                      https://evarazdin.hr/sport/
Politika:                   https://evarazdin.hr/politika/
Našim krajem:               https://evarazdin.hr/nasim-krajem/

Magazin
   U središtu:              https://evarazdin.hr/magazin/sredistu/
   Druga Hrvatska:          https://evarazdin.hr/magazin/druga-hrvatska/
   Intervjui:               https://evarazdin.hr/magazin/intervjui/
   Kolumne:                 https://evarazdin.hr/magazin/kolumne/
   Zabava:                  https://evarazdin.hr/magazin/zabava/
   Lifestyle:               https://evarazdin.hr/magazin/lifestyle/
"""


# MENI
print("======================================================")
print("=========================MENI=========================")
print("======================================================")

# Logic out - meni
while( n <= 0):
    print("\nMolim Vas unesite broj stranica koje želite 'scrapaty': ")
    n = int(input())

    if (n <= 0):
        print("Krivi unos stranice\n")

while( year <= 2018 and month <= 0 and day <= 0 ):
    year = int(input('Godina: '))
    month = int(input('Mjesec: '))
    day = int(input('Dan: '))

    d = date(year, month, day)

    # datetime.datetime.strptime(d, '%Y-%m-%d').strftime('%d/%m/%y')
    print(d)

print(date_pocetni)

# Prepoznaje error u linku na mojoj sekvenci te ga onda ne sprema u csv ali ga prepoznaje kao unikatan link
# Crna kronika nema takvog linka

with open('eVarazdin_lifestyle.csv', 'w', encoding='utf8', newline='') as f:
    thewriter = csv.writer(f)
    header = ['Naslov', 'Podnaslov', 'Tekst', 'Autor', 'Fotograf', 'Link', 'Datum', 'Objava', 'Kategorija', 'Tagovi', 'Broj_slika']
    thewriter.writerow(header)

    while pos < 100:

        print("\nPopis linkova za 'scrapanje': ")
        print("1)  eTV:              https://evarazdin.hr/etv/")
        print("2)  Crna kronika:     https://evarazdin.hr/crna-kronika/")
        print("3)  Sport:            https://evarazdin.hr/sport/")
        print("4)  Politika:         https://evarazdin.hr/politika/")
        print("5)  Našim krajem:     https://evarazdin.hr/nasim-krajem/")
        print("6)  U središtu:       https://evarazdin.hr/magazin/sredistu/")
        print("7)  Druga Hrvatska:   https://evarazdin.hr/magazin/druga-hrvatska/")
        print("8)  Intervjui:        https://evarazdin.hr/magazin/intervjui/")
        print("9)  Kolumne:          https://evarazdin.hr/magazin/kolumne/")
        print("10)  Zabava:           https://evarazdin.hr/magazin/zabava/")
        print("11)  Lifestyle:        https://evarazdin.hr/magazin/lifestyle/")
        print("(12)  IZLAZ IZ PROGRAMA")
        print("(13) AUTOMATSKI")

        pos = int(input('Odaberi link: '))

        if pos == '1':
            url_1 = 'https://evarazdin.hr/etv/'

        elif pos == 2:
            url_1 = 'https://evarazdin.hr/crna-kronika/'

        elif pos == 3:
            url_1 = 'https://evarazdin.hr/sport/'

        elif pos == 4:
            url_1 = 'https://evarazdin.hr/politika/'

        elif pos == 5:
            url_1 = 'https://evarazdin.hr/nasim-krajem/'

        elif pos == 6:
            url_1 = 'https://evarazdin.hr/magazin/sredistu/'

        elif pos == 7:
            url_1 = 'https://evarazdin.hr/magazin/druga-hrvatska/'

        elif pos == 8:
            url_1 = 'https://evarazdin.hr/magazin/intervjui/'

        elif pos == 9:
            url_1 = 'https://evarazdin.hr/magazin/kolumne/'

        elif pos == 10:
            url_1 = 'https://evarazdin.hr/magazin/zabava/'

        elif pos == 11:
            url_1 = 'https://evarazdin.hr/magazin/lifestyle/'

        elif pos == 12:
            exit()

        else:
            automatic = True
            url_1 = 'https://evarazdin.hr/etv/'

        print("Odabrali ste {} stranice za scraping!\n".format(n))

        for i in range(pagesToGet, pagesToGet + n):

            # url = 'https://evarazdin.hr/opcine-i-gradovi/varazdinske-toplice/?page={}'.format(i)
            url = '{}?page={}'.format(url_1, i)

            # print(url)

            page = requests.get(url)

            soup = BeautifulSoup(page.text, 'html.parser')
            frame = []
            links = soup.find_all('a', attrs={'class': 'pp'}, href=True) + soup.find_all('a', attrs={'class': 'pp.pp-sided'},
                                                                                         href=True) + soup.find_all('a', attrs={
                'class': 'pp.pp-big'}, href=True)

            # Debug 0
            # print("Pronađeno je {} unikatnih linkova!".format(len(links)))
            # print("Staranica [{}]".format(pagesToGet))

            # Ispis pronađenih linkova

            print("===============================================================================\n")

            for link in links:

                datumIKategorija = link.find('div', attrs={'class': 'pp-date'}).text.strip()
                splitano = datumIKategorija.split("-")
                datum = splitano[0]
                kategorija = splitano[1]

                datum_prerada = datum.split('.')
                datum_d = int(datum_prerada[0])
                datum_m = int(datum_prerada[1])
                datum_g = int(datum_prerada[2])

                datum_object = date(datum_g, datum_m, datum_d)

                if datum_object <= d:
                    break

                # Stranica
                if ( link_stranica == 16 ):
                    stranica = stranica + 1

                # Link na stranici
                if ( link_stranica % 16 == 0 and link_stranica != 0 ):
                    link_stranica = int(link_stranica / 16)

                else:
                    link_stranica = link_stranica + 1

                print("Ukupno pronađenih linkova: {}\nTrenutna stranica [{}] te pozicija linka na stranici [{}]\nPoveznica na članak: {}".format(pozicija, stranica, link_stranica, link['href']))
                pozicija = pozicija + 1

                Link = link['href']

                naslov = link.find('h3', attrs={'class': 'pp-title'}).text.strip().replace(chr(160), " ").replace('Foto - ', '').replace('Foto čitatelja - ', '').replace('eTV studio: ', '').replace('eTV - ', '').replace('eTV/ ', '').replace('VIDEO: ', '').replace('Video - ', '').replace('eTV i ', '').replace('eTV, ', '').replace('eTV i foto - ', '').replace('eTV: ', '').replace('eTV Studio: ', '').replace('eTV  - ', '').replace('eTV  studio: ', '').replace('Video: ', '').replace('foto - ', '').replace('eTV Studio: ', '').replace('Video čitatelja - ', '').replace('eTV Studio - ', '').replace('eTV -', '').replace('Video, Foto: ', '').replace('Foto -', '').replace('Županijski ', '').replace('Županija: ', '').replace('Čehokova lista: ', '').replace('Čehok: ', '').replace('Velika fotogalerija - ', '').replace('U ', '').replace('Stričak: ', '').replace('SDP: ', '').replace('Reformisti: ', '').replace('eTV | GLEDAJTE I GLASUJTE - ','').replace('eTV | ', '').replace('eTV- ', '').replace('eTV/FOTO: ', '').replace('eTV|  ', '').replace('eTV|FOTO ', '').replace('»', '').replace('«', '')

                # Debug 1
                # print("{}. {}".format(poz, naslov))

                # Skipanje error na vrijednosti None
                try:
                    podnaslov = link.find('div', attrs={'class': 'pp-headline'}).text.strip().replace("'", "").replace(chr(160), " ").lower()
                except AttributeError:
                    podnaslov = " "

                try:
                    broj_slika = link.find('span', attrs={'class': 'badge-text'}).text.strip()
                except AttributeError:
                    broj_slika = "0"

                # Dubina
                url_novi = Link
                page_novi = requests.get(url_novi)
                soup_novi = BeautifulSoup(page_novi.text, 'html.parser')

                try:
                    objava = soup_novi.find('div', attrs={'class': 'pd-date'}).text.strip()
                    objava = objava[-5:]
                except AttributeError:
                    objava = "Nedostupna"

                try:
                    autor = soup_novi.find('strong').text.strip().replace("Foto:", "").replace("poslovne biografije.", "").replace('Djed Mraz ni ove godine nije zaboravio na djecu u prigradskim mjesnim odborima. Već od danas, 12. prosinca, pa do petka 16. prosinca 2022. godine, Djed Mraz će svojim vozilom obići prigradska naselja i obradovati djecu.', '').replace('U eTV studiju danas je gostovao Zdenko Đuras, novi predsjednik Gradskog vijeća Grada Ivanca i prvi čovjek HDZ-a u tom gradu oko čijeg se izbora nedavno ujedinila cijela oporba.', '').replace('Policijski službenici Policijske postaje Varaždin dovršili su kriminalističko istraživanje nad 50-godišnjakom, zbog sumnje da je počinio kazneno djelo pronevjere.', '').replace('Foto:', '').replace('U prometnoj nesreći koja se dogodila jučer, 3. svibnja oko 15.40 sati na državnoj cesti D-3 u Presečnom ozlijeđena je jedna osoba.', '').replace('Kao što smo već izvijestili, jučer je oko 19.20 sati u Varaždinu u prometnoj  nesreći ozlijeđena jedna osoba, odnosno policijski službenik.', '').replace('Policijski službenici Policijske uprave varaždinske dovršili su kriminalističko istraživanje nad 50-godišnjakinjom, zbog sumnje da je počinila kazneno djelo Zlouporaba položaja i ovlasti.', '').replace('U prometnoj nesreći koja se dogodila u srijedu, 8. lipnja oko 0.15 sati u Bombellesovoj cesti u Varaždinu, ozlijeđena je 23-godišnjakinja.', '')
                    if autor == "Zadnja izmjena:":
                        autor = " "
                except AttributeError:
                    autor = " "

                try:
                    # Dodano micanje NBSP znaka; ASCII ID = 160
                    tekst = soup_novi.find('div', attrs={'class': 'pd-content'}).text.strip().replace(chr(160), " ")
                except AttributeError:
                    tekst = " "

                try:
                    tagovi = soup_novi.find('div', attrs={'class': 'pd-tags'}).text.strip().replace('#', "")
                except AttributeError:
                    tagovi = " "


                try:
                    # Dodano ".capitalize()" - Problem kod grupiranja podataka npr. ( arhiva i Arhiva )
                    fotograf = soup_novi.find('p', attrs={'class': 'pd-image-author'}).text.strip()
                    fotograf = fotograf[6:].capitalize()

                except AttributeError:
                    fotograf = " "


                # Debug 2
                # print("Autor clanka je: {}\nTekst clanka: {}\nTagovi clanka su: {}\n".format(autor, tekst, tagovi))
                print("Naslov clanka: {}\nPodnaslov clanka: {}\nDatum objave {}\n".format(naslov, podnaslov, datum))

                sleep(0.2)
                info = [naslov, podnaslov, tekst, autor, fotograf, Link, datum, objava, kategorija, tagovi, broj_slika]
                thewriter.writerow(info)
                sleep(0.4)

                print("===============================================================================\n")

        datum_object = 0
        ex = 0
        ext = 1
        pagesToGet = 0

    # Dimenzija vremena; Runtime

    time_s = round((time.time() - start_time),2)
    print("Runtime: {} sekundi\n".format(time_s))
    print("===============================================================================\n")

