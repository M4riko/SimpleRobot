'''
This class provides the simulation of a simple robot able to move on a square gridded surface

The robot accepts 5 commands:

- Place (robot on a grid)
- Turn left
- Turn right
- Move (forward)
- Report (returns position and facing of the robot)

Since the problem is deterministic (the robot always knows where he is on the grid) there is no need to create an actual grid
instead the position and facing is stored in internal variables and updated on any command.
The robot can be moved once it is placed, it will ignore commands given before the first place command.


'''

from enum import Enum

#   This enumeration contains the results a robot can send to the controller
class RoboResults(Enum):
    commandAccepted = 1
    notPlaced = -1
    borderReached = -2
    wrongPlacing = -3

GRIDSIZE = 5

class SimpleRobot:
    # Position of the robot on the grid
    _x = -1
    _y = -1
    # 0:North 1:East  2:South  3:West
    _facing = -1
    _placed = False

    # Turns the robot left or right
    def turn_left(self):
        if not self._placed:
            return RoboResults.notPlaced
        else:
            self._facing = (self._facing - 1) % 4
            return RoboResults.commandAccepted.value

    def turn_right(self) -> object:
        if not self._placed:
            return RoboResults.notPlaced
        else:
            self._facing = (self._facing + 1) % 4
            return RoboResults.commandAccepted.value

    # Moves the robot one square in the direction it is facing
    def move(self):
        if self._facing == 0:
            if self._y < (GRIDSIZE - 1):
                self._y += 1
                return RoboResults.commandAccepted.value
            else:
                return RoboResults.borderReached.value
        elif self._facing == 1:
            if self._x < (GRIDSIZE - 1):
                self._x += 1
                return RoboResults.commandAccepted.value
            else:
                return RoboResults.borderReached.value
        elif self._facing == 2:
            if self._y > 0:
                self._y -= 1
                return RoboResults.commandAccepted.value
            else:
                return RoboResults.borderReached.value
        elif self._facing == 3:
            if self._x > 0:
                self._x -= 1
                return RoboResults.commandAccepted.value
            else:
                return RoboResults.borderReached.value

    # reports the position and facing direction of the robot
    def report(self):
        return self._x, self._y, self._facing

    #   Places the robot in a certain position with given facing, can be called multiple times
    def place(self, pos_x=0, pos_y=0, face_direction=0):
        # check if the given parameters are on the grid and the direction is valid
        if 0 <= pos_x < GRIDSIZE and 0 <= pos_y < GRIDSIZE and pos_y < GRIDSIZE and 0 <= face_direction < 4:
            self._x = pos_x
            self._y = pos_y
            self._facing = face_direction
            self._placed = True
            return RoboResults.commandAccepted.value
        else:
            return RoboResults.wrongPlacing.value