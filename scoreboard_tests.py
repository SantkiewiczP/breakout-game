import unittest
from scoreboard import Scoreboard


class TestScoreboard(unittest.TestCase):

    def test_add_point(self):
        # Arrange
        s = Scoreboard()
        # Act
        s.add_points(2)
        # Assert
        self.assertEqual(s.score, 2)

    def test_scoreboard_updates(self):
        s = Scoreboard()
        s.add_points(5)
        s.__update_scoreboard__()
        self.assertEqual(s.score, 5)

    def test_scoreboard_clears_upon_new_game(self):
        s = Scoreboard()
        s.add_points(100)
        s.clear_scoreboard()
        self.assertEqual(s.score, 0)