class MembershipClass:
    def __init__(self):
        self.subscription_type = ['gold', 'platinum', 'diamond']

    def buy_ship(self, option):
        if option in self.subscription_type:
            return option
