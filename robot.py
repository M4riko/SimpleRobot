from robot_controller import *


if  __name__ == '__main__':
    rcontroller = RobotController()
    verbose = True
    while True:
        command = input()

        if command == "EXIT":
            break

        response = (rcontroller.execCommand(command))
        print(response)
