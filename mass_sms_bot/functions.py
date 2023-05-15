import sys

import pandas as pd


def get_dataframe(file):
    string_tokens = file.split(".")
    if len(string_tokens) != 2:
        sys.exit("Invalid file")
    else:
        if string_tokens[1] == "csv":
            df = pd.read_csv(file)
        elif string_tokens[1] == "xlsx":
            df = pd.read_excel(file)
        elif string_tokens[1] == "json":
            df = pd.read_json(file)
        else:
            sys.exit("Invalid extension")

        return df


def switch_to_international(phone_num):
    digits_only = "".join(filter(lambda x: x.isdigit(), phone_num))

    if len(digits_only) > 11:
        return 0
    elif len(digits_only) == 11:
        digits_only = digits_only[1:]
    return "+1" + digits_only
