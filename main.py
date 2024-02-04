from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

texture_list = [r"pictures\dzban.gif", r"pictures\dzbanice.gif", r"pictures\stanley.gif", r"pictures\snake.gif",
                r"pictures\snake_head_up.gif", r"pictures\snake_head_down.gif", r"pictures\snake_head_left.gif",
                r"pictures\snake_head_right.gif"]

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game 🐍")
screen.tracer(0)
for texture in texture_list:
    screen.register_shape(texture)


snake = Snake()
food = Food()
score_board = ScoreBoard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

time_sleep = 0.1
game_continues = True
while game_continues:
    screen.update()
    time.sleep(time_sleep)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 18:  # Distance checks distance between two turtle objects and returns distance
        food.refresh()
        time_sleep -= 0.005
        snake.extend()
        score_board.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score_board.reset_score()
        time_sleep = 0.1
        snake.reset_snake()
        time.sleep(1)

    # Detect collision with tail (if head collides with any segment in the tail = game over)
    for segment in snake.snake_segments[1:]:  # Slices list so doesn't account first item
        if snake.head.distance(segment) < 10:
            score_board.reset_score()
            time_sleep = 0.1
            snake.reset_snake()
            time.sleep(1)

screen.exitonclick()
