from robotController import *

#   The main program basically just reads the command from the command line and passes it to the roboController
#   An extra command "EXIT" has been implemented to exit the program without force closing it

#   If the program is launched wit the verbose parameter -v, the roboControlles is set to verbose mode, and every
#   command will give a response string
#   The user can also choose to save the commands in a file and give the filename as parameter.

import argparse

if  __name__ == '__main__':
    parser = argparse.ArgumentParser(description='SimpleRobot simulator')
    parser.add_argument("-v", "--verbose", help="Status message after every command", action="store_true")
    parser.add_argument('filename', nargs='?', type=argparse.FileType('r'), help="defines input file for commands")
    args = parser.parse_args()

    rcontroller = RobotController()
    # if -v is given
    if args.verbose:
        rcontroller.setVerbose(True)
    # if a file is given
    if args.filename:
        for s in args.filename.readlines():
            print(s.strip())
            response = (rcontroller.execCommand(s.strip()))
            # avoid empty prints
            if len(response) > 0:
                print(response)
    # else read from command line
    else:
        while True:
            command = input()
                #   closes the program
            if command == "EXIT":
                break

            response = (rcontroller.execCommand(command))
            # avoid empty prints
            if len(response) > 0:
                print(response)