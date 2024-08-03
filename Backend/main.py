import MetaTrader5 as mt

def main():
    # Initialize MT5
    mt.initialize()
    mt.login(105098537, 'Cornw@ll246!', 'Trading.comMarkets-MT5')

    # get all symbols
    symbols = mt.symbols_get()
    print('Symbols: ', symbols)


    #symbol = "BTC/USD"
    #lot = 0.1


    #request = {
    #    "action": mt.TRADE_ACTION_DEAL,
    #    "symbol": symbol,
    #   "volume": lot,
    #    "type": mt.ORDER_TYPE_BUY,
    #    "price": mt.symbol_info_tick(symbol).ask,
    #    "sl": 1.06695,
    #    "tp": 1.09695,
    #    "comment": 'Pyhon Script Buy',
    #    "type_time": mt.ORDER_TIME_GTC,
    #    "type_filling": mt.ORDER_FILLING_IOC
    #}

    # send a trading request
    #result = mt.order_send(request)



if __name__ == "__main__":
    main()