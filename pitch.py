import click
import random
import sys

products = [
    "your new hot cryptocurrency",
    "your new frontend JavaScript framework",
    "your new AI home assistant",
    "your new VR-based social network",
    "your new cross-platform mobile framework (this one's going to work guys!)",
    "your new smart home product which doesn't let you control your home's lights or temperature",
    "your new fancy monthly subscription service (like Trunk Club or Birchbox)",
    "your new way to deploy web applications that's better than serverless *and* Docker"
]

audiences = [
    "the queen of England",
    "the judges of Shark Tank (/ Dragon's Den)",
    "actor Keanu Reeves",
    "Amelia Earheart (p.s. you found her frozen at the North Pole and just thawed her out, Captain America-style, so you've got a lot of explaining to do)",
    "Colombian singing sensation Shakira",
    "the anesthesiologist putting you under before your (group) appendectomy",
    "Charlie and his brother from the \"Charlie bit my finger\" video",
    "yourselves, but 10 years ago"
]

def shuffle_and_pop():
    """Chooses a pairing and removes it from the lists"""
    # Shuffle the lists at runtime
    random.shuffle(products)
    random.shuffle(audiences)

    # Pick a product and an audience
    product = products.pop()
    audience = audiences.pop()

    click.echo('\n🏁  YOUR CHALLENGE 🏁\n')
    click.secho('Pitch...\n', bold=True)

    click.echo(product)

    click.secho('\nto...\n', bold=True)

    click.echo(audience + '\n')

    if click.confirm("(press any key to continue...)"):
        pass

@click.command()
def choose():
    """Chooses a random audience and topic"""
    click.echo("🚨  AWWWW YEAAAAA IT'S PITCH TIME 🚨\n")

    if not click.confirm('Ready?'):
        sys.exit(0)

    while len(products) > 0:
            shuffle_and_pop()

    click.echo('No more topics!')

if __name__ == '__main__':
    choose()
