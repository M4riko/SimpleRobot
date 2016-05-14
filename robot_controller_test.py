# Tests the functionality of the simple_Robot class
import unittest


from robot_controller import *

class TestRobot(unittest.TestCase):

    _robotController = 0
    # this method is called before every test, it creates a new robot object used in the tests
    @classmethod
    def setUpClass(cls):
        cls._robotController = RobotController()
        cls._robotController._verbose = True

    def test_Parser1(self):
        self.assertEqual(self._robotController.execCommand("ASDF"), RcResponseStr.invCommand.value )


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestRobot)
    unittest.TextTestRunner(verbosity=2).run(suite)
