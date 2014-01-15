import unittest
import rover
import direction


class RoverTest(unittest.TestCase):
    def test_rover_should_be_facing_east_after_turning_right_when_originally_facing_north(self):
        my_rover = rover.Rover(0, 1, direction.North(), 'R')
        my_rover.move()
        self.assertEqual(direction.East().__class__, my_rover.direction.__class__)

    def test_rover_should_be_facing_south_after_turning_right_when_originally_facing_east(self):
        my_rover = rover.Rover(0, 1, direction.East(), 'R')
        my_rover.move()
        self.assertEqual(direction.South().__class__, my_rover.direction.__class__)

    def test_rover_should_be_facing_west_after_turning_right_when_originally_facing_south(self):
        my_rover = rover.Rover(0, 1, direction.South(), 'R')
        my_rover.move()
        self.assertEqual(direction.West().__class__, my_rover.direction.__class__)

    def test_rover_should_be_facing_north_after_turning_right_when_originally_facing_west(self):
        my_rover = rover.Rover(0, 1, direction.West(), 'R')
        my_rover.move()
        self.assertEqual(direction.North().__class__, my_rover.direction.__class__)

    def test_rover_should_be_facing_west_after_turning_left_when_originally_facing_north(self):
        my_rover = rover.Rover(0, 1, direction.North(), 'L')
        my_rover.move()
        self.assertEqual(direction.West().__class__, my_rover.direction.__class__)

    def test_rover_should_be_facing_north_after_turning_left_when_originally_facing_east(self):
        my_rover = rover.Rover(0, 1, direction.East(), 'L')
        my_rover.move()
        self.assertEqual(direction.North().__class__, my_rover.direction.__class__)

    def test_rover_should_be_facing_east_after_turning_left_when_originally_facing_south(self):
        my_rover = rover.Rover(0, 1, direction.South(), 'L')
        my_rover.move()
        self.assertEqual(direction.East().__class__, my_rover.direction.__class__)

    def test_rover_should_be_facing_south_after_turning_left_when_originally_facing_west(self):
        my_rover = rover.Rover(0, 1, direction.West(), 'L')
        my_rover.move()
        self.assertEqual(direction.South().__class__, my_rover.direction.__class__)

    def test_rover_ypos_should_increase_when_facing_north_and_moving(self):
        my_rover = rover.Rover(2, 2, direction.North(), 'M')
        my_rover.move()
        self.assertEqual(my_rover.ypos, 3)

    def test_rover_ypos_should_decrease_when_facing_south_and_moving(self):
        my_rover = rover.Rover(2, 2, direction.South(), 'M')
        my_rover.move()
        self.assertEqual(my_rover.ypos, 1)

    def test_rover_xpos_should_decrease_when_facing_west_and_moving(self):
        my_rover = rover.Rover(2, 2, direction.West(), 'M')
        my_rover.move()
        self.assertEqual(my_rover.xpos, 1)

    def test_rover_xpos_should_increae_when_facing_east_and_moving(self):
        my_rover = rover.Rover(2, 2, direction.East(), 'M')
        my_rover.move()
        self.assertEqual(my_rover.xpos, 3)