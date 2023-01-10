class Authenticator:
    def __init__(self):

        self.Users = []

    def authenticate(self, user):
        if user in self.Users:
            return True
        else:
            return False
