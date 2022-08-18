from models.model import Model


class PyObjModel(Model):

    def __init__(self):
        super().__init__('py_method')

    def load_transformer(self, file_name=None):
        pass
