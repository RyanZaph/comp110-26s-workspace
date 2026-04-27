"""Data related utility functions."""

__author__ = ["730894533", ""]

from csv import DictReader


def get_keys(
    input_dict: (
        dict[str, list[str]]
        | dict[str, list[int]]
        | dict[str, list[str | int]]
        | dict[str, int]
        | dict[str, str]
    ),
) -> list[str]:
    result: list[str] = []
    for key in input_dict:
        result.append(key)

    return result


def convert_columns_to_int(
    data: dict[str, list[str]], columns_conv: list[str]
) -> dict[str, list[str | int]]:
    """Convert the data in the selected columns to be of type int."""
    # Create new table to store converted data
    data_converted: dict[str, list[int | str]] = {}

    # Iterate through column names (keys of the dictionary)
    for col_name in data:
        # Create new list to append converted values to
        data_converted[col_name] = []

        # Declare the converted value with a type of either int or str
        converted_value: int | str

        # Iterate through data values in the column
        for value in data[col_name]:
            # If this column is in the list of columns to be converted,
            # cast it to an int
            if col_name in columns_conv:
                converted_value = int(value)
            else:
                converted_value = value

            # Add it to the new column of values, the list we created
            # that we have a reference to at data_converted[col_name]
            data_converted[col_name].append(converted_value)

    return data_converted


"""These are the functions we wrote/will write in class!"""


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a CSV into a 'table'."""
    result: list[dict[str, str]] = []

    # Open a handle to the data file
    file_handle = open(filename, "r", encoding="utf8")

    # Prepare to read the data file as a CSV rather than just strings.
    csv_reader = DictReader(file_handle)

    # Read each row of the CSV line-by-line
    for row in csv_reader:
        result.append(row)

    # Close the file when done, to free its resources.
    file_handle.close()

    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []

    for row in table:
        item: str = row[column]
        result.append(item)

    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}

    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column) 
    return result


# take certain number of rows (N) and return new column basded list
def head( data_dict: dict[str, list[str]], N_rows: int) -> dict[str, list[str]]:  # first string is column name
    new_data_dict: dict[str, list[str]] = {}
    for column in data_dict:  # column is key and row is index value
        new_data_dict[column] = data_dict[column][
            :N_rows
        ]  # creates new dict and assigns key vvalue pair of data dict and uses 0 through Nth rows
    return new_data_dict


def select(
    og_dict: dict[str, list[str]], column_list: list[str]
) -> dict[str, list[str]]:
    result_dict: dict[str, list[str]] = {}
    for column in column_list:
        result_dict[column] = og_dict[column]
    return result_dict


# assigns select data of the orignal dat set to the new one without all the extra data


def concat(
    dict_a: dict[str, list[str]], dict_b: dict[str, list[str]]
) -> dict[str, list[str]]:
    result_dict: dict[str, list[str]] = {}
    for column in dict_a:
        result_dict[column] = dict_a[column]
    for column in dict_b:
        if column in result_dict:
            result_dict[column] += dict_b[column]
        else:
            result_dict[column] = dict_b[column]
    return result_dict


def count(og_list: list[str]) -> dict[str, int]:
    result_dict: dict[str, int] = {}
    for item in og_list:
        if item in result_dict:
            result_dict[item] += 1
        else:
            result_dict[item] = 1
    return result_dict

"""data - This is where you input your data dictionary.
kind - Customizes the kind of plot you'll get from relplot. Possible values: "scatter", "line"
x, y - Use these to define the data that will be on your x and y axes, using your column names as the arguments.
size (Optional) - Use this to define the size of your dots for the scatterplot or the width of the lines for the lineplot relative to a column's data, using the column's name as the argument.
col (Optional) - Use this to split your figure into multiple plots based on the values in a column, using the column's name as the argument.
hue (Optional) - Use this to define the color of your dots or lines for the lineplot relative to a column's data, using the column's name as the argumen"""


def data_filter(concat_dict: dict[str, list[str]]) -> dict[str, list[str]]:
    result: dict[str, list[str]] = {}
    keep_indices: list[int] = []

    for element in range(len(concat_dict["interested_connections"])):
        if int(concat_dict["interested_connections"][element]) <= 3:
            keep_indices.append(element) 

    for column in concat_dict:
        result[column] = []
        for element in keep_indices:
            result[column].append(concat_dict[column][element])

    return result