from typing import Optional


VALID_SIDES = {"BUY", "SELL"}
VALID_ORDER_TYPES = {"MARKET", "LIMIT"}


def validate_symbol(symbol: str) -> str:
    """Validate that symbol is a non-empty string."""
    if not isinstance(symbol, str):
        raise ValueError("Symbol must be a string.")

    cleaned_symbol = symbol.strip().upper()
    if not cleaned_symbol:
        raise ValueError("Symbol cannot be empty.")

    return cleaned_symbol


def validate_side(side: str) -> str:
    """Validate order side is BUY or SELL."""
    if not isinstance(side, str):
        raise ValueError("Side must be a string.")

    cleaned_side = side.strip().upper()
    if cleaned_side not in VALID_SIDES:
        raise ValueError("Side must be BUY or SELL.")

    return cleaned_side


def validate_order_type(order_type: str) -> str:
    """Validate order type is MARKET or LIMIT."""
    if not isinstance(order_type, str):
        raise ValueError("Type must be a string.")

    cleaned_order_type = order_type.strip().upper()
    if cleaned_order_type not in VALID_ORDER_TYPES:
        raise ValueError("Type must be MARKET or LIMIT.")

    return cleaned_order_type


def validate_quantity(quantity: float) -> float:
    """Validate quantity is a positive number."""
    if not isinstance(quantity, (int, float)):
        raise ValueError("Quantity must be a number.")

    numeric_quantity = float(quantity)
    if numeric_quantity <= 0:
        raise ValueError("Quantity must be greater than 0.")

    return numeric_quantity


def validate_price_for_limit(order_type: str, price: Optional[float]) -> Optional[float]:
    """Validate that price is provided and valid for LIMIT orders."""
    if order_type == "LIMIT":
        if price is None:
            raise ValueError("Price is required for LIMIT orders.")

        if not isinstance(price, (int, float)):
            raise ValueError("Price must be a number.")

        numeric_price = float(price)
        if numeric_price <= 0:
            raise ValueError("Price must be greater than 0.")

        return numeric_price

    return None
