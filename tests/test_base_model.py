#!/usr/bin/python3
"""
Test module for BaseModel.
"""
import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """
    Test cases for BaseModel class.
    """
    def test_base_model_instance(self):
        """
        Test instantiation of BaseModel.
        """
        my_model = BaseModel()
        self.assertIsInstance(my_model, BaseModel)
        self.assertIsInstance(my_model.id, str)
        self.assertIsInstance(my_model.created_at, datetime)
        self.assertIsInstance(my_model.updated_at, datetime)

    def test_str_representation(self):
        """
        Test string representation of BaseModel.
        """
        my_model = BaseModel()
        expected_str = "[BaseModel] ({}) {}".format(my_model.id, my_model.__dict__)
        self.assertEqual(str(my_model), expected_str)

    def test_save_method(self):
        """
        Test save method of BaseModel.
        """
        my_model = BaseModel()
        original_updated_at = my_model.updated_at
        my_model.save()
        self.assertNotEqual(original_updated_at, my_model.updated_at)

    def test_to_dict_method(self):
        """
        Test to_dict method of BaseModel.
        """
        my_model = BaseModel()
        obj_dict = my_model.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertEqual(obj_dict["__class__"], "BaseModel")
        self.assertEqual(obj_dict["created_at"], my_model.created_at.isoformat())
        self.assertEqual(obj_dict["updated_at"], my_model.updated_at.isoformat())
