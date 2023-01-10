from Membership import Membership
from Membership import *


class Admin:
    def __init__(self):
        self.name = "admin"

    def show_info(self):
        return "Admin created " + self.name


class Member:
    def __init__(self):
        self.name = "Ahmet"
        self.password = "XXX123"
        self.type = "standard"

    def buy_membership(self, option):
        ship = Membership()
        print(type(ship))
        subs = ship.select_member(option)
        self.type = subs


    def show_info(self):
        return "Member created " + self.name + " " + self.type


def UserFactory(type) -> object:
    """Factory"""
    Users = {
        "Admin": Admin,
        "Member": Member,
    }

    return Users[type]()
