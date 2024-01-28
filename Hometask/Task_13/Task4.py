class Robot:
    def __init__(self, orientation: str, position_x: int, position_y: int):
        self.orientation = orientation
        self.position_x = position_x
        self.position_y = position_y

    def move(self, steps: int) -> None:
        match self.orientation:
            case 'left':
                self.position_x -= steps
            case 'right':
                self.position_x += steps
            case 'up':
                self.position_y += steps
            case 'down':
                self.position_y -= steps
    def turn(self, direction: str) -> None:
        direction_list = [ "up", "right", "down", "left"]
        match direction:
            case 'right':
                current_direction = direction_list.index(self.orientation)
                if current_direction == 3:
                    self.orientation = "up"
                else:
                    self.orientation = direction_list[current_direction + 1]
            case 'left':
                current_direction = direction_list.index(self.orientation)
                if current_direction == 0:
                    self.orientation = "left"
                else:
                    self.orientation = direction_list[current_direction - 1]

    def display_position(self) -> str:
        return (f'Current position of robot is:\n'
                f'X = {self.position_x}\n'
                f'Y = {self.position_y}\n'
                f'Orientation = {self.orientation}')


robot = Robot('up', 1, 1)
print(robot.display_position())
robot.turn('right')
robot.move(5)
print(robot.display_position())
robot.turn('right')
robot.move(5)
print(robot.display_position())
robot.turn('left')
robot.move(5)
print(robot.display_position())