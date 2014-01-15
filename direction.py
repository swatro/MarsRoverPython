class North(object):
    def turn_right(self):
        return East()

    def turn_left(self):
        return West()

    def move_ypos(self):
        return 1

    def move_xpos(self):
        return 0

class East(object):
    def turn_right(self):
        return South()

    def turn_left(self):
        return North()

    def move_ypos(self):
        return 0

    def move_xpos(self):
        return 1


class South(object):
    def turn_right(self):
        return West()

    def turn_left(self):
        return East()

    def move_ypos(self):
        return -1

    def move_xpos(self):
        return 0


class West(object):
    def turn_right(self):
        return North()

    def turn_left(self):
        return South()

    def move_ypos(self):
        return 0

    def move_xpos(self):
        return -1