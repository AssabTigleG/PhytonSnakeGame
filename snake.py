from turtle import Turtle,Screen

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake = []
        for i in STARTING_POSITION:
            self.add(i)

    def add(self, pos):
        segment = Turtle("square")
        segment.penup()
        segment.color("white")
        segment.goto(pos)
        self.snake.append(segment)

    def extend(self):
        self.add(self.snake[-1].position())

    def move(self):
        for i in range(len(self.snake) - 1, 0, -1):
            x = self.snake[i - 1].xcor()
            y = self.snake[i - 1].ycor()
            self.snake[i].goto(x, y)

        self.snake[0].fd(20)

    def up(self):
        if self.snake[0].heading() != DOWN:
            self.snake[0].setheading(UP)

    def down(self):
        if self.snake[0].heading() != UP:
            self.snake[0].setheading(DOWN)

    def left(self):
        if self.snake[0].heading() != RIGHT:
            self.snake[0].setheading(LEFT)

    def right(self):
        if self.snake[0].heading() != LEFT:
            self.snake[0].setheading(RIGHT)
