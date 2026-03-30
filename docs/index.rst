coffeetrove -- Python SDK for CoffeeTrove
==========================================

**coffeetrove** is the official Python SDK for `CoffeeTrove <https://coffeetrove.com>`_, a
specialty coffee platform with data on 440,000+ cafes worldwide, coffee origins, brewing
methods, drinks, bean varieties, equipment, and comparisons.

Use this package to search cafes, explore coffee knowledge data, and build coffee-related
applications with data from `CoffeeTrove <https://coffeetrove.com>`_.

Quick Start
-----------

.. code-block:: python

   import coffeetrove

   # Get coffee origins data
   origins = coffeetrove.origins()
   for origin in origins:
       print(origin["name"], origin["region"])

   # Browse brewing methods
   methods = coffeetrove.methods()

   # Search cafes by city (requires internet)
   from coffeetrove import CoffeeTroveClient
   with CoffeeTroveClient() as client:
       paris_cafes = client.cafes(city="Paris")
       for cafe in paris_cafes:
           print(cafe["name"])

Explore the full cafe map and knowledge hub at `coffeetrove.com <https://coffeetrove.com>`_.

.. toctree::
   :maxdepth: 2
   :caption: Contents

   installation
   api
   knowledge

Links
-----

- **Website**: `coffeetrove.com <https://coffeetrove.com>`_
- **Cafe Map**: `coffeetrove.com/map <https://coffeetrove.com/map>`_
- **Knowledge Hub**: `coffeetrove.com/knowledge <https://coffeetrove.com/knowledge>`_
- **Brewing Guides**: `coffeetrove.com/knowledge/brewing-guides <https://coffeetrove.com/knowledge/brewing-guides>`_
- **Coffee Origins**: `coffeetrove.com/knowledge/coffee-origins <https://coffeetrove.com/knowledge/coffee-origins>`_
- **PyPI**: `pypi.org/project/coffeetrove/ <https://pypi.org/project/coffeetrove/>`_
- **GitHub**: `github.com/arnaudleroy-studio/coffeetrove-python <https://github.com/arnaudleroy-studio/coffeetrove-python>`_

Indices and tables
------------------

* :ref:`genindex`
* :ref:`search`
