# Tests the functionality of the simple_Robot class
import unittest

from simpleRobot import *

class TestRobot(unittest.TestCase):

    _robot = 0
    # this method is called before every test, it creates a new robot object used in the tests
    @classmethod
    def setUpClass(cls):
        cls._robot = SimpleRobot()

    #   test  place() function
    def test_place00(self):
        self.assertEqual(self._robot.place(0, 0, 0), RoboResults.commandAccepted.value)

    def test_place22(self):
        self.assertEqual(self._robot.place(2, 2, 0), RoboResults.commandAccepted.value)

    def test_placeneg11(self):
        self.assertEqual(self._robot.place(-1, -1, 0), RoboResults.wrongPlacing.value)

    def test_place66(self):
        self.assertEqual(self._robot.place(6, 6, 0), RoboResults.wrongPlacing.value)

    def test_place111(self):
        self.assertEqual(self._robot.place(1, 1, 1), RoboResults.commandAccepted.value)

    def test_place11n1(self):
        self.assertEqual(self._robot.place(1, 1, -1), RoboResults.wrongPlacing.value)

    def test_place11n5(self):
        self.assertEqual(self._robot.place(1, 1, 4), RoboResults.wrongPlacing.value)


    # test report() function
    def test_report1(self):
        self._robot.place(1, 1, 0)
        self.assertEqual(self._robot.report(), (1, 1, 0))

    def test_report2(self):
        self._robot.place(3, 1, 2)
        self.assertEqual(self._robot.report(), (3, 1, 2))

    # turn left() and right() function
    def test_turnRight(self):
        self._robot.place(1, 1, 0)
        self._robot.turn_right()
        self.assertEqual(self._robot.report(), (1, 1, 1))

    def test_turnLeft(self):
        self._robot.place(1, 1, 0)
        self._robot.turn_left()
        self.assertEqual(self._robot.report(), (1, 1, 3))

    # test basic movement
    def test_moveNorth(self):
        self._robot.place(1, 1, 0)
        self.assertEqual(self._robot.move(),RoboResults.commandAccepted.value )
        self.assertEqual(self._robot.report(), (1, 2, 0))

    def test_moveEast(self):
        self._robot.place(1, 1, 1)
        self.assertEqual(self._robot.move(),RoboResults.commandAccepted.value )
        self.assertEqual(self._robot.report(), (2, 1, 1))

    def test_moveSouth(self):
        self._robot.place(1, 1, 2)
        self.assertEqual(self._robot.move(),RoboResults.commandAccepted.value )
        self.assertEqual(self._robot.report(), (1, 0 , 2))

    def test_moveWest(self):
        self._robot.place(1, 1, 3)
        self.assertEqual(self._robot.move(),RoboResults.commandAccepted.value )
        self.assertEqual(self._robot.report(), (0, 1 , 3))


    # try to fall off
    def test_moveFallNorth(self):
        self._robot.place(0, 4, 0)
        self.assertEqual(self._robot.move(), RoboResults.borderReached.value )
        self.assertEqual(self._robot.report(), (0, 4 , 0))

    def test_moveFallEast(self):
        self._robot.place(4, 4, 1)
        self.assertEqual(self._robot.move(), RoboResults.borderReached.value )
        self.assertEqual(self._robot.report(), (4, 4 , 1))

    def test_moveFallSouth(self):
        self._robot.place(4, 0, 2)
        self.assertEqual(self._robot.move(), RoboResults.borderReached.value )
        self.assertEqual(self._robot.report(), (4, 0 , 2))

    def test_moveFallWest(self):
        self._robot.place(0, 0, 3)
        self.assertEqual(self._robot.move(), RoboResults.borderReached.value )
        self.assertEqual(self._robot.report(), (0, 0 , 3))

    # test replace
    def test_moveReplace(self):
        self._robot.place(0, 0, 3)
        self._robot.place(2, 1, 1)
        self.assertEqual(self._robot.report(), (2, 1 , 1))

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestRobot)
    unittest.TextTestRunner(verbosity=2).run(suite)
