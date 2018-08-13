## Minimal Python Project

[![Build Status](https://travis-ci.org/blankdots/minimalpy.svg?branch=master)](https://travis-ci.org/blankdots/minimalpy)
[![Coverage Status](https://coveralls.io/repos/github/blankdots/minimalpy/badge.svg?branch=master)](https://coveralls.io/github/blankdots/minimalpy?branch=master)
[![Documentation Status](https://readthedocs.org/projects/minimalpy/badge/?version=latest)](https://minimalpy.readthedocs.io/en/latest/?badge=latest)

An example of a minimal Python 3.6+ project that contains an web application built with [aiohttp](http://aiohttp.readthedocs.io/).
At the same time the project exemplifies:
* aiohttp server;
* logging formatting;
* unit tests;
* [tox automation](https://tox.readthedocs.io) for:
  * [flake8](http://flake8.pycqa.org/en/latest/) style enforcement;
  * running unit tests and coverage;
* [travis](https://travis-ci.org/blankdots/minimalpy.svg?branch=master) and [coveralls](https://coveralls.io/github/blankdots/minimalpy) integration;
* building documentation for [readthedocs](https://minimalpy.readthedocs.io).

### Install and Run

Installation can be done:
* Github - without cloning
```
$ pip install git+https://github.com/blankdots/minimalpy.git
```
* cloning repository:
```
$ git clone git@github.com:blankdots/minimalpy.git
$ cd minimalpy
$ pip install .
```

After install the application can be started like: `$ minimal`

#### Tests and Documentation

In order to run the tests: `$ tox` in the root directory of the git project.

To build documentation locally:
```
$ cd docs
$ make html
```

###  Structure

Following a similar structure as described in: [Structuring Your (Python) Project](https://docs.python-guide.org/writing/structure/).
Main application resides in `minimalpy` folder, documentation in `docs` and unit tests in `tests`.

```
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
```

### Similar Projects

Some projects similar in scope:

* https://github.com/pypa/sampleproject
* https://github.com/kennethreitz/samplemod
