from typing import Annotated

import typer

from icefy import ICE, Task


app = typer.Typer()
ice = ICE()

@app.command()
def init():
    
    if ice.is_initialized():
        print_warning(f"Warning: 'ice.json' already exists at '{ice.path.absolute()}'. Aborting...")
    
    else:
        ice.create()
        # ice_file.write_text(json.dumps({}, indent=4))  # Create empty JSON
        print(f"Successfully initialized {ice.file_name} at '{ice.path.absolute()}'.")

@app.command()
def add(
    task: Annotated[str, typer.Option("-t", "--task", help="Describe the task to add", prompt=True)],
    impact: Annotated[str, typer.Option("-i", "--impact", help="Impact of the task (1-10)", prompt=True, callback=comma_to_dot)],
    confidence: Annotated[str, typer.Option("-c", "--confidence", help="Confidence in the task (1-10)", prompt=True, callback=comma_to_dot)],
    ease: Annotated[str, typer.Option("-e", "--ease", help="Ease of the task (1-10)", prompt=True, callback=comma_to_dot)],
):
    ice.add_task(
        Task(
            text=task,
            impact=impact,  # type: ignore
            confidence=confidence,  # type: ignore
            ease=ease  # type: ignore
        )
    )

if __name__ == "__main__":
    app()
