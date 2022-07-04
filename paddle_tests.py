import unittest
from paddle import Paddle


class TestPaddle(unittest.TestCase):

    def test_paddle_moves_right(self):
        p = Paddle()
        p.move_right()
        self.assertEqual(p.position(), (25.0, -270.0))

    def test_paddle_moves_left_(self):
        p = Paddle()
        p.move_left()
        self.assertEqual(p.position(), (-25.0, -270.0))

    def test_paddle_goes_to_set_position(self):
        p = Paddle()
        p.move_left()
        p.move_left()
        p.set_position()
        self.assertEqual(p.position(), (-20, -270))

    def test_paddle_stops_at_right_screen_border(self):
        p = Paddle()
        for i in range(20):
            p.move_right()
        self.assertEqual(p.position(), (350.00, -270.00))

    def test_paddle_stops_at_left_screen_border(self):
        p = Paddle()

        for i in range(20):
            p.move_left()

        self.assertEqual(p.position(), (-350.00, -270.00))




