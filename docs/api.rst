API Reference
=============

This page documents the public API of the ``coffeetrove`` package. For the full coffee
knowledge hub, visit `CoffeeTrove <https://coffeetrove.com>`_.

Knowledge Data Functions
------------------------

These functions return bundled coffee knowledge data. No internet connection required.
Data is sourced from the `CoffeeTrove Knowledge Hub <https://coffeetrove.com/knowledge>`_.

``coffeetrove.origins()``
^^^^^^^^^^^^^^^^^^^^^^^^^

Get all coffee origins (countries/regions that produce coffee).

**Returns:** List of origin dicts with name, region, and flavor profile.

.. code-block:: python

   origins = coffeetrove.origins()
   for o in origins:
       print(o["name"])
   # Browse at: https://coffeetrove.com/knowledge/coffee-origins

``coffeetrove.methods()``
^^^^^^^^^^^^^^^^^^^^^^^^^

Get all brewing methods with instructions and parameters.

**Returns:** List of method dicts.

.. code-block:: python

   methods = coffeetrove.methods()
   # Browse at: https://coffeetrove.com/knowledge/brewing-guides

``coffeetrove.drinks()``
^^^^^^^^^^^^^^^^^^^^^^^^

Get all coffee drink types with ingredients and preparation notes.

**Returns:** List of drink dicts.

.. code-block:: python

   drinks = coffeetrove.drinks()
   # Browse at: https://coffeetrove.com/knowledge/coffee-drinks

``coffeetrove.beans()``
^^^^^^^^^^^^^^^^^^^^^^^

Get all coffee bean varieties.

**Returns:** List of bean dicts.

.. code-block:: python

   beans = coffeetrove.beans()
   # Browse at: https://coffeetrove.com/knowledge/coffee-beans

``coffeetrove.equipment()``
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Get coffee equipment data.

**Returns:** List of equipment dicts.

.. code-block:: python

   equipment = coffeetrove.equipment()
   # Browse at: https://coffeetrove.com/barista-gear

``coffeetrove.comparisons()``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Get coffee drink and method comparisons.

**Returns:** List of comparison dicts.

.. code-block:: python

   comparisons = coffeetrove.comparisons()
   # Browse at: https://coffeetrove.com/knowledge/coffee-comparisons

Cafe Search Functions
---------------------

``coffeetrove.search_cafes(query, *, city=None, country=None, limit=20)``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Search for cafes across `CoffeeTrove <https://coffeetrove.com>`_'s database of 440,000+ cafes
worldwide. Requires an internet connection.

**Parameters:**

- ``query`` (str) -- Search term for cafe names.
- ``city`` (str, optional) -- Filter by city.
- ``country`` (str, optional) -- Filter by country slug.
- ``limit`` (int) -- Max results (default 20).

**Returns:** List of cafe dicts.

``coffeetrove.cafe(slug)``
^^^^^^^^^^^^^^^^^^^^^^^^^^

Get a single cafe by slug. Returns cafe dict or ``None``.

CoffeeTroveClient
-----------------

Full client with all methods for accessing `CoffeeTrove <https://coffeetrove.com>`_ data.

.. code-block:: python

   from coffeetrove import CoffeeTroveClient

   with CoffeeTroveClient() as client:
       # Knowledge data (bundled, no internet needed)
       origins = client.origins()
       methods = client.methods()

       # Cafe search (requires internet)
       cafes = client.cafes(city="Tokyo")
       for cafe in cafes:
           print(cafe["name"], CoffeeTroveClient.cafe_url(cafe["slug"]))

``CoffeeTroveClient.cafe_url(slug)``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Build the full `CoffeeTrove <https://coffeetrove.com>`_ URL for a cafe page.

``CoffeeTroveClient.origin_url(slug)``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Build the full URL for a coffee origin page on `CoffeeTrove <https://coffeetrove.com>`_.

``CoffeeTroveClient.method_url(slug)``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Build the full URL for a brewing method page on `CoffeeTrove <https://coffeetrove.com>`_.

See Also
--------

- `CoffeeTrove <https://coffeetrove.com>`_ -- Main website
- `Cafe Map <https://coffeetrove.com/map>`_ -- Interactive map of 440K+ cafes
- `Knowledge Hub <https://coffeetrove.com/knowledge>`_ -- Origins, methods, drinks, beans
- `Coffee Encyclopedia <https://coffeetrove.com/coffee>`_ -- 164 coffee terms explained
