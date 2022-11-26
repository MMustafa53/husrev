import sys
import os.path

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

from src import sqlacodegen_husrev


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)


extra_requirements = ()
if sys.version_info < (2, 7):
    extra_requirements = ('argparse',)

here = os.path.dirname(__file__)
readme_path = os.path.join(here, 'README.rst')
readme = open(readme_path).read()

setup(
    name='sqlacodegen_husrev',
    description='Automatic model code generator for SQLAlchemy',
    long_description=readme,
    version=sqlacodegen_husrev.__version__,
    author='Alex Gronholm',
    author_email='sqlacodegen_husrev@nextday.fi',
    url='http://pypi.python.org/pypi/sqlacodegen/',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Environment :: Console',
        'Topic :: Database',
        'Topic :: Software Development :: Code Generators',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11'
    ],
    keywords='sqlalchemy',
    license='MIT',
    packages=find_packages(exclude=['tests']),
    install_requires=(
        'SQLAlchemy >= 0.6.0',
        'inflect >= 0.2.0'
    ) + extra_requirements,
    tests_require=['pytest', 'pytest-pep8'],
    cmdclass={'tests': PyTest},
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'sqlacodegen_husrev=sqlacodegen_husrev.main:main'
        ]
    }
)
