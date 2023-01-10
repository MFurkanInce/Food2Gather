import numpy as np
class ChatBotClass:
    def __init__(self):
        self.vocabulary = ['Merhaba', 'Ne vereyim abime' , 'xxx']

    def talk(self):
        return np.random.choice(self.vocabulary)

