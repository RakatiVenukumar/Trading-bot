import click

from bot.orders import place_order
from bot.validators import (
	validate_order_type,
	validate_price_for_limit,
	validate_quantity,
	validate_side,
	validate_symbol,
)


@click.command()
@click.option("--symbol", required=True, type=str, help="Trading pair symbol (e.g., BTCUSDT)")
@click.option("--side", required=True, type=str, help="Order side: BUY or SELL")
@click.option("--type", "order_type", required=True, type=str, help="Order type: MARKET or LIMIT")
@click.option("--quantity", required=True, type=float, help="Order quantity")
@click.option("--price", required=False, type=float, default=None, help="Order price (required for LIMIT)")
def main(symbol: str, side: str, order_type: str, quantity: float, price: float) -> None:
	"""CLI entry point for placing Binance Futures Testnet orders."""
	try:
		validated_symbol = validate_symbol(symbol)
		validated_side = validate_side(side)
		validated_order_type = validate_order_type(order_type)
		validated_quantity = validate_quantity(quantity)
		validated_price = validate_price_for_limit(validated_order_type, price)

		result = place_order(
			symbol=validated_symbol,
			side=validated_side,
			type=validated_order_type,
			quantity=validated_quantity,
			price=validated_price,
		)

		if not result.get("success"):
			error = result.get("error", {})
			message = error.get("message", "Unknown error")
			raise click.ClickException(message)

		request = result.get("request", {})
		order = result.get("order", {})

		click.echo("Order Summary:")
		click.echo(f"Symbol: {request.get('symbol')}")
		click.echo(f"Side: {request.get('side')}")
		click.echo(f"Type: {request.get('type')}")
		click.echo(f"Quantity: {request.get('quantity')}")
		click.echo(f"Price: {request.get('price') or 'N/A'}")
		click.echo("")
		click.echo("Order Response:")
		click.echo(f"Order ID: {order.get('order_id')}")
		click.echo(f"Status: {order.get('status')}")
		click.echo(f"Executed Quantity: {order.get('executed_qty')}")
		click.echo(f"Average Price: {order.get('avg_price')}")
		click.echo("")
		click.echo("Order placed successfully!")
	except ValueError as exc:
		raise click.ClickException(str(exc)) from exc


if __name__ == "__main__":
	main()
