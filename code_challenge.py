import sys
from string import ascii_lowercase

import pandas as pd


DEFAULT_BASE_PATH = 'https://public.wiwdata.com/engineering-challenge/data/'


def process_data(base_url):
    """ Transform web traffic data to per user format

    Reads web traffic data at the base_url and transforms it to per user format, 
    where each row is different user and column represents length of time in seconds 
    spent by user on each of the page path.
    Final result is written to the user_visits.csv in current directory.

    base_url - public root url to the data
    """

    print("Processing data at path ", base_url)

    table = pd.DataFrame([])

    for c in ascii_lowercase:
        try:
            url = base_url + c + ".csv"
            df = pd.read_csv(url)
            table = pd.concat([table, df])
        except Exception as e:
            print(e.__class__, " exception happened processing file ", c, ".csv")

    if not table.empty:
        table = pd.pivot_table(table, index=["user_id"], columns=[
                               "path"], values="length", aggfunc="sum", fill_value=0)
        table.to_csv(path_or_buf='./user_visits.csv')
        print("Final csv file created at ./user_visits.csv")


def main(args):
    if len(args) == 0:
        process_data(DEFAULT_BASE_PATH)
    else:
        process_data(args[0])


if __name__ == "__main__":
    main(sys.argv[1:])
