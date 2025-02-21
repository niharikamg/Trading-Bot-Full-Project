# Automated Trading Bot (Crypto/Stocks)

## Features
- Fetch **live price data** from Binance/Yahoo Finance.
- Implements **technical indicators** (EMA, RSI, MACD).
- **Backtest strategy** using Backtrader.
- Supports **live trade execution** on Binance.
- **Automated bot** runs 24/7 checking market conditions.
- **Flask API** to remotely execute trades.

## Setup Instructions
1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
2. Fetch live price data:
   ```
   python fetch_live_data.py
   ```
3. Test trading indicators:
   ```
   python technical_indicators.py
   ```
4. Backtest strategy:
   ```
   python backtest_strategy.py
   ```
5. Execute a test trade (CAUTION: Ensure API keys are set):
   ```
   python execute_trade.py
   ```
6. Start the automated trading bot:
   ```
   python auto_trading_bot.py
   ```
7. Run Flask API for remote trading:
   ```
   python trading_api.py
   ```

🚀 **Happy Trading! Always backtest before live trading!** 🛠
