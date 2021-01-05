## Minimal Python Project

![Integration Tests](https://github.com/blankdots/minimalpy/workflows/Integration%20Tests/badge.svg)
![Python Unit Tests](https://github.com/blankdots/minimalpy/workflows/Python%20Unit%20Tests/badge.svg)
![Python style check](https://github.com/blankdots/minimalpy/workflows/Python%20style%20check/badge.svg)
![Documentation Checks](https://github.com/blankdots/minimalpy/workflows/Documentation%20Checks/badge.svg)
[![Coverage Status](https://coveralls.io/repos/github/blankdots/minimalpy/badge.svg?branch=HEAD)](https://coveralls.io/github/blankdots/minimalpy?branch=HEAD)
[![Documentation Status](https://readthedocs.org/projects/minimalpy/badge/?version=latest)](https://minimalpy.readthedocs.io/en/latest/?badge=latest)

An example of a minimal Python 3.7+ project that contains an web application built with [aiohttp](http://aiohttp.readthedocs.io/).
At the same time the project exemplifies:
* aiohttp server;
* logging formatting;
* unit tests;
* [tox automation](https://tox.readthedocs.io) for:
  * [flake8](http://flake8.pycqa.org/en/latest/) style enforcement;
  * running unit tests and coverage;
* github-actions and [coveralls](https://coveralls.io/github/blankdots/minimalpy) integration;
* [bandit](https://bandit.readthedocs.io) to check common security issues in Python code;
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
├── bandit.yml
├── LICENSE
├── README.md
├── readthedocs.yml
├── requirements.txt
├── setup.py
├── tests
│   ├── conftest.py
│   ├── coveralls.py
│   ├── __init__.py
│   └── test_server.py
└── tox.ini
```

### Build and Deployment

#### Deploying with S2I (Source to Image)

Install s2i from: https://github.com/openshift/source-to-image

```
s2i build . centos/python-36-centos7 minimalpy
docker run -p 5430:5430 -e APP_FILE=minimalpy/server.py minimalpy
```

### License

`minimalpy` python and all it sources are released under `Apache License 2.0`.


### Similar Projects

Some projects similar in scope:

* https://github.com/pypa/sampleproject
* https://github.com/kennethreitz/samplemod
