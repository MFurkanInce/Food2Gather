class CalorieCalculator:
    def __init__(self, food):
        self.calorie = calc_calorie(foods=food)


def calc_calorie(foods):
    # do something
    calc = (len(foods) * 0.5 / 100) * 43.7
    return calc
