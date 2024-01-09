#!/usr/bin/python3
import json
import os.path
from models.base_model import BaseModel
class FileStorage:
    """_summary_

    Returns:
        _type_: _description_
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self):
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj
    
    def save(self):
        serialized_objects = {}
        for key, obj in self.__objects.items():
            serialized_objects[key] = obj.to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(serialized_objects, file)
    
    def reload(self):
        if os.path.exists(self.__file_path) is True:
            with open(self.__file_path, 'r') as file:
                for value in json.load(file).values():
                    self.new(dct[value['__class__']](**value))
