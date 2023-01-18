from CalorieCalculator import CalorieCalculator


class FoodClass:
    def __init__(self):
        self.foods_calories = {"Menemen": 250,
                               "Kuru_Fasulye": 350}

    def calorie_calc(self, food):
        calculator = CalorieCalculator(food)
        self.foods_calories[food] = calculator.calorie
