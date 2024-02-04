from turtle import Turtle
SEGMENT_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    """Class that creates snake nad handles his movement and graphic"""
    def __init__(self):
        self.snake_segments = []
        self.create_snake()
        self.head = self.snake_segments[0]
        self.head.shape(r"pictures\snake_head_right.gif")

    def create_snake(self):
        """Creates basic 3 tile snake body"""
        for segment_pos in SEGMENT_POSITIONS:
            self.add_segment(segment_pos)

    def move(self):
        """Moves all parts of snake body forward depending on first segment orientation"""
        # Snake smooth movement starts at last segment, moves this segment to place where next segment is. Finally,
        # moves first segment where we want to go
        for seg_num in range(len(self.snake_segments) - 1, 0, -1):  # Start, Stop, Step
            new_x = self.snake_segments[seg_num - 1].xcor()
            new_y = self.snake_segments[seg_num - 1].ycor()
            self.snake_segments[seg_num].goto(new_x, new_y)
        self.snake_segments[0].forward(MOVE_DISTANCE)

    def add_segment(self, position):
        """Adds segment to list of snake segments"""
        snake = Turtle(r"pictures\snake.gif")
        snake.color("white")
        snake.penup()
        snake.goto(position)
        self.snake_segments.append(snake)

    def reset_snake(self):
        """Resets snake body to default position and size and throws old snake body away from screen"""
        for seg in self.snake_segments:
            seg.goto(x=1000, y=1000)
        self.snake_segments.clear()
        self.create_snake()
        self.head = self.snake_segments[0]
        self.head.shape(r"pictures\snake_head_right.gif")

    def extend(self):
        """Extends snakes body by 1 segment"""
        self.add_segment(self.snake_segments[-1].position())

    def up(self):
        """Sets snakes head heading to 90 degree"""
        if self.head.heading() == RIGHT or self.head.heading() == LEFT:
            self.head.setheading(UP)
            self.head.shape(r"pictures\snake_head_up.gif")

    def down(self):
        """Sets snakes head heading to 270 degree"""
        if self.head.heading() == RIGHT or self.head.heading() == LEFT:
            self.head.setheading(DOWN)
            self.head.shape(r"pictures\snake_head_down.gif")

    def left(self):
        """Sets snakes head heading to 180 degree"""
        if self.head.heading() == UP or self.head.heading() == DOWN:
            self.head.setheading(LEFT)
            self.head.shape(r"pictures\snake_head_left.gif")

    def right(self):
        """Sets snakes head heading to 0 degree"""
        if self.head.heading() == UP or self.head.heading() == DOWN:
            self.head.setheading(RIGHT)
            self.head.shape(r"pictures\snake_head_right.gif")
