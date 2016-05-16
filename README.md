# SimpleRobot

Implementation of a robot able to accept basic movement commands.

## Environments

The application has been implemented using PYHTON 3.5.1 and tested on Windows 10. Only basic Python libraries has been used.

The code will not run on PYTHON 2.x



## Usage Instructions

The program is launched using: "python robot.py" an additional parameter "-v" can be used to activate verbose mode
which will give a response after every command.

Once started the following commands can be used:

- PLACE x,y,facedirection
Places the robot on the grid with the given parameters.

x and y has to be integer values from 0 to 4
facedirection has to be one of the following strings: "NORTH" "EAST" "SOUTH" "WEST"

This is the first command that has to be given to the robot. If not placed correctly the robot will ignore
all commands


- LEFT
The robot will turn 90° left

- RIGHT
The robot will turn 90° right

- MOVE
The robot will move one square in the facing direction. If the robot would fall of the  the table the command is ignored

- REPORT
Will report the x,y and the direction the robot is facing

- EXIT
Exits the program


## Testing Instructions

Two unit test has been implemented to test the robot and the robotController:

use:
"pyhton simple_robot_test.py"
"pyhton robot_controller_test.py"



## Design

The programm is composed of three parts:

- Main program (robot.py):
Reads from and writes to the console

- Robot controller (robot_controller.py)
Checks commands for errors and passes them to the robot

- Simple robot (simple_robot.py)
Actual robot logic, implemented as a simple state machine. All the inputs and outputs of the functions are integer values


The main program reads the input from the console and passes it to the roboController usig the execCommand() function.
The controller checks if there are any errors in the command or the parameters and if everything is alright it passes
the command to the simple_robot calling the associated function.
The simple_robot will then try to execute the command, if an error happens the function will return an error, the robo_controller
is then again responsable to interpret the error and if verbose mode is chosen return an error message. The main
program will then print the response on the console.

