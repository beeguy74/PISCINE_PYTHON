#!/usr/bin/env python3


from load_csv import load
import matplotlib.pyplot as plt


def main():
    '''
    loads the file 'life_expectancy_years.csv', and displays
    information about France.
    '''
    df = load("sample_data/life_expectancy_years.csv")
    if not df:
        return
    res = df.loc['France']
    plt.plot(res.index.astype(int), res.values)
    plt.xlabel("Year")
    plt.ylabel("Life expectancy")
    plt.title("France Life expectancy Projections")
    plt.show()


if __name__ == "__main__":
    main()
