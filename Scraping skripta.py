'''Ova skripta skrapuje odredjenu tabelu sa sajta, tabelu cuva u csv fajl, zatim vizuelizuje live grafik'''


import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import requests
import time

# Putanja do CSV fajla(KORISNIK UNOSI)
file_path = r"C:\Users\Korisnik\Desktop\DataAnalyst\Python\Podaci-za-analizu\CSV-za-vjezbu\CC-python-pandas-matplotlib-master\worldometer.csv"  # Promeniti putanju do željene lokacije za čuvanje CSV fajla

# URL adresa sajta sa kojeg se preuzimaju podaci(KORISNIK UNOSI)
url = "https://www.worldometers.info/world-population/"

def fetch_data():
    response = requests.get(url)
    if response.status_code == 200:
        return pd.read_html(response.content)[0]  # Promenite indeks ukoliko je potrebno da biste dobili pravu tabelu(KORISNIK UNOSI)
    else:
        print("Greška prilikom preuzimanja podataka.")
        return None

def update_csv():
    data = fetch_data()
    if data is not None:
        # Snimanje podataka u CSV fajl
        data.to_csv(file_path, index=False)
        print("Podaci su ažurirani u CSV fajlu:", file_path)
    else:
        print("Nema podataka.")

def update_graph(frame):
    # Učitavanje podataka iz CSV fajla
    data = pd.read_csv(file_path)
    
    # Crtanje grafikona (KORISNIK BIRA VRSTU GRAFIKONA I VARIJABLE)
    plt.cla()
    plt.style.use('fivethirtyeight') #Korisnik bira stil
    plt.plot(data['Year  (July 1)'], data['Population'], label='Population')
    plt.title('World Population Over Time')
    plt.xlabel('Year')
    plt.ylabel('Population')
    plt.legend(loc='upper left')

# Pokretanje animacije
ani = FuncAnimation(plt.gcf(), update_graph, interval=5000, cache_frame_data=False)  # interval u milisekundama (ovde svakih 5 sekundi)

# Osvežavanje CSV fajla svakih 5 sekundi
while True:
    update_csv()
    update_graph(None)  # Poziv funkcije za ažuriranje grafikona
    plt.show()          # Prikazivanje grafikona
    time.sleep(5)

plt.tight_layout()
plt.show()
