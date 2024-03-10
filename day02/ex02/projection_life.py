#!/usr/bin/env python3


from load_csv import load
import matplotlib.pyplot as plt


def main():
    '''
    displays population of Russia and France
    '''
    df = load("sample_data/population_total.csv")
    if df is None:
        return
    df.rename(columns=int, inplace=True)
    res = df.loc[:, df.columns < 2051]
    france = res.loc['France']
    russia = res.loc['Russia']

    plt.plot(russia.index, russia.values, color='blue', label="Russia")
    plt.plot(france.index, france.values, color='green', label="France")

    yticks = [35000000, 60000000, 135000000]
    myticks = ["35M", "60M", "135M"]
    plt.yticks(yticks, myticks)
    plt.legend(loc="lower right")

    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.title("France Life expectancy Projections")
    plt.show()


if __name__ == "__main__":
    main()
