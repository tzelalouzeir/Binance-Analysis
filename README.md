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

## Output
27 Sep 2023 15:00 UTC+3
```
Analyzing BTC/USDT...
BTC/USDT: Volume drop detected.
After a volume drop, the average change in the 1st and 2nd candles were -0.09% and -0.18%, respectively.

Analyzing ETH/USDT...
ETH/USDT: Volume drop detected.
After a volume drop, the average change in the 1st and 2nd candles were -0.09% and -0.18%, respectively.

Analyzing XRP/USDT...
XRP/USDT: Volume drop detected.
After a volume drop, the average change in the 1st and 2nd candles were 0.12% and 0.13%, respectively.

Analyzing FRONT/USDT...
FRONT/USDT: Volume surge detected.

FRONT/USDT: High volatility detected.

Analyzing TRB/USDT...
TRB/USDT: Volume surge detected.

TRB/USDT: High volatility detected.

TRB/USDT: Overbought conditions detected.

Analyzing BNB/USDT...
BNB/USDT: Volume drop detected.
After a volume drop, the average change in the 1st and 2nd candles were -0.08% and -0.02%, respectively.

Analyzing BLZ/USDT...
BLZ/USDT: High volatility detected.

Analyzing LOOM/USDT...
LOOM/USDT: Volume surge detected.

LOOM/USDT: High volatility detected.

LOOM/USDT: Overbought conditions detected.

Analyzing SOL/USDT...
SOL/USDT: Volume drop detected.
After a volume drop, the average change in the 1st and 2nd candles were -0.24% and -0.52%, respectively.

Analyzing GLMR/USDT...
GLMR/USDT: Volume surge detected.

GLMR/USDT: Overbought conditions detected.

Analyzing BCH/USDT...
BCH/USDT: Volume drop detected.
After a volume drop, the average change in the 1st and 2nd candles were 0.08% and 0.14%, respectively.

Analyzing LUNA/USDT...
LUNA/USDT: Overbought conditions detected.

LUNA/USDT: Volume drop detected.
After a volume drop, the average change in the 1st and 2nd candles were -0.68% and -1.09%, respectively.

Analyzing LINK/USDT...
LINK/USDT: Volume drop detected.
After a volume drop, the average change in the 1st and 2nd candles were 0.12% and 0.23%, respectively.

Analyzing WLD/USDT...
WLD/USDT: Volume drop detected.
After a volume drop, the average change in the 1st and 2nd candles were -0.16% and -0.30%, respectively.

Analyzing AMB/USDT...
AMB/USDT: Volume surge detected.

Analyzing MKR/USDT...
MKR/USDT: Overbought conditions detected.

MKR/USDT: Volume drop detected.
After a volume drop, the average change in the 1st and 2nd candles were 0.21% and 0.17%, respectively.

Analyzing DOGE/USDT...
DOGE/USDT: Volume drop detected.
After a volume drop, the average change in the 1st and 2nd candles were -0.05% and -0.06%, respectively.

Analyzing APT/USDT...
APT/USDT: Volume drop detected.
After a volume drop, the average change in the 1st and 2nd candles were -0.22% and -0.34%, respectively.

Analyzing STORJ/USDT...
STORJ/USDT: Volume surge detected.

Analyzing ARB/USDT...
ARB/USDT: Volume drop detected.
After a volume drop, the average change in the 1st and 2nd candles were -0.22% and -0.44%, respectively.
```
## Contributions

Feel free to contribute to this repository by creating issues or sending pull requests. Any feedback is highly appreciated!

