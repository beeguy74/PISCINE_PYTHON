from pandas import read_csv, DataFrame


def load(path: str) -> DataFrame:
    ''' takes a path as argument, writes the dimensions of the data set
    and returns it'''
    data = None
    try:
        data = read_csv(path)
        print("Loading dataset of dimensions", data.shape)
        data.set_index("country", inplace=True)
    except OSError as e:
        print("Loading csv failed:", e)
    return data
