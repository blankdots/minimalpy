MinimalPy
=========

An example of a minimal Python 3.6+ project that contains an web application built with `aiohttp <http://aiohttp.readthedocs.io/>`_.
At the same time the project exemplifies:

* aiohttp server;
* logging formatting;
* unit tests;
* `tox automation <https://tox.readthedocs.io>`_ for:

  * `flake8 <http://flake8.pycqa.org/en/latest/>`_ style enforcement;
  * running unit tests and coverage;

* `travis <https://travis-ci.org/blankdots/minimalpy.svg?branch=master>`_ and `coveralls <https://coveralls.io/github/blankdots/minimalpy>`_ integration
* building documentation for `readthedocs <https://minimalpy.readthedocs.io>`_.


Install and Run
---------------

Installation can be done:

* Github - without cloning

.. code-block:: console

    $ pip install git+https://github.com/blankdots/minimalpy.git

* cloning repository:

.. code-block:: console

    $ git clone git@github.com:blankdots/minimalpy.git
    $ cd minimalpy
    $ pip install .


After install the application can be started like: `$ minimal`

Tests and Documentation
-----------------------

In order to run the tests: `$ tox` in the root directory of the git project.

To build documentation locally:

.. code-block:: console

    $ cd docs
    $ make html


Structure
---------

Following a similar structure as described in: `Structuring Your (Python) Project <https://docs.python-guide.org/writing/structure/>`_.
Main application resides in `minimalpy` folder, documentation in `docs` and unit tests in `tests`.

.. code-block:: console

    .
    ├── minimalpy
    │   ├── __init__.py
    │   └── server.py
    ├── data
    │   └── data.json
    ├── docs
    │   ├── conf.py
    │   ├── index.rst
    │   └── Makefile
    ├── LICENSE
    ├── README.md
    ├── readthedocs.yml
    ├── requirements.txt
    ├── setup.py
    ├── tests
    │   ├── conftest.py
    │   ├── coveralls.py
    │   ├── __init__.py
    │   ├── requirements.txt
    │   └── test_server.py
    └── tox.ini


Similar Projects
----------------

Some projects similar in scope:

* https://github.com/pypa/sampleproject
* https://github.com/kennethreitz/samplemod
