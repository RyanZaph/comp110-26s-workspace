"""Defining a function to ise on my analysis notebook."""


def column_values(row_table: list[dict[str, str]], column: str) -> list[str]:

    result: list[str] = []

    for d in row_table:
        value: str = d[column]
        result.append(value)

    return result

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