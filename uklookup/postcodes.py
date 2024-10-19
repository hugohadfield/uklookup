
from pathlib import Path
from typing import Dict, Tuple, Optional
import sys
from functools import lru_cache

import numpy as np
from convertbng.util import convert_lonlat


def clean_alphanum(string: str) -> str:
    """
    Remove all non-alphanumeric characters from a string.
    """
    return "".join(c for c in string if c.isalnum())


def clean_alpha(string: str) -> str:
    """
    Remove all non-alphabetic characters from a string.
    """
    return "".join(c for c in string if c.isalpha())


@lru_cache(maxsize=5)
def get_prefix_data(prefix: str) -> Dict[str, Tuple[int, int]]:
    """
    Load the file containing the postcodes starting with the given prefix and return the 
    eastings and northings as numpy array.
    """
    current_file = Path(__file__).resolve()
    current_dir = current_file.parent
    # filename = f"codepointopen/Data/CSV/{prefix.lower().strip()}.csv.gz"
    filename = current_dir / f"codepointopen/Data/CSV/{prefix.lower().strip()}.csv.gz"
    path = Path(filename)
    if not path.exists():
        raise FileNotFoundError(f"No data found for prefix {prefix} at file {path.absolute()}")
    east_north = np.genfromtxt(filename, delimiter=",", skip_header=0, usecols=(2, 3), dtype=int)
    codes = np.genfromtxt(filename, delimiter=",", skip_header=0, usecols=(0), dtype=str)
    data = {code: (east, north) for code, (east, north) in zip(codes, east_north)}
    return data


def lookup_postcode(postcode: str) -> Optional[Tuple[int, int]]:
    """
    Look up the easting and northing for a given postcode.
    """
    prefix = clean_alpha(postcode.lower().split()[0])
    data = get_prefix_data(prefix)
    if postcode in data:
        return data[postcode]
    return None


def lookup_postcode_lat_long(postcode: str) -> Optional[Tuple[float, float]]:
    """
    Look up the latitude and longitude for a given postcode.
    """
    result = lookup_postcode(postcode)
    if result is None:
        return None
    east, north = result
    longs, lats = convert_lonlat([east], [north])
    return lats[0], longs[0]


if __name__ == '__main__':
    # postcode is the first command line argument
    postcode = " ".join(sys.argv[1:])
    eastings_northings = lookup_postcode(postcode)
    if eastings_northings is None:
        print(f"Postcode {postcode} not found.")
        sys.exit(1)
    eastings, northings = eastings_northings
    lat_long = lookup_postcode_lat_long(postcode)
    if lat_long is None:
        print(f"Postcode {postcode} not found.")
        sys.exit(1)
    lat, long = lat_long
    print(f"Postcode: {postcode}")
    print(f"Easting: {eastings}, Northing: {northings}")
    print(f"Latitude: {lat}, Longitude: {long}")
