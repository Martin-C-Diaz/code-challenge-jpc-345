import typer

from app.utils import parse_and_transform


def main(sentence: str = typer.Option("", help="Sentence")):
    print(parse_and_transform(sentence))

typer.run(main)
