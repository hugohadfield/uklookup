from setuptools import setup, find_packages
import os

here = os.path.abspath(os.path.dirname(__file__))
exec(open(os.path.join(here, 'uklookup/version.py')).read())

setup(
    name='uklookup',
    version=__version__,
    description='A tool to look up UK postcode eastings, northings, and convert them to latitude and longitude.',
    author='Hugo Hadfield',
    author_email='hadfield.hugo@gmail.com',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'convertbng'
    ],
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/hugohadfield/uklookup",
    license='MIT',
    entry_points={
        'console_scripts': [
            'postcode_lookup=postcode_lookup:main'
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    package_data={
        # Include all CSV files under codepointopen directory
        'uklookup': ['codepointopen/Data/CSV/*.csv.gz'],
    },
    include_package_data=True,
)
