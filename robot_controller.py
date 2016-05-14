from simple_Robot import *

# The RobotController interprets the commands given as input, checks them for errors and passes it to the robot.
# At the moment there is only a single robot in use. More commands could be added to create
from enum import Enum

class RcResponseStr(Enum):
    invParams       =   "Invalid parameters. usage: PLACE x y facedirection"
    invCommand      =   "Invalid command"
    invX            =   "Invalid x parameter"
    invY            =   "Invalid y parameter"
    invDir          =   "Invalid direction parameter"
    invPlace        =   "Cannot place here"
    invMoveBorder   =   "Boarder reached, command ignored"
    invParamsNum    =   "Need more parameters to place robot. usage: PLACE x y facedirection"
    comAccept       =   "Command accepted"
    notPlaced       =   "Robot not placed. Use: PLACE x,y,facedirection"


class RobotController:

    _directionlookup = {"NORTH":0 , "EAST":1 , "SOUTH":2 , "WEST":3 }
    _robot = SimpleRobot()
    _commandstring = ""
    _verbose = False

#    The command switcher interprets the string given as input and calls the associated function.
#    (Similar to case/switch used in other languages)
#    To add a new command define a new function and add a new statement in the switcher dictionary below.

    def __commandSwitcher(self,argument):
        switcher = {
            "PLACE"     : self.__place,
            "LEFT"      : self.__left,
            "RIGHT"     : self.__right,
            "MOVE"      : self.__move,
            "REPORT"    : self.__report,
        }

        # command stored locally to give all the functions access to it.
        # (i.e. PLACE needs to interpet also the parameters)


        func = switcher.get(argument, lambda: RcResponseStr.invCommand.value)
        result = func()

        #   Report ist the only command allowed to give a respone whitout verbose mode
        if argument == "REPORT" or self._verbose:
            return result
        else:
            return ""

    #   Functions used by the command switcher
    def __place(self):

        returntxt = ""
        try:
            commandsplit = self._commandstring.split(" ")[1].split(",")
        except:
            return RcResponseStr.invParams.value

        if len(commandsplit) > 2:
            # check if the x any y values are Integers
            x,y,facedirection = 0, 0, 0
            try:
                x = int(commandsplit[0])
            except ValueError:
                returntxt = RcResponseStr.invX.value
            try:
                y = int(commandsplit[1])
            except ValueError:
                returntxt = RcResponseStr.invY.value
            # check direction parameter
            if commandsplit[2] in self._directionlookup:
               facedirection = self._directionlookup[commandsplit[2]]
            else:
                returntxt = RcResponseStr.invDir.value

            # if all the parameters are correct, try to place the robot with those
            if returntxt == "":
                if self._robot.place(x,y,facedirection) == RoboResults.wrongPlacing:
                    returntxt = RcResponseStr.invPlace.value
                else:
                    returntxt = "Robot placed"

        #   if there where not enough parameters
        else:
            returntxt = RcResponseStr.invParamsNum.value

        return returntxt

    def __left(self):
        if self._robot.turn_left() == RoboResults.commandAccepted.value:
            return RcResponseStr.comAccept.value
        else:
            return RcResponseStr.notPlaced.value

    def __right(self):
        if self._robot.turn_right() == RoboResults.commandAccepted.value:
            return RcResponseStr.comAccept.value
        else:
            return RcResponseStr.notPlaced.value

    def __move(self):
        r = self._robot.move()
        if r == RoboResults.commandAccepted.value:
            return RcResponseStr.comAccept.value
        elif r == RoboResults.notPlaced.value:
            return RcResponseStr.notPlaced.value
        elif r == RoboResults.borderReached.value:
            return RcResponseStr.invMoveBorder.value

    def __report(self):
        x,y,face = self._robot.report()
        directions = ["NORTH","EAST","SOUTH","WEST"]
        return str(x) + "," + str(y) + "," +  directions[face]
    #
    def execCommand(self,command):
        # save the commandstring to extract the parameters
        self._commandstring = command
        # extract the command and call the switcher
        returntxt = self.__commandSwitcher(self._commandstring.split()[0])
        return returntxt