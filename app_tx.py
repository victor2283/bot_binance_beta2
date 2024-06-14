from bot import BotBinance
import time
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
perc_priceSide=0.013
bot = BotBinance(symbol=symbol, asset_primary=asset_primary, asset_secundary=asset_secundary, mode_Soft=mode_Soft, interval="1m", limit=300, sPd=sPd, mPd=mPd, lPd=lPd, perc_binance= perc_binance, perc_stopSide=perc_stopSide, perc_priceSide=perc_priceSide, nbdevup=nbdevup, nbdevdn=nbdevdn)

ear = 0
price_market = 0
last_price_market = 0
price_buy = 0
orderId=0
last_order_tradeId =0
sTrade =0
last_trend=""
candles=[]
while True:
    sTrade, last_order_tradeId, last_trend, last_price_market, closes, upperband, lowerband, smaS, smaM, smaL, print_msg, print_alert, print_ear, print_price_market, candles, price_market = bot.update_data(last_trend, last_price_market, last_order_tradeId, sTrade)
    print(f" [{sTrade}] | {print_price_market} | {print_ear} | {print_alert}")
    if print_msg !="":
        print(f"{print_msg}")
    time.sleep(3)
    
