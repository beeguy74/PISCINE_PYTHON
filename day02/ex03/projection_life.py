#!/usr/bin/env python3


from load_csv import load
import matplotlib.pyplot as plt


def main():
    '''
    displays the projection of life expectancy in relation to the gross
    national product of the year 1900 for each country
    '''
    ipp = load(
        "sample_data/income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
        )
    expectancy = load("sample_data/life_expectancy_years.csv")

    if ipp is None or expectancy is None:
        return
    data_ipp = ipp["1900"]
    data_expectancy = expectancy["1900"]
    print(data_ipp)
    print(data_expectancy)

    xticks = [300, 1000, 10000]
    myticks = ["300", "1k", "10k"]

    plt.scatter(data_ipp, data_expectancy)
    plt.title("1900")
    plt.xlabel("Gross domestic product")
    plt.ylabel("Life Expectancy")
    plt.xscale("log")
    plt.xticks(xticks, myticks)
    plt.show()


if __name__ == "__main__":
    main()
