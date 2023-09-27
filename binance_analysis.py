import ccxt
import pandas as pd
import pandas_ta as ta

def fetch_ohlcv(exchange, symbol, timeframe='1d'):
    ohlcv = exchange.fetch_ohlcv(symbol, timeframe)
    df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    return df

def volume_surge(df):
    avg_volume = df['volume'].mean()
    latest_volume = df['volume'].iloc[-1]
    return latest_volume > avg_volume * 2

def volatility_index(df):
    atr = ta.atr(df['high'], df['low'], df['close'], length=14)
    latest_atr = atr.iloc[-1]
    return latest_atr > atr.mean() * 1.5

def rsi_divergence(df):
    rsi = ta.rsi(df['close'], length=14)
    latest_rsi = rsi.iloc[-1]
    return (df['close'].iloc[-1] < df['close'].iloc[-2]) and (latest_rsi > rsi.iloc[-2])

def moving_average_crossover(df):
    short_ma = ta.sma(df['close'], length=5)
    long_ma = ta.sma(df['close'], length=20)
    return short_ma.iloc[-1] > long_ma.iloc[-1] and short_ma.iloc[-2] <= long_ma.iloc[-2]

def is_overbought(df):
    rsi = ta.rsi(df['close'], length=14)
    latest_rsi = rsi.iloc[-1]
    return latest_rsi > 70  # Change this threshold as you see fit

def macd_bearish_crossover(df):
    macd_indicators = ta.macd(df['close'])
    return macd_indicators['MACD_12_26_9'].iloc[-1] < macd_indicators['MACDs_12_26_9'].iloc[-1] and macd_indicators['MACD_12_26_9'].iloc[-2] >= macd_indicators['MACDs_12_26_9'].iloc[-2]

def volume_drop(df):
    avg_volume = df['volume'].mean()
    latest_volume = df['volume'].iloc[-1]
    return latest_volume < avg_volume * 1  # Less than half the average volume

def get_top_symbols(exchange, num_symbols=20):
    stable_coins = ['USDT', 'USDC', 'BUSD', 'TUSD', 'PAX', 'DAI','EUR','FDUSD']  # Add more stable coins if needed
    markets = exchange.fetchMarkets()
    symbols = [market['symbol'] for market in markets if '/USDT' in market['symbol'] and market['baseId'] not in stable_coins]
    tickers = exchange.fetch_tickers(symbols)
    sorted_tickers = sorted(tickers.items(), key=lambda x: x[1]['quoteVolume'], reverse=True)
    top_symbols = [ticker[0] for ticker in sorted_tickers[:num_symbols]]
    return top_symbols
    
def analyze_after_volume_drop(df):
    volume_drops = df[df['volume'] < df['volume'].mean()]
    if len(volume_drops) < 2:  # Ensure that you have at least two instances to compare.
        return "Not enough data for volume drop analysis."

    changes_1 = []
    changes_2 = []

    for idx in volume_drops.index:
        if idx + 2 < len(df):  # Make sure the next two candles exist
            close_price = df.loc[idx, 'close']
            next_close_1 = df.loc[idx + 1, 'close']
            next_close_2 = df.loc[idx + 2, 'close']

            changes_1.append((next_close_1 - close_price) / close_price)
            changes_2.append((next_close_2 - close_price) / close_price)

    if not changes_1 or not changes_2:
        return "Not enough data for analysis after volume drop."

    avg_change_1 = sum(changes_1) / len(changes_1)
    avg_change_2 = sum(changes_2) / len(changes_2)

    return f"After a volume drop, the average change in the 1st and 2nd candles were {avg_change_1:.2%} and {avg_change_2:.2%}, respectively.\n"

def main():
    exchange = ccxt.binance()
    top_symbols = get_top_symbols(exchange)

    for symbol in top_symbols:
        print(f"Analyzing {symbol}...")
        df = fetch_ohlcv(exchange, symbol)

        if volume_surge(df):
            print(f"{symbol}: Volume surge detected.\n")
        
        if volatility_index(df):
            print(f"{symbol}: High volatility detected.\n")
        
        if rsi_divergence(df):
            print(f"{symbol}: RSI divergence detected.\n")
        
        if moving_average_crossover(df):
            print(f"{symbol}: Moving average crossover detected.\n")
            
        # New indicators for detecting peak before downturn
        if is_overbought(df):
            print(f"{symbol}: Overbought conditions detected.\n")
            
        if macd_bearish_crossover(df):
            print(f"{symbol}: MACD bearish crossover detected.\n")
            
        if volume_drop(df):
            print(f"{symbol}: Volume drop detected.")
            print(analyze_after_volume_drop(df))
          
if __name__ == "__main__":
    main()
