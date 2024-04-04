import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from IPython.display import display, clear_output
from matplotlib.animation import FuncAnimation
import time

# Prvo, definirajte funkciju za crtanje grafikona
def plot_live_graph(frame):
    plt.clf()  # Očisti prethodni grafikon
    sns.lineplot(x='percent_change', y='values', hue='name', data=frame, markers=True)
    plt.tight_layout()  # Dodajemo ovu liniju za bolji raspored elemenata na grafikonu

# Zatim, ažurirajte podatke u DataFrameu i ponovno nacrtajte grafikon
def update_graph(i):
    # Ovdje ažurirajte podatke u df7 prema potrebi
    pd.set_option('display.float_format', lambda x: '%.5f' % x)
    df = pd.read_csv(r'C:\Users\Korisnik\Desktop\DataAnalyst\Python\Podaci-za-analizu\CSV-za-vjezbu\CC-python-pandas-matplotlib-master\API.csv')
    df3 = df.groupby('name', sort=False)[['quote.USD.percent_change_1h','quote.USD.percent_change_24h','quote.USD.percent_change_7d','quote.USD.percent_change_30d','quote.USD.percent_change_60d','quote.USD.percent_change_90d']].mean()
    df4 = df3.stack()
    df5 = df4.to_frame(name='values') 
    df6 = df5.reset_index()
    df7 = df6.rename(columns={'level_1': 'percent_change'})
    df7['percent_change'] = df7['percent_change'].replace(['quote.USD.percent_change_1h','quote.USD.percent_change_24h','quote.USD.percent_change_7d','quote.USD.percent_change_30d','quote.USD.percent_change_60d','quote.USD.percent_change_90d'],['1h','24h','7d','30d','60d','90d'])
    
    # Prikazivanje grafikona
    plot_live_graph(df7)

# Stvorite animaciju
fig = plt.figure(figsize=(10, 6))
ani = FuncAnimation(fig, update_graph, interval=60000)  # 60 sekundi

plt.show()

