from pandas import read_csv, DataFrame


def converter(x):
    if 'M' in x:
        res = float(x.strip('M'))*1000000
    elif 'B' in x:
        res = float(x.strip('B'))*1000000000
    elif 'k' in x:
        res = float(x.strip('k'))*1000
    else:
        res = x
    return int(res)


def load(path: str) -> DataFrame:
    ''' takes a path as argument, writes the dimensions of the data set
    and returns it'''
    data = None
    try:
        col_names = read_csv(path, nrows=0).columns.tolist()
        dtypes_dict = {col_name: str if col_name == "country"
                       else converter
                       for col_name in col_names}
        data = read_csv(path, index_col=0, converters=dtypes_dict)
        print("Loading dataset of dimensions", data.shape)
        # data.set_index("country", inplace=True)
    except OSError as e:
        print("Loading csv failed:", e)
    return data
