# Binance Futures Demo Trading Bot

Python CLI-based trading bot for Binance USDT-M Futures Demo/Testnet.

## Features

- Place MARKET and LIMIT orders from CLI
- Clean modular architecture (`client`, `orders`, `validators`, `logging_config`)
- Input validation for symbol, side, type, quantity, and limit price
- Environment-based API key configuration through `.env`
- Structured logging to console and `logs/app.log`
- Error handling for Binance API and network exceptions

## Project Structure

```text
bot/
  __init__.py
  client.py
  orders.py
  validators.py
  logging_config.py
cli.py
requirements.txt
README.md
.env
.gitignore
```

## Setup

1. Open terminal in project root.

```powershell
cd C:\PrimeTrade-PythonDev\Trading-bot
```

2. Create and activate virtual environment.

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

3. Install dependencies.

```powershell
pip install -r requirements.txt
```

4. Add demo API keys to `.env`.

```env
BINANCE_API_KEY=your_demo_api_key
BINANCE_SECRET_KEY=your_demo_secret_key
```

## Where To Get Demo API Keys

1. Log in to Binance Demo Futures: `https://demo.binance.com/en/futures/BTCUSDT`
2. Open profile menu and go to API Management
3. Create a new API key (example label: `trading-bot-demo`)
4. Copy API Key and Secret Key
5. Ensure Futures permission is enabled for the key

Use demo keys only. Do not use production keys.

## Usage

Run from project root:

```powershell
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01
```

LIMIT order:

```powershell
python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.01 --price 30000
```

## Expected Output

```text
Order Summary:
Symbol: BTCUSDT
Side: BUY
Type: LIMIT
Quantity: 0.01
Price: 30000

Order Response:
Order ID: 12345678
Status: NEW
Executed Quantity: 0
Average Price: 0

Order placed successfully!
```

## Troubleshooting

- `Missing Binance API credentials`:
  - Confirm `.env` exists in project root and has both keys.
- `insufficient balance` or `Please deposit`:
  - Add demo USDT in Binance Demo Futures wallet/faucet.
- Git shows many warnings from `.venv` files:
  - Keep virtual environments ignored via `.gitignore`.
- Command not found for Python/venv:
  - Activate your venv first, then run `python cli.py ...`.

## Notes

- The bot uses Binance Futures demo endpoint: `https://testnet.binancefuture.com`
- LIMIT orders require `--price`
- Logs are written to `logs/app.log`
