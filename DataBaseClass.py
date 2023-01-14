from Pics import PicClass
from RecipeClass import RecipeClass
from Authentication import Authenticator


class DataBaseClass:
    def __init__(self):
        self.pics = PicClass()
        self.recipe = RecipeClass()
        self.users = Authenticator()

    def create_default_db(self):
        'FACADE'
        self.pics.get_default_photos()
        self.recipe.get_default_recipes()
        self.users.get_default_users()