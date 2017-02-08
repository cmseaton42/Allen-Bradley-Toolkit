"""
A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'Description.txt'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    # Project MetaData
    name='Preh',
    version='1.0a2',
    description='Allen-Bradley Python Toolbelt',
    long_description=long_description,
    url='https://bitbucket.org/cmseaton42/allen-bradley-python-tools',

    # Author Information
    author='Canaan Seaton',
    author_email='cmseaton42@gmail.com',

    # Licensing
    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7'
    ],

    # Package Specific Data
    keywords='PLC Tools XML L5X LXML Rockwell Allen Bradley Allen-Bradley Python Python27',
    packages=find_packages(exclude=['Docs', 'tests']),
    install_requires=[
        'lxml==3.6.0',
        'enum'
    ],
    scripts=[
        'Scripts/BuildPBRoutine.py'
    ],
    zip_safe=False
)
