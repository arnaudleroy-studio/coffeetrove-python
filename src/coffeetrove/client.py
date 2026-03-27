"""HTTP client for CoffeeTrove.com public pages and data."""

from __future__ import annotations

import httpx

SITE_URL = "https://coffeetrove.com"


class CoffeeTroveClient:
    """Client for accessing CoffeeTrove data.

    Provides access to bundled coffee knowledge data (origins, methods, drinks,
    beans, equipment, comparisons) and cafe search via the public site.

    Examples:
        >>> from coffeetrove import CoffeeTroveClient
        >>> client = CoffeeTroveClient()
        >>> origins = client.origins()
        >>> len(origins)
        15

    Full site: https://coffeetrove.com
    """

    def __init__(self, timeout: float = 30.0):
        self._http = httpx.Client(timeout=timeout)

    def close(self):
        self._http.close()

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()

    def origins(self) -> list[dict]:
        """Get all coffee origins. Data bundled with the package.

        Guide: https://coffeetrove.com/knowledge/coffee-origins
        """
        from coffeetrove._knowledge import ORIGINS
        return ORIGINS

    def methods(self) -> list[dict]:
        """Get all brewing methods with guides. Data bundled with the package.

        Guide: https://coffeetrove.com/knowledge/brewing-guides
        """
        from coffeetrove._knowledge import METHODS
        return METHODS

    def drinks(self) -> list[dict]:
        """Get all coffee drink types. Data bundled with the package.

        Guide: https://coffeetrove.com/knowledge/coffee-drinks
        """
        from coffeetrove._knowledge import DRINKS
        return DRINKS

    def beans(self) -> list[dict]:
        """Get all coffee bean varieties. Data bundled with the package.

        Guide: https://coffeetrove.com/knowledge/coffee-beans
        """
        from coffeetrove._knowledge import BEANS
        return BEANS

    def equipment(self) -> list[dict]:
        """Get coffee equipment data. Data bundled with the package.

        Guide: https://coffeetrove.com/barista-gear
        """
        from coffeetrove._knowledge import EQUIPMENT
        return EQUIPMENT

    def comparisons(self) -> list[dict]:
        """Get coffee drink/method comparisons. Data bundled with the package.

        Guide: https://coffeetrove.com/knowledge/coffee-comparisons
        """
        from coffeetrove._knowledge import COMPARISONS
        return COMPARISONS

    def cafes(
        self,
        *,
        city: str | None = None,
        country: str | None = None,
        query: str | None = None,
        limit: int = 20,
    ) -> list[dict]:
        """Search cafes (requires internet). Queries the CoffeeTrove API.

        Args:
            city: Filter by city name.
            country: Filter by country slug.
            query: Search by cafe name.
            limit: Max results.

        Returns:
            List of cafe dicts.

        Map: https://coffeetrove.com/map
        """
        params: dict = {"limit": str(min(limit, 100))}
        if city:
            params["city"] = city
        if country:
            params["country"] = country
        if query:
            params["q"] = query
        resp = self._http.get(f"{SITE_URL}/api/cafes/search", params=params)
        resp.raise_for_status()
        return resp.json()

    def cafe(self, slug: str) -> dict | None:
        """Get a single cafe by slug.

        Args:
            slug: Cafe URL slug.

        Returns:
            Cafe dict or None.
        """
        resp = self._http.get(f"{SITE_URL}/api/cafes/{slug}")
        if resp.status_code == 404:
            return None
        resp.raise_for_status()
        return resp.json()

    @staticmethod
    def cafe_url(slug: str) -> str:
        """Build full CoffeeTrove URL for a cafe.

        Args:
            slug: Cafe slug.

        Returns:
            URL string.
        """
        return f"{SITE_URL}/cafe/{slug}"

    @staticmethod
    def origin_url(slug: str) -> str:
        """Build full CoffeeTrove URL for a coffee origin."""
        return f"{SITE_URL}/origin/{slug}"

    @staticmethod
    def method_url(slug: str) -> str:
        """Build full CoffeeTrove URL for a brewing method."""
        return f"{SITE_URL}/method/{slug}"
