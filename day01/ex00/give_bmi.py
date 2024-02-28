import numpy as np


def give_bmi(
        height: list[int | float],
        weight: list[int | float]) -> list[int | float]:
    '''take 2 lists of integers or floats in input and returns a list
        of BMI values. BMI = poids[kg] / taille2[m2]'''
    res = []
    try:
        assert len(height) == len(weight), "lists are not the same size"
        res = np.divide(weight, np.square(height)).tolist()
    except Exception as e:
        print("give_bmi's Error :", e)
    return res


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    '''accepts a list of integers or floats and an integer representing
      a limit as parameters. It returns a list of booleans
      (True if above the limit)'''
    res = []
    try:
        assert isinstance(limit, int), 'limit should be int type'
        res = np.vectorize(lambda num: num > limit)(bmi).tolist()
    except Exception as e:
        print("apply_limit's Error :", e)
    return res
