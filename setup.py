from setuptools import setup, find_packages
from minimalpy import __version__, __author__, __title__
from os import path

here = path.abspath(path.dirname(__file__))

# main module source folder, will be used for imports as the main module
_main_module = 'minimalpy'

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    # There are some restrictions on what makes a valid project name
    # specification here:
    # https://packaging.python.org/specifications/core-metadata/#name
    name='minimalpy',  # Required

    # Versions should comply with PEP 440:
    # https://www.python.org/dev/peps/pep-0440/
    #
    # For a discussion on single-sourcing the version across setup.py and the
    # project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version=__version__,  # Required

    # This is a one-line description or tagline of what your project does. This
    # corresponds to the "Summary" metadata field:
    # https://packaging.python.org/specifications/core-metadata/#summary
    description=__title__,  # Required

    # This field corresponds to the "Description" metadata field:
    # https://packaging.python.org/specifications/core-metadata/#description-optional
    long_description=long_description,  # Optional

    # This field corresponds to the "Description-Content-Type" metadata field:
    # https://packaging.python.org/specifications/core-metadata/#description-content-type-optional
    long_description_content_type='text/markdown',  # Optional (see note above)

    # This field corresponds to the "Home-Page" metadata field:
    # https://packaging.python.org/specifications/core-metadata/#home-page-optional
    url='https://github.com/blankdots/minimalpy',  # Optional

    author=__author__,  # Optional

    author_email='blankdots@gmail.com',  # Optional

    # For a list of valid classifiers, see https://pypi.org/classifiers/
    classifiers=[  # Optional
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish
        'License :: OSI Approved :: Apache Software License',

        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],


    keywords='setuptools development',  # Optional

    # Required
    # packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    # Alternative for listing individual packages
    packages=[_main_module],

    # For an analysis of "install_requires" vs pip's requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=['aiohttp'],  # Optional

    extras_require={  # Optional
        'test': ['coverage', 'pytest', 'pytest-cov', 'coveralls', 'tox'],
    },

    package_data={'': ['data/*.json']},  # Optional

    entry_points={  # Optional
        'console_scripts': [
            'minimal=minimalpy.server:main',
        ],
    },

    project_urls={  # Optional
        'Source': 'https://github.com/blankdots/minimalpy/',
    },
)
