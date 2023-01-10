class Membership:
    def __init__(self):
        self.temp='s'
        self.subscriptions=['bronz','silver','gold','diamond']

    def select_member(self,opt):
        if opt in self.subscriptions:
            return self.subscriptions[opt]
        else:
            return " "
