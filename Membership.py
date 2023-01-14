class MembershipClass:
    def __init__(self):
        self.subscriptions = ['bronze', 'silver', 'gold', 'diamond']

    def buy_ship(self, option):
        if option in self.subscriptions:
            return option
