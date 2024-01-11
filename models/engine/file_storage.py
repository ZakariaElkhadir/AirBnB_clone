#!/usr/bin/python3
"""class model"""
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
        """all returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """new: sets in __object the obj with key class_name id"""
        id = obj.to_dict()["id"]
        class_name = obj.to_dict()["__class__"]
        key_name = class_name + "." + id
        FileStorage.__objects[key_name] = obj

    def save(self):
        """save - serializes __objects to the JSON file"""
        path = FileStorage.__file_path
        data = dict(FileStorage.__objects)
        for key, value in data.items():
            data[key] = value.to_dict()
        with open(path, 'w') as file:
            json.dump(data, file)

    def reload(self):
        """reload: Deserialize the JSON file\
__file_path to __objects, if it exists."""
        try:
            with open(FileStorage.__file_path) as file:
                obj_dict = json.load(file)
                for obj in obj_dict.values():
                    className = obj["__class__"]
                    del obj["__class__"]
                    self.new(eval(className)(**obj))
        except FileNotFoundError:
            return
