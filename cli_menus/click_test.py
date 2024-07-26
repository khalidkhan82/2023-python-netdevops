# hello.py

import click

Options = {"option 1": "blue",
        "option 2": "green",
        "option 3": "yellow"}

value = click.prompt('Please choose option', type=click.Choice(Options.keys()))
@click.command("hello")
@click.version_option("0.1.0", prog_name="hello")
#@click.argument("options", type=click.Choice(Options.keys()))
def hello():
    click.echo("Hello, World!")

if __name__ == "__main__":
    hello()