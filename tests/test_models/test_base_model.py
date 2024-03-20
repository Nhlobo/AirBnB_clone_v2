import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    def test_create_instance(self):
        obj = BaseModel()
        self.assertIsNotNone(obj)

    # Add more test cases as needed
