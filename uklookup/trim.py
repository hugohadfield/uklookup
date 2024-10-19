"""
This file contains a function that trims the columns of a CSV file and writes the trimmed columns to the 
same file. The function is then used to trim the columns of all CSV files in a directory. 
This is used to process the downloaded codepointopen dataset before it can be used by the 
lookup_postcode functionality. It makes the whole package much smaller to distribute and install.
"""

import csv
import gzip
from pathlib import Path


def trim_csv_columns(file_path: Path, n_cols: int):
    """
    Opens, reads, and trims the columns of a CSV file then writes the trimmed
    columns to the same file.
    """
    with open(file_path) as f:
        reader = csv.reader(f)
        rows = [row[:n_cols] for row in reader]
        n_processed = len(rows)

    # Delete the original file and write the trimmed rows to a new file
    file_path.unlink()

    with gzip.open(str(file_path) + '.gz', 'wt') as f:
        writer = csv.writer(f)
        writer.writerows(rows)
    return n_processed


def trim_all_files(directory: Path, n_cols: int):
    """
    Trims the columns of all CSV files in a directory.
    """
    total_processed = 0
    for file_path in directory.glob("*.csv"):
        n_processed = trim_csv_columns(file_path, n_cols)
        total_processed += n_processed
    print(f"Trimmed {total_processed} postcodes")


if __name__ == "__main__":
    trim_all_files(Path("codepointopen/Data/CSV"), 4)