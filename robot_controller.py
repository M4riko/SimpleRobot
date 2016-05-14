from simple_Robot import *
import sys
# The RobotController interprets the commands given as input, checks them for errors and passes it to the robot.

# At the moment there is only a single robot in use. More commands could be added to create



class RobotController:

    _directionlookup = {"NORTH":0 , "EAST":1 , "SOUTH":2 , "WEST":3 }
    _robot = SimpleRobot()
    #
    _commandstring = ""

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
        _commandstring = argument

        func = switcher.get(argument, lambda: "Invalid command")
        return func()


#   Every command
    def __place(self):

        returntxt = ""
        try:
            commandsplit = self._commandstring.split(" ")[1].split(",")
        except:
            return "Invalid parameters PLACE x y facedirection"

        if len(commandsplit) > 2:
            # check if the x any y values are Integers
            x,y,facedirection = 0, 0, 0
            try:
                x = int(commandsplit[0])
            except ValueError:
                returntxt = "Invalid x parameter"
            try:
                y = int(commandsplit[1])
            except ValueError:
                returntxt = "Invalid y parameter"
            # check directiom parameter
            if commandsplit[2] in self._directionlookup:
               facedirection = self._directionlookup[commandsplit[2]]
            else:
                returntxt = "Invalid face direction"

            # if all the parameters are correct, try to place the robot with those
            if returntxt == "":
                if self._robot.place(x,y,facedirection) == RoboResults.wrongPlacing:
                    returntxt = "Cannot place the robot there"
                else:
                    returntxt = "Robot placed"

        #   if there where not enough parameters
        else:
            returntxt = "Need more parameters to place robot. usage: PLACE x y facedirection"

        return returntxt

    def __left(self):
        if self._robot.turn_left() == RoboResults.commandAccepted:
            return "Command accepted"
        else:
            return "Robot not placed"


    def __right(self):
        if self._robot.turn_right() == RoboResults.commandAccepted:
            return "Command accepted"
        else:
            return "Robot not placed"

    def __move(self):
        r = self._robot.move()
        if r == RoboResults.commandAccepted:
            return "Command accepted"
        elif r == RoboResults.notPlaced:
            return "Robot not placed"
        elif r == RoboResults.borderReached:
            return "Border reached"

    def __report(self):
        x,y,face = self._robot.report()
        directions = ["NORTH","EAST","SOUTH","WEST"]
        return str(x) + "," + str(y) + "," +  directions[face]

    def execCommand(self,command):
        self._commandstring = command
        command = self._commandstring.split()[0]
        returntxt = self.__commandSwitcher(command)
        return returntxt




