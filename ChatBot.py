import numpy as np


class ChatBotClass:
    def __init__(self, user):
        self.vocabulary = ['Nasil Yardimci Olabilirim?', 'Abonelik almak ister misiniz?',
                           'Sorununuzu detaylandirabilir misiniz?']
        self.user = user

    def talk(self):
        result = " HOSGELDINIZ " + str(self.user) + " " + np.random.choice(self.vocabulary)
        return result
