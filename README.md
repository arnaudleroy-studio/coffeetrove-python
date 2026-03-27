# coffeetrove

Python SDK for [CoffeeTrove.com](https://coffeetrove.com) -- explore 440,000+ cafes, coffee origins, brewing methods, beans, and specialty coffee data worldwide.

## Install

```bash
pip install coffeetrove
```

For pandas DataFrame support:

```bash
pip install coffeetrove[pandas]
```

## Quick Start

```python
import coffeetrove

# Find cafes in any city
paris_cafes = coffeetrove.cafes("Paris", limit=5)
print(paris_cafes[0]["name"])

# Search cafes by name
results = coffeetrove.search_cafes("Blue Bottle", city="Tokyo")

# Coffee origins with flavor profiles
origins = coffeetrove.origins()
ethiopia = [o for o in origins if o["slug"] == "ethiopia"][0]
print(ethiopia["flavor_profile"])

# Brewing methods with step-by-step guides
methods = coffeetrove.methods()

# Coffee drinks with nutritional info
drinks = coffeetrove.drinks()

# Bean varieties
beans = coffeetrove.beans()

# Equipment and gear
gear = coffeetrove.equipment()
```

## Using the Client

For more control, use `CoffeeTroveClient` directly:

```python
from coffeetrove import CoffeeTroveClient

with CoffeeTroveClient() as client:
    # Search cafes with multiple filters
    cafes = client.cafes(city="Melbourne", limit=20)

    # Get cafes by country
    japan_cafes = client.cafes(country="japan", limit=50)

    # Count cafes
    total = client.count_cafes()
    print(f"Total cafes: {total:,}")  # Total cafes: 440,000+

    # Count by country
    france = client.count_cafes(country="france")
    print(f"Cafes in France: {france:,}")

    # Get all coffee comparisons
    comparisons = client.comparisons()
```

## Pandas DataFrames

```python
import coffeetrove

# Cafes as DataFrame
df = coffeetrove.cafes("London", limit=100, as_dataframe=True)
print(df[["name", "city", "score"]].describe())

# Origins as DataFrame
origins_df = coffeetrove.origins(as_dataframe=True)
```

## Data Available

| Data | Count | Description |
|------|-------|------------|
| Cafes | 440,000+ | Name, address, coordinates, score, hours, chain type |
| Origins | 15+ | Growing regions with altitude, flavor, harvest data |
| Brewing Methods | 15+ | Step-by-step guides with grind, temp, ratio |
| Drinks | 17+ | Ingredients, caffeine, calories |
| Beans | 23+ | Species, origin, flavor notes, processing |
| Equipment | 15+ | Category, price range, difficulty |
| Comparisons | 17+ | Side-by-side drink and method analysis |

## Golden Drop Score

Every cafe has a score (0-100) based on data completeness, reviews, and chain type. Independent cafes receive a +10 bonus. [Learn more](https://coffeetrove.com/about).

## Links

- [CoffeeTrove.com](https://coffeetrove.com) -- Main site
- [Cafe Map](https://coffeetrove.com/map) -- Interactive map of 440K cafes
- [Knowledge Hub](https://coffeetrove.com/knowledge) -- Brewing guides, origins, drinks
- [Brewing Tools](https://coffeetrove.com/tools) -- Ratio calculator, grind guide, timer
- [Magazine](https://coffeetrove.com/magazine) -- Coffee culture articles

## License

MIT
