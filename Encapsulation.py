# Another example of encapsulation
class Robot:
    def __init__(self, robot_1, robot_2):
        self.robot_1 = robot_1  # Public attribute
        #self.__robot_1 => # Private attribute
        self.robot_2 = robot_2  # Public attribute

    def display_robots(self):
        print(f"Robot 1: {self.robot_1}, Robot 2: {self.robot_2}")

r = Robot("Alpha", "Beta")
r.display_robots() # Output: Robot 1: Alpha, Robot 2: Beta

# You can change values directly
r.robot_1 = "Gamma"
r.robot_2 = "Delta"
r.display_robots() # Output: Robot 1: Gamma, Robot 2: Delta
