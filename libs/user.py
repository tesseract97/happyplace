import json

class User:

    def __init__(self, name):
        self.name = name
        self.sites = []
        self.background_img = []

    def get_sites(self):
        return self.sites
    
    def add_site(self, site):
        return self.sites.append(site)
    
    def del_site(self, site):
        return self.sites.remove(site)

    def get_background(self):
        return self.background_img
    
    def add_img(self, img):
        return self.background_img.append(img)
    
    def del_img(self, img):
        return self.background_img.remove(img)

    def user_to_json(self):
        return self.__dict__