#!/usr/bin/python3

# models/engine/file_storage.py

import json

class FileStorage:
    def __init__(self):
        # Your initialization logic here
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        # Your all method logic here
        return self.__objects

    def new(self, obj):
        # Your new method logic here
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        # Your save method logic here
        data = {}
        for key, obj in self.__objects.items():
            data[key] = obj.to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(data, file)

    def reload(self):
        # Your reload method logic here
        try:
            with open(self.__file_path, 'r') as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name, obj_id = key.split('.')
                    obj = globals()[class_name](**value)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass
