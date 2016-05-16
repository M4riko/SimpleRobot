from simpleRobot import *
from enum import Enum


'''
The RobotController interprets the commands given as input, checks them for errors and passes it to the robot.
At the moment there is only a single robot in use. More commands could be added to create

The if verbose mode is set by calling the setVerbose(True) the execCommand function will return a status string
after every command. (See RcResponse) else an empty string is returned
'''

class RcResponse(Enum):
    invParams       =   "Invalid parameters. usage: PLACE x,y,facedirection"
    invCommand      =   "Invalid command"
    invPlace        =   "Cannot place here"
    invMoveBorder   =   "Boarder reached, command ignored"
    comAccept       =   "Command accepted"
    notPlaced       =   "Robot not placed. Use: PLACE x,y,facedirection"
    Placed          =   "Robot placed"

class RobotController:
    _directionlookup = {"NORTH":0 , "EAST":1 , "SOUTH":2 , "WEST":3 }
    _robot = None
    _commandstring = ""
    _verbose = False

    def __init__(self):
        self._robot = SimpleRobot()

#    The command switcher interprets the string given as input and calls the associated function.
#    (Similar to case/switch used in other languages)
#    To add a new command define a new function and add a new statement in the switcher dictionary below.

    def setVerbose(self,verboseMode):
        self._verbose = verboseMode

    #   Functions used by the command switcher
    def __place(self):

        returntxt = ""
        try:
            commandsplit = self._commandstring.split(" ")[1].split(",")
        except:
            return RcResponse.invParams.value

        if len(commandsplit) > 2:
            # check if the x any y values are Integers
            x,y,facedirection = 0, 0, 0
            try:
                x = int(commandsplit[0])
            except ValueError:
                returntxt = RcResponse.invParams.value
            try:
                y = int(commandsplit[1])
            except ValueError:
                returntxt = RcResponse.invParams.value
            # check direction parameter
            if commandsplit[2] in self._directionlookup:
               facedirection = self._directionlookup[commandsplit[2]]
            else:
                returntxt = RcResponse.invParams.value

            # if all the parameters are correct, try to place the robot with those
            if returntxt == "":
                if self._robot.place(x,y,facedirection) == RoboResults.wrongPlacing.value:
                    returntxt = RcResponse.invPlace.value
                else:
                    returntxt = RcResponse.Placed.value

        #   if there where not enough parameters
        else:
            returntxt = RcResponse.invParams.value
        return returntxt

    def __left(self):
        if self._robot.turn_left() == RoboResults.commandAccepted.value:
            return RcResponse.comAccept.value
        else:
            return RcResponse.notPlaced.value

    def __right(self):
        if self._robot.turn_right() == RoboResults.commandAccepted.value:
            return RcResponse.comAccept.value
        else:
            return RcResponse.notPlaced.value

    def __move(self):
        r = self._robot.move()
        if r == RoboResults.commandAccepted.value:
            return RcResponse.comAccept.value
        elif r == RoboResults.notPlaced.value:
            return RcResponse.notPlaced.value
        elif r == RoboResults.borderReached.value:
            return RcResponse.invMoveBorder.value

    def __report(self):
        x,y,face = self._robot.report()
        directions = ["NORTH","EAST","SOUTH","WEST"]
        return str(x) + "," + str(y) + "," +  directions[face]

    def execCommand(self,command):
        # save the commandstring locally to extract the parameters (i.e. PLACE command)
        self._commandstring = command
        argument = ""
        # extract the command and call the switcher
        if self._commandstring.split():
            argument = self._commandstring.split()[0]

        switcher = {
            "PLACE"     : self.__place,
            "LEFT"      : self.__left,
            "RIGHT"     : self.__right,
            "MOVE"      : self.__move,
            "REPORT"    : self.__report,
        }
        func = switcher.get(argument, lambda: RcResponse.invCommand.value)
        result = func()

    #   Report ist the only command allowed to give a response without verbose mode
        if argument == "REPORT" or self._verbose:
            return result
        else:
            return ""