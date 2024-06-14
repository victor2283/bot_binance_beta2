El archivo app_tk tiene tkinter y entorno grafico con los indicadores tecnicos, app_tx 
tiene unicamente prints de informacion sin grafica
siendo mas compatible con servers externos para usarlo 24/7, todos los codigos que 
hacen procesamiento de datos como creacion de velas
y dar informacion de las indicadores estan en el archivo bot.py
El modo de uso es muy facil en windows en consola escriba py app_tk.py o py app_tx.py y
el programa lo guiara en todo lo demas, los dos archivos ejecutables tienen las variables donde 
debe cambiar parametros para el par en el que trabajara por ejemplo btc_try o btc_usdt como
tambien cualquier otro tipo de par como xrp_usdc, etc. la manera de crearlo es poner en
asset_primary = "BTC" y asset_secundary="USDC", EL orden de estas dos variables es importante
porque si coloca al revez no le funcionara por eso debe consultar en binance que pares estan
disponibles en el orden que muestra esto puede hacerlo facilmente mirando en la direccion url
de trading spot. Para que el programa de python funcione debe instalar el conector de binance
de python como lo indica la documentacion de binance y previamente gestionar su token de
acceso que debe reemplazar en el archivo config.py

La estrategia que usa este programa, basado en la tendencia que detectan las velas heilin ashi 
detecta puntos de entrada y salida y al confirmar realiza compra o venta si estan en el margen de 
ganancia mayor a la comision de binance, tiene un metodo de cancelacion de ordenes por si el
precio baja o sube que se activa si la tendencia detectada cambia repentinamente para tomar precios
mas baratos para la compra y precios mas altos para la venta y ademas compra dentro de los limites
de las bandas de bollinger por lo que cuando detecta el precio mas bajo crea una orden a un
precio mas alto para que cuando la tendencia cambia a alcista la orden sea tomada y para la venta 
crea la orden de venta cuando el precio llega a su maximo en las bandas a un precio mas bajo 
porque todo lo que sube tiene que bajar. En el caso de compra o venta si la tendencia cambia por 
ejemplo si el precio sigue subiendo en venta la orden es cancelada y si hizo una orden de compra 
y el precio baja repentimanete la orden se cancela automaticamente.



