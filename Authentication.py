class Authenticator:
    def __init__(self):

        self.Users = []

    def authenticate(self, user):
        if user in self.Users:
            return True
        else:
            return False

    def add_user(self, user):
        self.Users.append(user)

    def get_default_users(self):
        self.Users.append("Dincer")
        self.Users.append("Kaan")
        self.Users.append("Ince")


