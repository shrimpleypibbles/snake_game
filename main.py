import time
from turtle import Screen

from food import Food
from scoreboard import Scoreboard
from snake import Snake

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(snake.up, "Up")
screen.onkeypress(snake.down, "Down")
screen.onkeypress(snake.left, "Left")
screen.onkeypress(snake.right, "Right")

is_on = True
while is_on:
    screen.update()
    time.sleep(0.08)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        is_on = False
        scoreboard.game_over()

    # Detect collision tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            is_on = False
            scoreboard.game_over()

screen.exitonclick()
