#!/usr/bin/python3
"""
=============================
Module with the class Rectangle
=============================
"""


import uuid
from datetime import datetime


class BaseModel:
    """
    base class for the project
    """

    def __init__(self, *args, **kwargs):
        """
        The constructor of the class BaseModel
        """
        if len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key == "updated_at" or key == "created_at":
                    value = datetime.fromisoformat(value)
                setattr(self, key, value)
            return

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        The string representation of the class BaseModel
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        updates the public instance attribute updated_at
        with the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values
        of __dict__ of the instance
        """
        dict = {**self.__dict__}
        dict['__class__'] = type(self).__name__
        dict['created_at'] = dict['created_at'].isoformat()
        dict['updated_at'] = dict['updated_at'].isoformat()

        return dict


my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89
print(my_model.id)
print(my_model)
print(type(my_model.created_at))
print("--")
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

print("--")
my_new_model = BaseModel(**my_model_json)
print(my_new_model.id)
print(my_new_model)
print(type(my_new_model.created_at))

print("--")
print(my_model is my_new_model)

# guillaume@ubuntu:~/AirBnB$ ./test_base_model_dict.py
# 56d43177-cc5f-4d6c-a0c1-e167f8c27337
# [BaseModel] (56d43177-cc5f-4d6c-a0c1-e167f8c27337) {'id': '56d43177-cc5f-4d6c-a0c1-e167f8c27337', 'created_at': datetime.datetime(2017, 9, 28, 21, 3, 54, 52298), 'my_number': 89, 'updated_at': datetime.datetime(2017, 9, 28, 21, 3, 54, 52302), 'name': 'My_First_Model'}
# <class 'datetime.datetime'>
# --
# {'id': '56d43177-cc5f-4d6c-a0c1-e167f8c27337', 'created_at': '2017-09-28T21:03:54.052298', '__class__': 'BaseModel', 'my_number': 89, 'updated_at': '2017-09-28T21:03:54.052302', 'name': 'My_First_Model'}
# JSON of my_model:
#     id: (<class 'str'>) - 56d43177-cc5f-4d6c-a0c1-e167f8c27337
#     created_at: (<class 'str'>) - 2017-09-28T21:03:54.052298
#     __class__: (<class 'str'>) - BaseModel
#     my_number: (<class 'int'>) - 89
#     updated_at: (<class 'str'>) - 2017-09-28T21:03:54.052302
#     name: (<class 'str'>) - My_First_Model
# --
# 56d43177-cc5f-4d6c-a0c1-e167f8c27337
# [BaseModel] (56d43177-cc5f-4d6c-a0c1-e167f8c27337) {'id': '56d43177-cc5f-4d6c-a0c1-e167f8c27337', 'created_at': datetime.datetime(2017, 9, 28, 21, 3, 54, 52298), 'my_number': 89, 'updated_at': datetime.datetime(2017, 9, 28, 21, 3, 54, 52302), 'name': 'My_First_Model'}
# <class 'datetime.datetime'>
# --
# False