"""Exercise 8 utility functions."""

__author__ = "730466997"

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read an entire CSV of data into a list of rows represented by dictionaries."""
    data_rows: list[dict[str, str]] = []
    
    # Open a handle to the data file
    file_handle = open(filename, "r", encoding="utf8")

    # Prepare to read the data file as CSV rather than just strings
    csv_reader = DictReader(file_handle)

    # Read each row of the CSV line-by-line
    for row in csv_reader:
        data_rows.append(row)

    # Close the file when we're done, to free its resources.
    file_handle.close()

    return data_rows


def column_values(rows: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list of all values in a single column whose name is given."""
    values: list[str] = []
    
    for row in rows:
        values.append(row[column])

    return values


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}
    
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)

    return result


def head(table: dict[str, list[str]], n: int) -> dict[str, list[str]]:
    """Produce a new column-based table of only the first n rows."""
    new_table: dict[str, list[str]] = {}
    for column in table:
        values: list[str] = []
        i: int = 0
        while i < n and i < len(table[column]):
            values.append(table[column][i])
            i += 1
        new_table[column] = values
    return new_table


def select(table: dict[str, list[str]], desired_columns: list[str]) -> dict[str, list[str]]:
    """Produce a new column-based table with only specific columns."""
    new_table: dict[str, list[str]] = {}
    for column in desired_columns:
        new_table[column] = table[column]
    return new_table


def concat(table_one: dict[str, list[str]], table_two: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce a new column-based table with two column-based tables combined."""
    new_table: dict[str, list[str]] = {}
    for column in table_one:
        new_table[column] = table_one[column]
    for column in table_two:
        if column in new_table:
            new_table[column] += table_two[column]
        else:
            new_table[column] = table_two[column]
    return new_table


def count(values: list[str]) -> dict[str, int]:
    """Produce a dictionary that counts the number of times a value has occurred in a list."""
    counts: dict[str, int] = {}
    for item in values:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    return counts


def sift(table: dict[str, list[str]], filtered_column: str, value: str, values_column: str) -> list[str]:
    """Produce a list of values that correspond with a specific value in another column."""
    # Index variable
    i: int = 0

    # Lists of values for each column
    filtered_column_values: list[str] = table[filtered_column]
    values_column_values: list[str] = table[values_column]

    # List of indexes for corresponding values
    indices: list[int] = []
    
    # Loop through the filtered column and add all the indices that match the given value
    for item in filtered_column_values:
        if item == value:
            indices.append(i)
        i += 1
    
    # Create a list and add all values with corresponding indices
    values: list[str] = []
    i = 0
    for item in values_column_values:
        if i in indices:
            values.append(item)
        i += 1

    return values


def avg_from_strings(values_strings: list[str]) -> float:
    """Produce the average value given a list of strings."""
    average: float = 0.0

    # Change strings to floats
    values_floats: list[float] = []
    for string in values_strings:
        values_floats.append(float(string))

    # Calculate total
    total: float = 0.0
    for number in values_floats:
        total += number

    # Find average by dividing total by length of list
    average = total / len(values_floats)

    return average
