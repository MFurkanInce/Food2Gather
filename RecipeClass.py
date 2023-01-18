class RecipeClass:
    def __init__(self):
        self.recipes = {}

    def get_default_recipes(self):
        self.recipes['Menemen'] = {
            " 2 yemek kaşığı sıvı yağ ,"
            "3 adet yeşil biber,3 orta boy domates,"
            "1/2 (yarım) çay kaşığı tuz,"
            "3 adet yumurta",
        }
        self.recipes['Kuru Fasulye'] = {
            "4 yemek kaşığı sıvı yağ,"
            "2 yemek kaşığı tereyağı,"
            "1 adet orta boy kuru soğan,"
            "1 yemek kaşığı domates salçası,"
            "500 gram kuru fasulye,"
            "3 su bardağı su,"
            "1 çay kaşığı tuz,"
            "1 çay kaşığı toz şeker,"
            "1/2 çay kaşığı tatlı toz kırmızı biber",
        }

    def find_recipe(self, name):

        if name in self.recipes:
            return name
        else:
            print('Could not find recipe')

    # Food2Gather v2.01
    # def get_category(self):
    #     countries = ['Turkey', 'Indian', 'USA', 'Japan', 'Netherlands']
    #     for recipe in self.recipes:
    #         for country in countries:
    #             if recipe.values()[1] == country:
    #                 return country
