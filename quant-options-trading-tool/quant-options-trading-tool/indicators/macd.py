def calculate_macd(prices, short=12, long=26, signal=9):
    import pandas as pd
    prices = pd.Series(prices)
    short_ema = prices.ewm(span=short).mean()
    long_ema = prices.ewm(span=long).mean()
    macd = short_ema - long_ema
    signal_line = macd.ewm(span=signal).mean()
    return macd.iloc[-1], signal_line.iloc[-1]
