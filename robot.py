from robot_controller import *

#   The main program basically just reads the command from the command line and passes it to the roboController
#   An extra command "EXIT" has been implemented to exit the program without force closing it

#   If the program is launched wit the verbose parameter -v, the roboControlles is set to verbose mode, and every
#   command will give a response string

if  __name__ == '__main__':
    rcontroller = RobotController()
    verbose = True
    while True:
        command = input()
        #   closes the program
        if command == "EXIT":
            break

        response = (rcontroller.execCommand(command))
        if len(response) > 0: print(response)
