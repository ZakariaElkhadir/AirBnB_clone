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
        return FileStorage.__objects

    def new(self, obj):
        id = obj.to_dict()["id"]
        class_name = obj.to_dict()["__class__"]
        key_name = class_name +"."+id
        FileStorage.__objects[key_name] = obj
    
    def save(self):
        path = FileStorage.__file_path
        data = dict(FileStorage.__objects)
        for key, value in data.items():
            data[key] = value.to_dict()
        with open(path, 'w') as file:
            json.dump(data, file)
    
    def reload(self):
        if os.path.exists(self.__file_path) is True:
            with open(self.__file_path, 'r') as file:
                for value in json.load(file).values():
                    self.new(dct[value['__class__']](**value))
