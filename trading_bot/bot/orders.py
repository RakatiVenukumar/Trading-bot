from typing import Any, Dict, Optional

from bot.client import BinanceClient


def place_order(
	symbol: str,
	side: str,
	type: str,
	quantity: float,
	price: Optional[float] = None,
) -> Dict[str, Any]:
	"""Place a Futures order on Binance Testnet and return structured output."""
	client = BinanceClient().instance

	order_params: Dict[str, Any] = {
		"symbol": symbol.upper(),
		"side": side.upper(),
		"type": type.upper(),
		"quantity": float(quantity),
	}

	if order_params["type"] == "MARKET":
		response = client.futures_create_order(**order_params)
	elif order_params["type"] == "LIMIT":
		order_params["price"] = str(price)
		order_params["timeInForce"] = "GTC"
		response = client.futures_create_order(**order_params)
	else:
		raise ValueError("Unsupported order type. Use MARKET or LIMIT.")

	return {
		"success": True,
		"request": {
			"symbol": order_params["symbol"],
			"side": order_params["side"],
			"type": order_params["type"],
			"quantity": order_params["quantity"],
			"price": order_params.get("price"),
		},
		"order": {
			"order_id": response.get("orderId"),
			"status": response.get("status"),
			"executed_qty": response.get("executedQty"),
			"avg_price": response.get("avgPrice"),
		},
		"raw_response": response,
	}
