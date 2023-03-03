"""A setuptools based setup module.
"""
from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name='pulsar-timing',  # Required
    version='1.0.0',  # Required
    description='Make timing fits to pulsars',  # Optional
    long_description=long_description,  # Optional
    long_description_content_type='text/markdown',  # Optional (see note above)
    author='Ulrik Egede',  # Optional
    author_email='ulrik.egede@monash.edu',  # Optional
    classifiers=[  # Optional
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',

        # Pick your license as you wish
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate you support Python 3. These classifiers are *not*
        # checked by 'pip install'. See instead 'python_requires' below.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3 :: Only',
    ],

    # When your source code is in a subdirectory under the project root, e.g.
    # `src/`, it is necessary to specify the `package_dir` argument.
    # package_dir={'': 'src'},  # Optional
    #
    packages=find_packages(where='src'),  # Required

    python_requires='>=3.8, <4',
    install_requires=[
        'iminuit',
        'ipykernel',
        'numpy',
        'matplotlib',
        'numba_stats',
        'pandas',
    ],
    extras_require={
        'dev': ['pytest', 'pytest-cov', 'flake8', 'coveralls'],
    },

    # If there are data files included in your packages that need to be
    # installed, specify them here.
    package_data={  # Optional
        'input': ['pulses_turn_nobl.txt'],
    },

    # entry_points={  # Optional
    #    'console_scripts': [
    #        'monitor=spotmanager.monitor:main',
    #    ],
    #},

)
