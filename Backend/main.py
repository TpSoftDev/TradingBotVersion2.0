import MetaTrader5 as mt

def initialize_mt5():
    """Initialize the MetaTrader 5 platform."""
    if not mt.initialize():
        print("Initialize failed, error code =", mt.last_error())
        return False
    return True

def login_mt5(account_id, password, server):
    """Login to the MetaTrader 5 account."""
    if not mt.login(account_id, password, server):
        print("Login failed, error code =", mt.last_error())
        return False
    return True

def get_symbol_info(symbol):
    """Ensure the symbol is available and return its information."""
    if not mt.symbol_select(symbol, True):
        print(f"Failed to select symbol {symbol}, error code =", mt.last_error())
        return None
    symbol_info = mt.symbol_info(symbol)
    if symbol_info is None or not symbol_info.visible:
        print(f"Symbol {symbol} is not available or not visible, error code =", mt.last_error())
        return None
    return symbol_info

def send_trade_request(symbol, lot, sl_points, tp_points):
    """Send a trade request to buy the specified symbol."""
    symbol_info = get_symbol_info(symbol)
    if symbol_info is None:
        return False

    # Get the current ask price
    symbol_tick = mt.symbol_info_tick(symbol)
    if symbol_tick is None:
        print(f"Failed to get symbol tick for {symbol}, error code =", mt.last_error())
        return False

    # Define the trade request
    request = {
        "action": mt.TRADE_ACTION_DEAL,
        "symbol": symbol,
        "volume": lot,
        "type": mt.ORDER_TYPE_BUY,
        "price": symbol_tick.ask,
        "sl": symbol_tick.ask - sl_points * symbol_info.point,
        "tp": symbol_tick.ask + tp_points * symbol_info.point,
        "comment": "Python Script Buy",
        "type_time": mt.ORDER_TIME_GTC,
        "type_filling": mt.ORDER_FILLING_IOC
    }

    print(f"Sending trade request: {request}")

    # Send the trading request
    result = mt.order_send(request)

    # Check the result
    if result.retcode != mt.TRADE_RETCODE_DONE:
        print(f"Trade failed, retcode={result.retcode}, result={result}, error code={mt.last_error()}")
        return False
    else:
        print(f"Trade successful, order ticket={result.order}")
        return True

def main():
    """Main function to execute the trading script."""
    account_id = 1052460042
    password = 'Cornw@ll7!'
    server = 'FTMO-Demo'
    symbol = "BTCUSD"
    lot = 1.0
    sl_points = 10000  # Example stop loss in points
    tp_points = 20000  # Example take profit in points

    # Initialize and login to MT5
    if not initialize_mt5() or not login_mt5(account_id, password, server):
        mt.shutdown()
        return

    # Send the trade request
    if send_trade_request(symbol, lot, sl_points, tp_points):
        print("Trade executed successfully.")
    else:
        print("Trade execution failed.")

    # Shutdown MT5 connection
    mt.shutdown()

if __name__ == "__main__":
    main()
