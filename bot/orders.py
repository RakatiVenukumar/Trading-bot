from typing import Any, Dict, Optional

from binance.exceptions import BinanceAPIException, BinanceRequestException
from requests.exceptions import RequestException

from bot.client import BinanceClient
from bot.logging_config import setup_logging


logger = setup_logging(__name__)


def place_order(
	symbol: str,
	side: str,
	type: str,
	quantity: float,
	price: Optional[float] = None,
) -> Dict[str, Any]:
	"""Place a Futures order on Binance Testnet and return structured output."""
	try:
		client = BinanceClient().instance

		order_params: Dict[str, Any] = {
			"symbol": symbol.upper(),
			"side": side.upper(),
			"type": type.upper(),
			"quantity": float(quantity),
		}

		logger.info(
			"Placing futures order: symbol=%s side=%s type=%s quantity=%s",
			order_params["symbol"],
			order_params["side"],
			order_params["type"],
			order_params["quantity"],
		)

		if order_params["type"] == "MARKET":
			response = client.futures_create_order(**order_params)
		elif order_params["type"] == "LIMIT":
			order_params["price"] = str(price)
			order_params["timeInForce"] = "GTC"
			logger.info("Limit order price=%s timeInForce=%s", order_params["price"], order_params["timeInForce"])
			response = client.futures_create_order(**order_params)
		else:
			raise ValueError("Unsupported order type. Use MARKET or LIMIT.")

		logger.info(
			"Order API response: orderId=%s status=%s executedQty=%s avgPrice=%s",
			response.get("orderId"),
			response.get("status"),
			response.get("executedQty"),
			response.get("avgPrice"),
		)

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
	except BinanceAPIException as exc:
		logger.exception("Binance API error while placing order: %s", exc)
		return {
			"success": False,
			"error": {
				"type": "BinanceAPIException",
				"message": str(exc),
				"code": getattr(exc, "code", None),
			},
		}
	except (BinanceRequestException, RequestException) as exc:
		logger.exception("Network/request error while placing order: %s", exc)
		return {
			"success": False,
			"error": {
				"type": "NetworkError",
				"message": str(exc),
			},
		}
	except Exception as exc:
		logger.exception("Unexpected error while placing order: %s", exc)
		return {
			"success": False,
			"error": {
				"type": "UnexpectedError",
				"message": str(exc),
			},
		}
