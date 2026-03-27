"""Convenience data loaders for CoffeeTrove.

    >>> import coffeetrove
    >>> origins = coffeetrove.origins()
    >>> methods = coffeetrove.methods()
    >>> paris = coffeetrove.cafes("Paris", limit=5)

Explore more: https://coffeetrove.com/knowledge
"""

from __future__ import annotations

from coffeetrove._knowledge import (
    ORIGINS, METHODS, DRINKS, BEANS, EQUIPMENT, COMPARISONS,
)


def _to_dataframe(rows: list[dict]):
    try:
        import pandas as pd
        return pd.DataFrame(rows)
    except ImportError:
        raise ImportError(
            "pandas is required for DataFrame output. "
            "Install with: pip install coffeetrove[pandas]"
        )


def cafes(
    city: str | None = None,
    *,
    country: str | None = None,
    query: str | None = None,
    limit: int = 20,
    as_dataframe: bool = False,
):
    """Search 440,000+ cafes worldwide (requires internet).

    Args:
        city: Filter by city name.
        country: Filter by country slug (e.g., 'france', 'japan').
        query: Search by cafe name.
        limit: Max results (default 20, max 100).
        as_dataframe: Return pandas DataFrame.

    Returns:
        List of cafe dicts sorted by Golden Drop score.

    Map: https://coffeetrove.com/map
    """
    from coffeetrove.client import CoffeeTroveClient
    with CoffeeTroveClient() as client:
        rows = client.cafes(city=city, country=country, query=query, limit=limit)
    return _to_dataframe(rows) if as_dataframe else rows


def origins(*, as_dataframe: bool = False):
    """15 coffee-growing origins with flavor profiles, altitude, and regions.

    Returns:
        List of origin dicts.

    Examples:
        >>> origins = coffeetrove.origins()
        >>> [o["name"] for o in origins[:3]]
        ['Brazil Cerrado', 'Colombia Huila', 'Costa Rica Tarrazu']

    Guide: https://coffeetrove.com/knowledge/coffee-origins
    """
    return _to_dataframe(ORIGINS) if as_dataframe else list(ORIGINS)


def methods(*, as_dataframe: bool = False):
    """15 brewing methods with brew time, difficulty, and equipment.

    Returns:
        List of method dicts.

    Examples:
        >>> methods = coffeetrove.methods()
        >>> [m["name"] for m in methods[:3]]
        ['AeroPress', 'Auto Drip Machine', 'Chemex']

    Guide: https://coffeetrove.com/knowledge/brewing-guides
    """
    return _to_dataframe(METHODS) if as_dataframe else list(METHODS)


def drinks(*, as_dataframe: bool = False):
    """17 coffee drink types with ingredients and caffeine content.

    Returns:
        List of drink dicts.

    Examples:
        >>> drinks = coffeetrove.drinks()
        >>> [d["name"] for d in drinks[:3]]
        ['Affogato', 'Americano', 'Cappuccino']

    Guide: https://coffeetrove.com/knowledge/coffee-drinks
    """
    return _to_dataframe(DRINKS) if as_dataframe else list(DRINKS)


def beans(*, as_dataframe: bool = False):
    """23 coffee bean varieties with species, tasting notes, and altitude.

    Returns:
        List of bean dicts.

    Guide: https://coffeetrove.com/knowledge/coffee-beans
    """
    return _to_dataframe(BEANS) if as_dataframe else list(BEANS)


def equipment(*, as_dataframe: bool = False):
    """15 coffee equipment items with category and price range.

    Returns:
        List of equipment dicts.

    Guide: https://coffeetrove.com/barista-gear
    """
    return _to_dataframe(EQUIPMENT) if as_dataframe else list(EQUIPMENT)


def comparisons(*, as_dataframe: bool = False):
    """17 coffee drink and method comparisons.

    Returns:
        List of comparison dicts.

    Guide: https://coffeetrove.com/knowledge/coffee-comparisons
    """
    return _to_dataframe(COMPARISONS) if as_dataframe else list(COMPARISONS)
