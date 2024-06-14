from bot import BotBinance
from tkinter import messagebox
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from pprint import pprint

mode_Soft=1 # modo 0 como demo - modo 1 produccion con datos reales
asset_primary = "BTC"
asset_secundary="TRY"
symbol = asset_primary + asset_secundary
perc_binance = 0.167
sPd = 9
mPd = sPd * 2
lPd = mPd * 3
nbdevup= 2
nbdevdn=2
perc_stopSide= 0.03
perc_priceSide=0.01
bot = BotBinance(symbol=symbol, asset_primary=asset_primary, asset_secundary=asset_secundary, mode_Soft=mode_Soft, interval="1m", limit=300, sPd=sPd, mPd=mPd, lPd=lPd, perc_binance= perc_binance, perc_stopSide=perc_stopSide, perc_priceSide=perc_priceSide, nbdevup=nbdevup, nbdevdn=nbdevdn)

ear = 0
price_market = 0
last_price_market = 0
price_buy = 0
orderId=0
last_order_tradeId =0
sTrade =0
last_trend=""


running = False  # Estado del bot
candles=[]

# Crear la ventana principal
root = tk.Tk()
root.title("Bot de Trading")
root.geometry("1024x700")  # Ajustar el tamaño de la ventana

# Crear frames para organización
frame_top = tk.Frame(root)
frame_top.pack(pady=10)
frame_middle = tk.Frame(root)
frame_middle.pack(pady=10)
frame_bottom = tk.Frame(root)
frame_bottom.pack(pady=10)

def update_root():
    global fig, canvas, candles, price_market, last_price_market, ear, last_order_tradeId, sTrade, last_trend, symbol, nbdevup, nbdevdn, asset_primary, asset_secundary, perc_stopSide, perc_priceSide, mode_Soft, perc_binance 
    if not running:
        return
    
    sTrade, last_order_tradeId, last_trend, last_price_market, closes, upperband, lowerband, smaS, smaM, smaL, print_msg, print_alert, print_ear, print_price_market, candles, price_market = bot.update_data(last_trend, last_price_market, last_order_tradeId, sTrade)
                                                                                                                                                                                                      
    print(f" [{sTrade}] | {print_price_market} | {print_ear} | {print_alert}")
    if print_msg !="":
        print(f"{print_msg}")
    
    # Actualizar etiquetas
    color = "green" if price_market > last_price_market else "red"
    label_0_price.config(text= f" [{sTrade}] {print_price_market} ", fg=color)
    label_1_ear.config(text= print_ear )
    label_2_alerts.config(text=print_alert)
    label_3_msg.config(text= print_msg, fg=color)    
    fig.clear()
    fig = bot.update_chart(candles, closes, upperband, lowerband, smaS, smaM, smaL, fig)
    canvas.draw()
    # Actualizar gráfico
    root.after(3000, update_root)  # Actualizar cada 3000 ms 
    
def start_bot():
    global running
    running = True
    update_root()

def stop_bot():
    global running
    running = False
    messagebox.showinfo("Stop Bot..", "bot status = stop.")

button_0_start = tk.Button(frame_top, text="Start bot", command=start_bot)
button_0_start.grid(row=0, column=0,  columnspan=3, padx=3)
label_0_price = tk.Label(frame_top, text="Price: ", font=("Arial", 14))
label_0_price.grid(row=0, column=3, columnspan=3, pady=3)
button_1_stop = tk.Button(frame_top, text="Stop Bot", command=stop_bot)
button_1_stop.grid(row=0, column=6, columnspan=3, padx=3)

# Crear widgets

label_1_ear = tk.Label(frame_top, text="Ear: ", font=("Arial", 13))
label_1_ear.grid(row=1, column=1, columnspan=3, pady=3)
label_2_alerts = tk.Label(frame_top, text="Alerts: ", font=("Arial", 12))
label_2_alerts.grid(row=1, column=6, columnspan=3, pady=3)
label_3_msg = tk.Label(frame_top, text="Msg: ", font=("Arial", 12))
label_3_msg.grid(row=2, column=3, columnspan=3, pady=3)

# Crear la figura de Matplotlib con un tamaño mayor
fig = Figure(figsize=(13, 5), dpi=85) # Aumentar el tamaño de la figura

# Crear el lienzo de Matplotlib para Tkinter
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()

# Iniciar la aplicación
root.mainloop()
