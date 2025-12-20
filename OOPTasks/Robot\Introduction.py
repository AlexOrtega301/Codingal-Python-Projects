# Robot blueprint (Class)
class Robot:
    def __init__(self, name):
        self.name = name  # robot's internal memory

    def introduce(self):
        print(f"Hello Human! 🤖 My name is {self.name}.")


# Creating robot objects
tom = Robot("Tom")
jerry = Robot("Jerry")

# Robots introduce themselves
tom.introduce()
jerry.introduce()
