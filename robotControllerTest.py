# Tests the functionality of the simple_Robot class
import unittest

CommandTestSequence1 = ["PLACE 1,1,NORTH", "MOVE","MOVE","MOVE","MOVE","REPORT"]
CommandTestSequence1Result = "1,4,NORTH"

CommandTestSequence2 = ["PLACE 1,1,SOUTH", "MOVE","MOVE","LEFT","LEFT","MOVE","MOVE","MOVE","RIGHT","RIGHT","RIGHT",
                        "MOVE","MOVE","REPORT"]

CommandTestSequence2Result = "0,3,WEST"

from robotController import *

class TestRobotController(unittest.TestCase):

    _robotController = 0
    # this method is called before every test, it creates a new robot object used in the tests
    @classmethod
    def setUp(self):
        self._robotController = RobotController()

    @classmethod
    def tearDownClass(cls):
        cls._robotController = None

    # whitout verbose mode no cmmand except REPORT should return an empty string
    def test_NV_ResponseInvalid1(self):
        self.assertEqual(self._robotController.execCommand("ASDF"), "" )

    def test_NV_ResponseInvalid2(self):
        self.assertEqual(self._robotController.execCommand("ASDF asd 1"), "" )

    def test_NV_ResponseInvalid3(self):
        self.assertEqual(self._robotController.execCommand("1 2  ASDF"), "" )

    def test_NV_PLACE1(self):
        self.assertEqual(self._robotController.execCommand("PLACE"), "" )

    def test_NV_PLACE2(self):
        self.assertEqual(self._robotController.execCommand("PLACE 1,1,NORTH"), "" )

    def test_NV_LEFT(self):
        self.assertEqual(self._robotController.execCommand("RIGHT"), "" )

    def test_NV_LEFT(self):
        self.assertEqual(self._robotController.execCommand("LEFT"), "" )

    def test_NV_MOVE(self):
        self.assertEqual(self._robotController.execCommand("MOVE"), "" )
    #   Test if report gives an answer
    def test_NV_REPORT(self):
        r = self._robotController.execCommand("REPORT")
        self.assertGreater(len(r), 0 )


    #   Tests verbose mode
    #   invalid place commands
    def test_V_PLACE_invalid1(self):
        self._robotController.setVerbose(True)
        self.assertEqual(self._robotController.execCommand("PLACE 1 1 2"), "Invalid parameters. usage: PLACE x,y,facedirection" )

    def test_V_PLACE_invalid1(self):
        self._robotController.setVerbose(True)
        self.assertEqual(self._robotController.execCommand("PLACE 1,1,2"), "Invalid parameters. usage: PLACE x,y,facedirection" )

    def test_V_PLACE_invalid2(self):
        self._robotController.setVerbose(True)
        self.assertEqual(self._robotController.execCommand("PLACE a,1"), "Invalid parameters. usage: PLACE x,y,facedirection" )

    def test_V_PLACE_invalid3(self):
        self._robotController.setVerbose(True)
        self.assertEqual(self._robotController.execCommand("PLACE b,a,SOUTH"), "Invalid parameters. usage: PLACE x,y,facedirection" )

    def test_V_PLACE_invalid4(self):
        self._robotController.setVerbose(True)
        self.assertEqual(self._robotController.execCommand("PLACE SOUTH,1,2"), "Invalid parameters. usage: PLACE x,y,facedirection" )

    #   Place invalid position

    def test_V_PLACE_invalid_pos1(self):
        self._robotController.setVerbose(True)
        self.assertEqual(self._robotController.execCommand("PLACE 6,1,NORTH"), "Cannot place here" )

    def test_V_PLACE_invalid_pos2(self):
        self._robotController.setVerbose(True)
        self.assertEqual(self._robotController.execCommand("PLACE -1,1,NORTH"), "Cannot place here" )

    def test_V_PLACE_invalid_pos3(self):
        self._robotController.setVerbose(True)
        self.assertEqual(self._robotController.execCommand("PLACE -1,1,NORTH"), "Cannot place here" )

    # Test right positioning

    def test_V_PLACE_pos1(self):
        self._robotController.setVerbose(True)
        self.assertEqual(self._robotController.execCommand("PLACE 1,1,NORTH"), "Robot placed" )

    def test_V_PLACE_pos2(self):
        self._robotController.setVerbose(True)
        self.assertEqual(self._robotController.execCommand("PLACE 2,1,EAST"), "Robot placed" )

    def test_V_PLACE_pos3(self):
        self._robotController.setVerbose(True)
        self.assertEqual(self._robotController.execCommand("PLACE 3,1,SOUTH"), "Robot placed" )

    def test_V_PLACE_pos4(self):
        self._robotController.setVerbose(True)
        self.assertEqual(self._robotController.execCommand("PLACE 1,3,WEST"), "Robot placed" )

    # Test if all commands return error when not placed
    def test_V_NotP_LEFT(self):
        self._robotController.setVerbose(True)
        self.assertEqual(self._robotController.execCommand("LEFT"), "Robot not placed. Use: PLACE x,y,facedirection" )

    def test_V_NotP_RIGHT(self):
        self._robotController.setVerbose(True)
        self.assertEqual(self._robotController.execCommand("RIGHT"), "Robot not placed. Use: PLACE x,y,facedirection" )

    def test_V_NotP_MOVE(self):
        self._robotController.setVerbose(True)
        self.assertEqual(self._robotController.execCommand("MOVE"), "Robot not placed. Use: PLACE x,y,facedirection" )

    # Test basic functions with placed robot
    def test_V_P_LEFT(self):
        self._robotController.setVerbose(True)
        self._robotController.execCommand("PLACE 1,1,SOUTH" )
        self.assertEqual(self._robotController.execCommand("LEFT"), "Command accepted" )

    def test_V_P_RIGHT(self):
        self._robotController.setVerbose(True)
        self._robotController.execCommand("PLACE 1,1,SOUTH" )
        self.assertEqual(self._robotController.execCommand("RIGHT"), "Command accepted" )

    def test_V_P_MOVE(self):
        self._robotController.setVerbose(True)
        self._robotController.execCommand("PLACE 1,1,SOUTH" )
        self.assertEqual(self._robotController.execCommand("MOVE"), "Command accepted" )

    #   Test fall of condition
    def test_V_P_MOVE(self):
        self._robotController.setVerbose(True)
        self._robotController.execCommand("PLACE 0,0,SOUTH" )
        self.assertEqual(self._robotController.execCommand("MOVE"), "Boarder reached, command ignored")

    # test command sequences
    def test_CommandSequence1(self):
        res = ""
        for a in CommandTestSequence1:
            res = self._robotController.execCommand(a)
        self.assertEqual(res,CommandTestSequence1Result)

    def test_CommandSequence2(self):
        res = ""
        for a in CommandTestSequence2:
            res = self._robotController.execCommand(a)
        self.assertEqual(res,CommandTestSequence2Result)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestRobotController)
    unittest.TextTestRunner(verbosity=2).run(suite)
