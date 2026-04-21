"""Defining a function to ise on my analysis notebook."""


def column_values(row_table: list[dict[str, str]], column: str) -> list[str]:

    result: list[str] = []

    for d in row_table:
        value: str = d[column]
        result.append(value)

    return result
