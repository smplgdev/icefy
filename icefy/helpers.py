import logging
from rich.logging import RichHandler


def comma_to_dot(value: str) -> float:
    return float(value.replace(",", "."))


def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(message)s",
        handlers=[RichHandler(
            show_level=False,
            show_path=False,
            show_time=False
        )]
    )
