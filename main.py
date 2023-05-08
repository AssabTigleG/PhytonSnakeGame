# TODO: Create a snake body
# TODO: Move the snake
# TODO: Create snake food
# TODO: Detect collision with food
# TODO: Create a scoreboard
# TODO: Detect collision with wall
# TODO: Detect collision with body
# ------------------------------------------
from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Board
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake = Snake()
food = Food()
board = Board()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_on = True
while is_on:

    screen.update()
    time.sleep(0.07)
    snake.move()

    if snake.snake[0].distance(food) < 17.5:
        food.refresh()
        board.increase_score()
        snake.extend()

    if snake.snake[0].xcor() > 280 or snake.snake[0].xcor() < -300 or snake.snake[0].ycor() > 300 or snake.snake[0].ycor() < -280:
        is_on = False
        board.game_over()

    slices = snake.snake[1:3]
    for segment in slices:
        if snake.snake[0].distance(segment) < 10:
            is_on = False
            board.game_over()



screen.exitonclick()