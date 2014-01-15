class Rover(object):
    def __init__(self, xpos, ypos, my_direction, commands):
        self.xpos = xpos
        self.ypos = ypos
        self.direction = my_direction
        self.commands = commands

    def move(self):
        if self.commands == 'R':
            self.direction = self.direction.turn_right()
        elif self.commands == 'L':
            self.direction = self.direction.turn_left()
        elif self.commands == 'M':
            self.ypos += self.direction.move_ypos()
            self.xpos += self.direction.move_xpos()