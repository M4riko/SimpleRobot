# SimpleRobot

Implementation of a simple robot program which takes movement commands as input and

# Environments

The application has been implemented using PYHTON 3.5.1 and tested on Windows 10. Since only basic Python libraries
has been used the code should run un every operating system.

The code will not run on PYTHON 2.x



# Operating Instructions

The program is launched using: "python robot.py" an additional parameter "-v" can be used to activate verbose mode
which will give a response after every command.

Once started the following commands can be used:

-> PLACE x,y,facedirection
Places the robot on the grid with the given parameters.

x and y has to be integer values from 0 to 4
facedirection has to be one of the following strings: "NORTH" "EAST" "SOUTH" "WEST"

This is the first command that has to be given to the robot. If not placed correctly the robot will ignore
all commands


-> LEFT
The robot will turn 90° on the left

-> RIGHT
The robot will turn 90° on the right

-> MOVE
The robot will move one square in the facing direction. If the robot would fall of the  the table the command is ignored

-> REPORT
Will report the x,y and the direction the robot is facing

-> EXIT
Exits the program


