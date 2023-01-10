from __future__ import annotations

from Membership import MembershipClass
from ChatBot import ChatBotClass

from typing import Callable


class LimitStrategyValidator:  # Descriptor class for check perform
    @staticmethod
    def validate(obj: Member, value: Callable) -> bool:
        ship = MembershipClass()
        print(value)
        if value in ship.subscriptions:
            return True
        else:
            print('validate error')
            return False

    def __set_name__(self, owner, name: str) -> None:
        self.private_name = f"_{name}"

    def __set__(self, obj: Member, value: Callable = None) -> None:
        if value and self.validate(obj, value):
            setattr(obj, self.private_name, value)
        else:
            setattr(obj, self.private_name, None)

    def __get__(self, obj: object, objtype: type = None):
        return getattr(obj, self.private_name)

def apply_subscription(member: Member) -> float:
    ship = MembershipClass()
    subs = member.membership
    for num, sub in enumerate(ship.subscriptions):
        if subs == sub:
            member.upload_limit = (num+1) * 25
            return member.upload_limit


class Admin:
    def __init__(self):
        self.name = "admin"

    def show_info(self):
        return "Admin created " + self.name


class Member:
    limit_strategy = LimitStrategyValidator()

    def __init__(self, limit_strategy: Callable = None):
        self.name = "Ahmet"
        self.password = "XXX123"
        self.membership = "bronze"
        self.upload_limit = 25
        self.limit_strategy = limit_strategy

    def talk_chatbot(self):
        bot = ChatBotClass()
        return 'member ' + bot.talk()

    def buy_membership(self, option):
        ship = MembershipClass()
        self.membership = ship.buy_ship(option=option)
        self.upload_limit = apply_subscription(self)

    def show_info(self):
        return "Member ::: " + self.name + " " + str(self.membership) + " " + str(self.upload_limit)



def UserFactory(type) -> object:
    """Factory"""
    Users = {
        "Admin": Admin,
        "Member": Member,
    }

    return Users[type]()
