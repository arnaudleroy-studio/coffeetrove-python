"""
coffeetrove - Python SDK for CoffeeTrove.com specialty coffee data.

Explore 440,000+ cafes worldwide, coffee origins, brewing methods,
specialty drinks, bean varieties, and more.

    >>> import coffeetrove
    >>> cafes = coffeetrove.cafes("Paris")
    >>> cafes[0]["name"]
    'Cafe de Flore'

    >>> origins = coffeetrove.origins()
    >>> methods = coffeetrove.methods()

Full site: https://coffeetrove.com
Knowledge hub: https://coffeetrove.com/knowledge
"""

__version__ = "0.1.0"
__author__ = "CoffeeTrove"
__url__ = "https://coffeetrove.com"

from coffeetrove.client import CoffeeTroveClient
from coffeetrove.data import (
    cafes,
    origins,
    methods,
    drinks,
    beans,
    equipment,
    comparisons,
)
from coffeetrove.search import search_cafes, cafe

__all__ = [
    "CoffeeTroveClient",
    "cafes",
    "origins",
    "methods",
    "drinks",
    "beans",
    "equipment",
    "comparisons",
    "search_cafes",
    "cafe",
]
