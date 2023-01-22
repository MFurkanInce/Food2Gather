class MembershipClass:
    def __init__(self):
        self.subscription_type = ['gold', 'platinum', 'diamond']
        self.price = {'gold': 150,
                      'platinum': 200,
                      'diamond': 250}

    def buy_ship(self, option):
        if option in self.subscription_type:
            print('Thank you for purchasing our membership plan')
            print(f'Plan : f{option}'
                  f'Price : f{self.price[option]}')
            return option
