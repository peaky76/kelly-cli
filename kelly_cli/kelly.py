import click
from pybet import Odds
from pybet.staking import kelly as pykelly


@click.command()
@click.option(
    "-d",
    "--decimal",
    "odds_type",
    flag_value="decimal",
    default=True,
    help="interpret inputs as decimal odds (default)",
)
@click.option(
    "-p",
    "--prob",
    "odds_type",
    flag_value="prob",
    help="interpret inputs as probabilities",
)
@click.option(
    "-c",
    "--percent",
    "odds_type",
    flag_value="percent",
    help="interpret inputs as percentages",
)
@click.argument("true_odds", type=click.FLOAT)
@click.argument("market_odds", type=click.FLOAT)
@click.option(
    "-b", "--bank", default=100, help="the size of betting bank (default 100)"
)
def kelly(odds_type, true_odds, market_odds, bank):

    constructor = {
        "decimal": Odds,
        "prob": Odds.probability,
        "percent": Odds.percentage,
    }[odds_type]

    stake = pykelly(constructor(true_odds), constructor(market_odds), bank)
    color = "bright_green" if stake > 0 else "red"
    click.secho(f"£{round(stake, 2)}", fg=color)
