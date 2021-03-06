import unittest
from RiverCrossingPuzzles.TestsForMakeMove import LocationDummy, ValidationDummy

"""Checks with Validation class if the move is valid. If yes, update the Location class and call the Animation."""


class ControlTest(unittest.TestCase):

    def test_make_move(self, char_id=2, move='move'):
        """Checks that this is the character we want to work with"""
        self.assertEqual(char_id, 2)
        """Checks that the character is in the right place"""
        self.assertTrue(LocationDummy.checkLocation(self, char_id), True)
        """Checks that the move is legal"""
        self.assertTrue(ValidationDummy.isLegal(self, move, char_id), True)
        """Updates location"""
        self.assertTrue(LocationDummy.updateLocation(self, char_id, 'new location'), True)


if __name__ == '__main__':
    unittest.main()
