from turtle import Screen
import time
from Snake import Snake
from Food import Food
from Scoreboard import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

segments = []
screen.tracer(0)
snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(fun=snake.left, key="Left")
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    if snake.head.distance(food) < 13:
        food.refresh()
        snake.extend()
        score.refresh()


    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>290 or snake.head.ycor()<-290:
        score.reset()
        snake.reset()

    for segment in segments:
        if segment == snake.head:
            pass
        if snake.head.distance(segment) < 10:
            score.reset()
            snake.reset()






screen.exitonclick()
