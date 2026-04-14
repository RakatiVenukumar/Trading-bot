# Binance Futures Testnet Trading Bot

Python CLI-based trading bot for Binance USDT-M Futures Testnet.

## Features

- Place MARKET and LIMIT orders from CLI
- Input validation for symbol, side, type, quantity, and limit price
- Environment-based API key configuration via .env
- Structured logging to console and log file
- Error handling for Binance API and network exceptions

## Project Structure

trading_bot/
	bot/
		__init__.py
		client.py
		orders.py
		validators.py
		logging_config.py
	cli.py
	requirements.txt
	README.md

## Setup Instructions

1. Clone the repository and move into the project folder.

2. Create and activate a virtual environment.

Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

3. Install dependencies.

```powershell
pip install -r requirements.txt
```

4. Create or update .env in the project root with your Binance testnet credentials.

```env
BINANCE_API_KEY=your_key
BINANCE_SECRET_KEY=your_secret
```

## Usage

Run the CLI from the project root:

```powershell
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01
```

LIMIT order example:

```powershell
python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.01 --price 30000
```

## Example Output

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

## Notes

- Use Binance Futures Testnet keys, not production keys.
- Ensure your testnet account has sufficient USDT balance.
- LIMIT orders require --price.
- Logs are written to logs/app.log.
- If you receive credential errors, confirm .env exists in the project root.
