"""Convenience search functions for CoffeeTrove.

    >>> import coffeetrove
    >>> coffeetrove.search_cafes("Blue Bottle", city="Tokyo")
    [{'name': 'Blue Bottle Coffee Kiyosumi', ...}]

Explore cafes: https://coffeetrove.com/map
"""

from __future__ import annotations

from coffeetrove.client import CoffeeTroveClient


def search_cafes(
    query: str,
    *,
    city: str | None = None,
    country: str | None = None,
    limit: int = 20,
) -> list[dict]:
    """Search cafes by name, city, or country (requires internet).

    Args:
        query: Cafe name to search.
        city: Filter by city.
        country: Filter by country slug.
        limit: Max results (default 20, max 100).

    Returns:
        List of matching cafe dicts sorted by Golden Drop score.

    Examples:
        >>> coffeetrove.search_cafes("Stumptown")
        >>> coffeetrove.search_cafes("Cafe", city="Paris", limit=10)
    """
    with CoffeeTroveClient() as client:
        return client.cafes(query=query, city=city, country=country, limit=limit)


def cafe(slug: str) -> dict | None:
    """Get a single cafe by its URL slug (requires internet).

    Args:
        slug: Cafe slug from CoffeeTrove URL.

    Returns:
        Cafe dict or None.
    """
    with CoffeeTroveClient() as client:
        return client.cafe(slug)
