#!/usr/bin/python3
import pickle

class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print(f"Name: {self.name}\nAge: {self.age}\nIs Student: {self.is_student}")

    def serialize(self, filename):
        try:
            with open(filename, "wb") as file:
                pickle.dump(self, file)
        except (OSError, pickle.PickleError) as e:
            print(f"Error serializing to {filename}: {e}")

    @classmethod
    def deserialize(cls, filename):
        try:
            with open(filename, "rb") as file:
                loaded_data = pickle.load(file)
                if isinstance(loaded_data, cls):
                    return loaded_data
                else:
                    print("Loaded object is not of type CustomObject")
                    return None
        except (OSError, pickle.PickleError) as e:
            print(f"Error deserializing from {filename}: {e}")
            return None
