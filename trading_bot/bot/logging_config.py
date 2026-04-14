import logging
from pathlib import Path


def setup_logging(logger_name: str = "trading_bot", level: int = logging.INFO) -> logging.Logger:
    """Configure and return an application logger.

    Logs are written to logs/app.log and also emitted to the console.
    """
    logs_dir = Path("logs")
    logs_dir.mkdir(parents=True, exist_ok=True)

    logger = logging.getLogger(logger_name)
    logger.setLevel(level)

    # Prevent duplicate handlers when setup is called multiple times.
    if logger.handlers:
        return logger

    formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")

    file_handler = logging.FileHandler(logs_dir / "app.log", encoding="utf-8")
    file_handler.setLevel(level)
    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    logger.propagate = False

    return logger
