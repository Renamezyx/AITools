"""CLI commands for AITools"""
import os
import time

import typer
from AITools import __logo__, __version__, __author__
from rich.progress import track, Console
from AITools.config.loader import get_config_path, save_config
from AITools.config.schema import Config

console = Console()
app = typer.Typer(
    name="AITools",
    help=f"{__logo__} AITools - Personal AI Assistant",
    no_args_is_help=True
)


@app.command()
def hello(name: str):
    print(f"Hello {name}")


@app.command()
def goodbye(name: str, formal: bool = False):
    if formal:
        print(f"Goodbye Ms. {name}. Have a good day.")
    else:
        print(f"Bye {name}!")


@app.command()
def speed():
    total = 0
    for value in track(range(100), description="Processing..."):
        # Fake processing time
        time.sleep(0.01)
        total += 1
    print(f"Processed {total} things.")


@app.command()
def init():
    """初始化配置"""
    config = Config()
    if os.path.exists(get_config_path()):
        if not typer.confirm(f"Are you sure to init the config?"):
            return 0
    else:
        os.makedirs(os.path.dirname(get_config_path()), exist_ok=True)
    save_config(config)
    console.print(f"\n{__logo__} aitools is ready!")
    console.print("\nNext steps:")
    console.print("  1. Add your API key to [cyan]~/.aitools/config.json[/cyan]")
    console.print("  2. Chat: [cyan]aitools agent -m \"Hello!\"[/cyan]")


@app.command()
def agent(message: str = typer.Option(None, "--message", "-m", help="Message to send to the agent")):
    console.log(message)


if __name__ == '__main__':
    app()
