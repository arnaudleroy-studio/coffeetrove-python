Coffee Knowledge
================

The ``coffeetrove`` package includes bundled coffee knowledge data sourced from the
`CoffeeTrove Knowledge Hub <https://coffeetrove.com/knowledge>`_. This data is included
in the package and does not require an internet connection.

Coffee Origins
--------------

15 coffee-producing origins with region, flavor profiles, and growing conditions.

.. code-block:: python

   origins = coffeetrove.origins()
   for o in origins:
       print(o["name"], o.get("region"))

Browse all origins at `coffeetrove.com/knowledge/coffee-origins <https://coffeetrove.com/knowledge/coffee-origins>`_.

Brewing Methods
---------------

Comprehensive brewing method guides with parameters, instructions, and equipment needed.

.. code-block:: python

   methods = coffeetrove.methods()
   pour_overs = [m for m in methods if "pour" in m["name"].lower()]

Browse all methods at `coffeetrove.com/knowledge/brewing-guides <https://coffeetrove.com/knowledge/brewing-guides>`_.

Coffee Drinks
-------------

Coffee drink recipes and descriptions, from espresso to specialty drinks.

.. code-block:: python

   drinks = coffeetrove.drinks()

Browse all drinks at `coffeetrove.com/knowledge/coffee-drinks <https://coffeetrove.com/knowledge/coffee-drinks>`_.

Bean Varieties
--------------

Coffee bean varieties with tasting notes and characteristics.

.. code-block:: python

   beans = coffeetrove.beans()

Browse all beans at `coffeetrove.com/knowledge/coffee-beans <https://coffeetrove.com/knowledge/coffee-beans>`_.

Equipment
---------

Coffee equipment data including grinders, brewers, and accessories.

.. code-block:: python

   equipment = coffeetrove.equipment()

Browse equipment at `coffeetrove.com/barista-gear <https://coffeetrove.com/barista-gear>`_.

Comparisons
-----------

Side-by-side comparisons of drinks and brewing methods.

.. code-block:: python

   comparisons = coffeetrove.comparisons()

Browse comparisons at `coffeetrove.com/knowledge/coffee-comparisons <https://coffeetrove.com/knowledge/coffee-comparisons>`_.

Cafe Data
---------

The package also provides access to `CoffeeTrove <https://coffeetrove.com>`_'s database
of 440,000+ cafes worldwide via the ``CoffeeTroveClient``:

.. code-block:: python

   from coffeetrove import CoffeeTroveClient

   with CoffeeTroveClient() as client:
       # Search by city
       paris = client.cafes(city="Paris")

       # Search by country
       japan = client.cafes(country="japan")

       # Search by name
       blue_bottle = client.cafes(query="Blue Bottle")

Explore the interactive map at `coffeetrove.com/map <https://coffeetrove.com/map>`_.
