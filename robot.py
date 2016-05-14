from robot_controller import *


if  __name__ == '__main__':
    r = RobotController()
    
    while True:
        command = input()
        print(r.execCommand(command))
