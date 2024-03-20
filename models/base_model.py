#!/usr/bin/python3

# models/base_model.py

from datetime import datetime
import uuid

class BaseModel:
    def __init__(self):
        # Your initialization logic here
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        # Your string representation logic here
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        # Your save logic here
        self.updated_at = datetime.now()

    def to_dict(self):
        # Your to_dict logic here
        result = self.__dict__.copy()
        result['created_at'] = self.created_at.isoformat()
        result['updated_at'] = self.updated_at.isoformat()
        return result
