import numpy as np


class ChatBotClass:
    def __init__(self, user):
        self.dictionary = ['Nasil Yardimci Olabilirim?', 'Abonelik almak ister misiniz?',
                           'Sorununuzu detaylandirabilir misiniz?',
                           'Istediginiz tarifi bulamadiysaniz lutfen bizimle iletisime gecin',
                           'mail: info@food2gather.com', 'Turk tariflere sahip tek uygulama Food2Gather',
                           'Food2Gather simdi Google Play Store ve App Storeda']
        self.user = user

    def talk(self):
        result = " Hosgeldiniz " + str(self.user) + " " + np.random.choice(self.dictionary)
        return result
