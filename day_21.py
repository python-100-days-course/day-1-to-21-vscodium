# 100 Days of Code: The Complete Python Pro Bootcamp by Dr. Angela Yu
# Day 21 - Intermediate - Build the Snake Game Part 2 (different files): Class Inheritance & Slicing List and Dictionaries

# Example of class inheritance:
class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale.")

class Fish(Animal): # In () is a class that's inherited
    def __init__(self):
        super().__init__() # Code for inheriting the attributes

    def breathe(self):
        super().breathe() # Code to inherit a specific method from superclass to subclass
        print("Doing this under water.")

    def swim(self):
        print("Moving in water.")

nemo = Fish()
nemo.swim()
nemo.breathe()
print(nemo.num_eyes)

# Example of list slicing:
piano_keys = ["a", "b", "c", "d", "e", "f", "g"]
piano_tuple = ["do", "re", "mi", "fa", "so", "la", "ti"]
piano_keys_sliced = piano_keys[2:5] # c-e
piano_keys_sliced_2 = piano_keys[2:] # c and the rest
piano_keys_sliced_3 = piano_keys[:5] # e and everything before
piano_keys_sliced_4 = piano_keys[2:5:2] # c to e, skip every other one, so just c and e
piano_keys_sliced_5 = piano_keys[::2] # obtain every other one
piano_keys_sliced_6 = piano_keys[::-1] # reverse the list
piano_tuple_sliced = piano_tuple[2:5] # also works with tuples
print(f"piano_keys = {piano_keys}")
print(f"piano_keys_sliced = {piano_keys_sliced}")
print(f"piano_keys_sliced_2 = {piano_keys_sliced_2}")
print(f"piano_keys_sliced_3 = {piano_keys_sliced_3}")
print(f"piano_keys_sliced_4 = {piano_keys_sliced_4}")
print(f"piano_keys_sliced_5 = {piano_keys_sliced_5}")
print(f"piano_keys_sliced_6 = {piano_keys_sliced_6}")
print(f"piano_tuple = {piano_tuple}")
print(f"piano_tuple_sliced = {piano_tuple_sliced}")