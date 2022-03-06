import os
import click

@click.group()
def entrypoint(*opts):
    if args:
        args_used_count: int = 0
        for a in opts:
            if a == "--version" or a == "-V":
                click.echo("""
                    mkproj:
                        version: 0.1.3_(0.13)
                        codename: \"WTF\"
                """)
        return "0"
    else:
        raise ValueError

@entrypoint.command()
def forPython3():
    click.echo('Hello Python!')

@entrypoint.command()
def forJava():
    click.echo('Hello Java!')

@entrypoint.command()
def forC():
    click.echo('Hello C!')

@entrypoint.command()
def forCpp():
    click.echo('Hello C++!')

@entrypoint.command()
def forC():
    click.echo('Hello Node!')

if __name__== '__main__':
    entrypoint()