import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget
from PyQt6.QtCore import QTimer
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from bot import BotBinance  # Suponiendo que tienes tu clase BotBinance en un archivo llamado bot.py

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
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
        perc_stopSide= 0.035
        perc_priceSide=0.018
        self.bot = BotBinance(symbol=symbol, asset_primary=asset_primary, asset_secundary=asset_secundary, mode_Soft=mode_Soft, interval="1m", limit=300, sPd=sPd, mPd=mPd, lPd=lPd, perc_binance= perc_binance, perc_stopSide=perc_stopSide, perc_priceSide=perc_priceSide, nbdevup=nbdevup, nbdevdn=nbdevdn)
        
        self.setWindowTitle("Bot de Trading")
        self.setGeometry(100, 100, 1024, 700)

        # Crear instancia de BotBinance

        # Estado del bot
        self.running = False

        # Botones
        self.btn_start = QPushButton("Start bot", self)
        self.btn_start.clicked.connect(self.start_bot)

        self.btn_stop = QPushButton("Stop bot", self)
        self.btn_stop.clicked.connect(self.stop_bot)

        # Etiquetas
        self.label_price = QLabel("Price: ", self)
        self.label_ear = QLabel("Ear: ", self)
        self.label_alerts = QLabel("Alerts: ", self)
        self.label_msg = QLabel("Msg: ", self)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.btn_start)
        layout.addWidget(self.btn_stop)
        layout.addWidget(self.label_price)
        layout.addWidget(self.label_ear)
        layout.addWidget(self.label_alerts)
        layout.addWidget(self.label_msg)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Crear figura de Matplotlib
        self.fig = Figure(figsize=(13, 5), dpi=85)
        self.canvas = FigureCanvas(self.fig)
        layout.addWidget(self.canvas)

    def update_root(self):
        if not self.running:
            return
        closes, upperband, lowerband, smaS, smaM, smaL, print_msg, print_alert, print_ear, print_price_market, candles, price_market, last_price_market = self.bot.update_data()
        
        print(f" [{print_price_market} | {print_ear} | {print_alert}")
        if print_msg !="":
            print(f"{print_msg}")
        
        # Actualizar etiquetas
        self.label_price.setText(f"{price_market}")
        self.label_ear.setText(f"{print_ear}")
        self.label_alerts.setText(f"{print_alert}")
        self.label_msg.setText(f"{print_msg}")

        # Actualizar gráfico de Matplotlib (aquí deberías agregar tu lógica específica)
        # Suponiendo que simplemente limpiamos la figura
        self.fig.clear()
        self.fig = self.bot.update_chart(candles, closes, upperband, lowerband, smaS, smaM, smaL, self.fig)
        # Re-dibujar el canvas
        self.canvas.draw()

        # Llamar a la función de actualización nuevamente después de un tiempo
        QTimer.singleShot(3000, self.update_root)

    def start_bot(self):
        self.running = True
        self.update_root()

    def stop_bot(self):
        self.running = False
        self.label_msg.setText(f"bot stop")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
