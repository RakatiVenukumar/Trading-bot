import os
from typing import Optional

from binance.client import Client
from dotenv import load_dotenv

from bot.logging_config import setup_logging


class BinanceClient:
    """Wrapper around python-binance Client for Futures Testnet usage."""

    TESTNET_FUTURES_URL = "https://testnet.binancefuture.com"

    def __init__(self, api_key: Optional[str] = None, secret_key: Optional[str] = None) -> None:
        self.logger = setup_logging(__name__)

        load_dotenv()

        self.api_key = api_key or os.getenv("BINANCE_API_KEY")
        self.secret_key = secret_key or os.getenv("BINANCE_SECRET_KEY")

        if not self.api_key or not self.secret_key:
            error_message = "Missing Binance API credentials. Set BINANCE_API_KEY and BINANCE_SECRET_KEY in .env"
            self.logger.error(error_message)
            raise ValueError(error_message)

        self._client = self._initialize_client()

    def _initialize_client(self) -> Client:
        """Initialize python-binance client against Futures Testnet."""
        try:
            client = Client(api_key=self.api_key, api_secret=self.secret_key)
            client.FUTURES_URL = self.TESTNET_FUTURES_URL
            self.logger.info("Binance Futures Testnet client initialized successfully")
            return client
        except Exception as exc:
            self.logger.exception("Failed to initialize Binance client: %s", exc)
            raise

    @property
    def instance(self) -> Client:
        """Return the initialized python-binance Client instance."""
        return self._client
