Installation
============

Install from PyPI
-----------------

.. code-block:: bash

   pip install coffeetrove

With pandas support (for DataFrame output):

.. code-block:: bash

   pip install coffeetrove[pandas]

Requirements
------------

- Python 3.9 or later
- ``httpx`` (installed automatically)
- ``pandas`` (optional, for DataFrame output)

Install from Source
-------------------

.. code-block:: bash

   git clone https://github.com/arnaudleroy-studio/coffeetrove-python.git
   cd coffeetrove-python
   pip install -e .

Verify Installation
-------------------

.. code-block:: python

   import coffeetrove
   print(coffeetrove.__version__)  # 0.1.0

   # Quick test -- list coffee origins
   origins = coffeetrove.origins()
   print(len(origins))  # 15

   # Browse brewing methods
   methods = coffeetrove.methods()
   for m in methods:
       print(m["name"])

Explore the full coffee knowledge hub at `coffeetrove.com/knowledge <https://coffeetrove.com/knowledge>`_.
