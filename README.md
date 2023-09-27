# Binance Analysis with CCXT

This repository houses Python code that utilizes the `ccxt` library to fetch OHLCV (Open, High, Low, Close, Volume) data for various cryptocurrency pairs from Binance. The data is then subjected to a series of technical analyses to identify key patterns and indicators which can be useful for traders.

## Features

1. **Fetching OHLCV Data**: Fetches the OHLCV data of a cryptocurrency pair from Binance.
2. **Multiple Technical Analyses**: The code runs a series of technical analyses on the fetched data, such as:
    - Volume Surge Detection
    - Volatility Index Calculation
    - RSI Divergence Detection
    - Moving Average Crossover Analysis
    - Overbought Condition Check
    - MACD Bearish Crossover Detection
    - Volume Drop Detection and Analysis
3. **Top Symbols Filtering**: The code fetches the top cryptocurrency pairs based on their trading volume against USDT.

## Installation

Make sure you have the following Python packages installed:

- `ccxt`
- `pandas`
- `pandas_ta`

You can install them using `pip`:

```bash
pip install ccxt pandas pandas_ta
```

## Usage

1. Clone this repository.
2. Navigate to the repository's root directory in your terminal.
3. Run the code using the following command:

```bash
python <filename>.py
```

Replace `<filename>` with the name you've saved the provided code as.

The script will fetch the top cryptocurrency pairs from Binance and run them through various technical analyses, printing detected patterns and indicators for each pair.

## Functions Breakdown

- `fetch_ohlcv`: Fetches OHLCV data for a given pair and timeframe.
- `volume_surge`: Detects if the latest volume is significantly higher than the average volume.
- `volatility_index`: Checks if the latest ATR (Average True Range) is much higher than the average ATR.
- `rsi_divergence`: Detects RSI divergence.
- `moving_average_crossover`: Identifies short and long SMA crossovers.
- `is_overbought`: Checks if a cryptocurrency pair is overbought based on its RSI.
- `macd_bearish_crossover`: Identifies bearish crossovers in MACD.
- `volume_drop`: Checks if the latest volume is significantly lower than the average volume.
- `get_top_symbols`: Fetches the top traded pairs based on quote volume against USDT.
- `analyze_after_volume_drop`: Analyzes the price change after a volume drop.
- `main`: The main function that ties all the other functions together.

## Contributions

Feel free to contribute to this repository by creating issues or sending pull requests. Any feedback is highly appreciated!

