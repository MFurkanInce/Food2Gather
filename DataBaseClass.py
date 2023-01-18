from Pics import PicClass
from RecipeClass import RecipeClass
from Authentication import Authenticator
from Food import FoodClass
from Food2Gather import Food2GatherAI


class DataBaseClass:
    """SINGLETON"""
    __instance = None

    @staticmethod
    def get_instance():
        if DataBaseClass.__instance == None:
            DataBaseClass()
        return DataBaseClass.__instance

    def __init__(self):

        if DataBaseClass.__instance != None:
            Exception("This class is a singleton!")
        else:
            DataBaseClass.__instance = self

        self.pics = PicClass()
        self.recipe = RecipeClass()
        self.users = Authenticator()
        self.foods = FoodClass()

    def create_default_db(self):
        'FACADE'
        self.pics.get_default_photos()
        self.recipe.get_default_recipes()
        self.users.get_default_users()

    def find_recipe_from_pic(self, pic):
        aimodel = Food2GatherAI()
        result = aimodel.run_model(input=pic, db=self.pics)
        recipe = self.recipe.find_recipe(result)

        return recipe

    def load_pics(self, input):
        self.pics.add_pic(input)
