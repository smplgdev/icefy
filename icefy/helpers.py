from rich.console import Console

console = Console()
err_console = Console(stderr=True)


def print_warning(message: str):
    console.print(message, style="yellow")


def comma_to_dot(value: str) -> float:
    return float(value.replace(",", "."))
