# SimpleRobot

Implementation of a robot that moves on a 5x5 gridded table.

## Environments

The application has been implemented using PYHTON 3.5.1 and tested on Windows 10. Only basic Python libraries have been used.

The code will not run on PYTHON 2.x


## Usage Instructions

The program is launched using: "python robot.py" an additional parameter "-v" can be used to activate verbose mode
which will give a response after every command.
The user can also choose to save the commands in a file and give the filename as parameter.


usage: robot.py [-h] [-v] [filename]

Once started the following commands can be used:

- PLACE : x,y,facedirection
Places the robot on the grid with the given parameters.

x and y have to be integer values from 0 to 4
facedirection has to be one of the following strings: "NORTH" "EAST" "SOUTH" "WEST"

This is the first command that has to be given to the robot. If not placed correctly the robot will ignore
all commands


- LEFT : The robot will turn 90° left

- RIGHT : The robot will turn 90° right

- MOVE : The robot will move one square in the facing direction. If the robot would fall of the  the table the command is ignored

- REPORT : Will report the x,y and the direction the robot is facing

- EXIT : Exits the program


## Testing Instructions

Two unit test has been implemented to test the robot and the robotController:
use:
"pyhton simpleRobotTest.py" and "pyhton robotControllerTest.py"


####simple_robot_test:
-	Test different values for place command
-	Test different values for place command
-	Test if report returns the right value
-	Test turn functions
-	Test movement in every direction
-	Test that robot does not fall over one of the 4 borders
-	Test if a second place command works

####command handler test
-	Test return string for every command whitout verbose mode : Only PLACE should give a return value
-	Test return string for every command with verbose mode
-	Test return string for invalid place 
-	Test return string for different PLACE commands
-	Test return string for commands with placed robot
-	Test return string for movement commands that would make the robot fall off the table
-	2 Functionallity tests: Command sequences that should move the robot from one position to another

## Design

```
+------------------+     Command      +----------------------+     executes     +------------------+
|                  |     String       |                      |     command      |                  |
|      main        |  +----------->   |  RobotHandler        |  +------------>  | SimpleRobot      |
|                  |                  |                      |                  |                  |
| - console I/O    |                  | -com. interpretation |                  | -Robot logic     |
| - file I/O       |                  | -error hadling       |                  |                  |
|                  |  <-----------+   |                      |  <------------+  |                  |
|                  |     Response     |                      |     gives        |                  |
|                  |     String       |                      |     Response     |                  |
+------------------+                  +----------------------+                  +------------------+

```


The programm is composed of three parts:

- Main program (robot.py):
Reads from and writes to the console

- Robot controller (robotController.py)
Checks commands for errors and passes them to the robot

- Simple robot (simpleRobot.py)
Actual robot logic, implemented as a simple state machine. All the inputs and outputs of the functions are integer values


While implementing this project I was imagining a little toy robot able to accept only simple commands. That’s why the class works entirely
with integer values. Also everything the robot does is encapsulated in this class which could be easily extended to send the commands (via RF or cable) to
an actual toy robot.
The robothandler works as command interpreter, the commands are passed via the execCommand() function. If the verbose mode is off only the REPORT command returns a string
and all errors and warnings are ignored. The class is designed so that new commands can be implemented easily.
Since Python does not have a case-switch statement i used dictionary mapping for functions which also makes the code more readable.
To add a new command you simply need to implement a new function and add the function to the dictionary. 
It was not requested that every command gives an answer so a verbose mode has been added to the class, so that the user can decide if he wants the answers or not



## Discussion

The Project is an implementation of the Model–view–presenter pattern:

Passive view: main program -> interacts with the user
Presenter: RoboController -> interacts with the model and formats display for the view
Model:	simpleRobot -> acts on inputs and generates data for the output

The model is a derived form of the Model-view-controller but the view in this case is not a separate enitiy. Moreover the presenter
acts as "Middle Men" between the actual user interface and the model. I choose this model because it allowes a complete separation
of the command interpretation and the changes in the model, also it would be straight forward to change how the data is delivered to the presenter
(i.e: over a socket connection)

