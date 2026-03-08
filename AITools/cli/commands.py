"""CLI commands for AITools"""
import typer
from AITools import __logo__, __version__, __author__
app = typer.Typer(
    name="AITools",
    help=f"{__logo__} AITools - Personal AI Assistant",
    no_args_is_help= True
)

