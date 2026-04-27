from data_utils import head

data_cols_head: dict[str, list[str]] = head(data_cols, 5)

if (
    len(get_keys(data_cols_head)) != len(get_keys(data_cols))
    or len(data_cols_head["year"]) != 5
):
    print("Complete your implementation of columnar in data_utils.py")
    print(
        "Be sure to follow the guidelines above and save your work before re-evaluating!"
    )

tabulate(data_cols_head, get_keys(data_cols_head), "html")
