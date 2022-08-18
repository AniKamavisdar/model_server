import pickle
from models.model import Model


class PklModel(Model):

    def __init__(self):
        super().__init__('pkl')

    def load_transformer(self,file_name):
        with open(file_name,'rb') as file:
            self.transformer_object = pickle.load(file)
        pass
