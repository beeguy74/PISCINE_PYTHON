import numpy as np


def give_bmi(
        height: list[int | float],
        weight: list[int | float]) -> list[int | float]:
    '''take 2 lists of integers or floats in input and returns a list
        of BMI values. BMI = poids[kg] / taille2[m2]'''
    res = []
    try:
        res = np.divide(weight, np.square(height)).tolist()
    except Exception as e:
        print("Error give_bmi:", e)
    return res


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    '''accepts a list of integers or floats and an integer representing
      a limit as parameters. It returns a list of booleans
      (True if above the limit)'''
    res = []
    try:
        res = np.vectorize(lambda num: num > limit)(bmi).tolist()
    except Exception as e:
        print("Error apply_limit:", e)
    return res


def main():
    # your tests and your error handling
    height = [2.71, 1.15]
    weight = [165.3, 38.4]
    bmi = give_bmi(height, weight)
    print(bmi, type(bmi))
    print(apply_limit(bmi, 26))


if __name__ == "__main__":
    main()
