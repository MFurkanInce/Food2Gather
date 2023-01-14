class PicClass:
    def __init__(self):
        self.size = 50
        self.weight = 1920
        self.height = 1080
        self.photos = self.get_default_photos()

    def get_pic_shape(self):
        return self.weight, self.height

    def get_default_photos(self):
        photos =[]
        #get default photos
        return photos