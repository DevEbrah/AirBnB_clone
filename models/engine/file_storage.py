#!/usr/bin/python3
"""This is the file storage class for AirBnB"""
import json
from models.base_model import BaseModel
import shlex

class FileStorage:
    """This class serializes instances to a JSON file and deserializes JSON file to instatnces"""
    __file__path = "file.json"
    _objects ={}

    def all(self, cls=None):
        """returns a dictionary
        Return:
        returns a dictionary of __object
        """
        dic = {}
        if cls:
            dictionary =self._objects
            for key in dictionary:
                partition = key.replace('.', '')
                partition = shlex.split(partition)
                if (partition[0] == cls._name_):
                    dic[key] = self._objects[key]
            return (dic)
        else:
            return self._objects

    def new(self, obj):
        """sets __object to given obj
        Args:
            obj: given object
        """
        if obj:
            key = "{}.{}".format(type(obj)._name_, obj.id)
            self._objects[key] = obj

    def save(self):
    	"""serialize the file path to JSON file path
        """
        my_dict = {}
        for key, value in self._objects.items():
            my_dict[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(my_dict, f)

    def reload(self):
        """serialize the file path to JSON file path
        """
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                for key, value in (json.load(f)).items():
                    value = eval(value["_class_"])(**value)
                    self._objects[key] = value
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """ delete an existing element
        """
        if obj:
            key = "{}.{}".format(type(obj)._name_, obj.id)
            del self._objects[key]

    def close(self):
    	"""calls reload()
    	"""
    	self.reload()
