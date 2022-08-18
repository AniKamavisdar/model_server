from models.model import Model
from package import Model_


class PyFileModel(Model):

    def __init__(self):
        super().__init__('py_file')

    def load_transformer(self,file_name=None):
        self.transformer_object = Model_()
