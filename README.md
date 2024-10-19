# Postcode Lookup Tool

This repository contains a simple Python package for looking up UK postcodes to obtain their easting/northing coordinates and corresponding latitude/longitude values. The package reads data from CSV files based on the postcode prefix and uses this data to perform lookups efficiently.

## Features

- Lookup eastings and northings for a given UK postcode.
- Convert the easting and northing coordinates to latitude and longitude.
- Efficient caching using `functools.lru_cache` to improve performance for repeated postcode prefix lookups.
  
## Installation

You can install this package directly from PyPI using `pip`:

```bash
pip install uklookup
```

## Usage

### Command Line Usage

Once installed, you can use the package directly from the command line to look up the easting, northing, latitude, and longitude for a UK postcode:

```bash
python -m uklookup "SW1A 1AA"
```

Example output:

```
Postcode: SW1A 1AA
Easting: 530046, Northing: 179386
Latitude: 51.501009, Longitude: -0.141588
```

### Programmatic Usage

You can also import the package and use it in your own Python scripts.

#### Example:

```python
from uklookup import lookup_postcode_lat_long

postcode = "SW1A 1AA"
lat_long = lookup_postcode_lat_long(postcode)

if lat_long:
    lat, long = lat_long
    print(f"Latitude: {lat}, Longitude: {long}")
else:
    print("Postcode not found.")
```

### Functions

#### `lookup_postcode(postcode: str) -> Optional[Tuple[int, int]]`
Looks up the easting and northing for a given UK postcode. Returns a tuple of integers `(easting, northing)` if found, or `None` if the postcode is not in the dataset.

#### `lookup_postcode_lat_long(postcode: str) -> Optional[Tuple[float, float]]`
Looks up the latitude and longitude for a given UK postcode. Returns a tuple of floats `(latitude, longitude)` if found, or `None` if the postcode is not in the dataset.

### Dependencies

- `numpy`
- `convertbng` (for converting eastings/northings to latitudes/longitudes)

## License

This project is licensed under the MIT License.

## Acknowledgements

This project uses data from the Code-Point Open dataset provided by Ordnance Survey. The data is available under the Open Government Licence v3.0.

## Other Projects
A much more comprehensive postcode lookup tool is available at [postcodes.io](https://postcodes.io/). This project is a simple alternative for basic postcode lookups in an offline setting.
