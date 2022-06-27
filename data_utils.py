from csv import DictReader 


def read_csv_rows(path: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []
    file_handle = open(path, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)

    for row in csv_reader: 
        result.append(row)
    file_handle.close
    return result 


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Returns a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(table_of_rows: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a table represented as a list of rows into a table represented by a dictionary of columns."""
    result: dict[str, list[str]] = {}

    first_row: dict[str, str] = table_of_rows[0]
    for column in first_row: 
        result[column] = column_values(table_of_rows, column)
    return result


def head(column_table: dict[str, list[str]], number_of_values: int) -> dict[str, list[str]]:
    """Returns a column based table with first N number of rows of data for each column."""
    final_table: dict[str, list[str]] = {}
    for column in column_table:
        if number_of_values > len(column_table[column]):
            return column_table
        n_values: list[str] = []
        i: int = 0
        while i < number_of_values:
            n_values.append(column_table[column][i])
            i += 1
        final_table[column] = n_values
    return final_table


def select(column_table: dict[str, list[str]], selected_values: list[str]) -> dict[str, list[str]]:
    """Returns a column based table with only certain subsets of the original columns."""
    selected_dict: dict[str, list[str]] = {}
    for items in selected_values:
        selected_dict[items] = column_table[items]
    return selected_dict


def concat(table_1: dict[str, list[str]], table_2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Returns two tables combined."""
    combined_dict: dict[str, list[str]] = {}
    for columns in table_1:
        combined_dict[columns] = table_1[columns]
    for columns in table_2:
        if columns in combined_dict:
            combined_dict[columns] += table_2[columns]
        else:
            combined_dict[columns] = table_2[columns] 
    return combined_dict


def count(values: list[str]) -> dict[str, int]:
    """Counts the number of times a value is present in a list."""
    results: dict[str, int] = {}
    for item in values:
        if item in results:
            results[item] += 1
        else:
            results[item] = 1
    return results

    # My Own Function:


def count_certain_values(values: list[str]) -> dict[str, int]:
    """Counts the number of times certain values are present in a list."""
    results: dict[str, int] = {}
    for item in values: 
        if item in results and int(item) >= 4:
            results[item] += 1
        else:
            if item not in results and int(item) >= 4:
                results[item] = 1
    return results
