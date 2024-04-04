import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from IPython.display import display, clear_output
from matplotlib.animation import FuncAnimation
import time

# Prvo, definirajte funkciju za crtanje grafikona
def plot_live_graph(frame):
    plt.cla()  # Očisti postojeći grafikon
    plt.style.use('fivethirtyeight')
    sns.lineplot(x='quote.USD.last_updated', y='quote.USD.price',hue='name', data=frame)

    y_min = frame['quote.USD.price'].min()
    plt.fill_between(frame['quote.USD.last_updated'], y_min, frame['quote.USD.price'], color='skyblue', alpha=0.3, interpolate=True)

    plt.xticks(rotation=45, fontsize=7)
    plt.tight_layout()

# Zatim, ažurirajte podatke u DataFrameu i ponovno nacrtajte grafikon
def update_graph(i):
    # Ovdje ažurirajte podatke u df7 prema potrebi
    df = pd.read_csv(r'C:\Users\Korisnik\Desktop\DataAnalyst\Python\Podaci-za-analizu\CSV-za-vjezbu\CC-python-pandas-matplotlib-master\API1.csv')
    df.set_index('name', inplace=True)
    df3 = df.loc['SingularityNET',['quote.USD.last_updated', 'quote.USD.price']]
    df4 = pd.DataFrame(df3)
   
    # Prikazivanje grafikona
    plot_live_graph(df4)

# Stvorite animaciju
fig = plt.figure(figsize=(10, 6))
ani = FuncAnimation(fig, update_graph, interval=60000, save_count=10)  # 60 sekundi, save_count=10

plt.show()

