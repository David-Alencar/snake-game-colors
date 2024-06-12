from turtle import Screen, Turtle
from time import sleep
from snake import Snake
from food import Food
from random import randint
from scoreboard import ScoreBoard, Wall

screen = Screen()
screen.listen()
screen.colormode(255)
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My Snake Game')
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()
wall = Wall()

screen.onkey(snake.turn_up, 'Up')
screen.onkey(snake.turn_down, 'Down')
screen.onkey(snake.turn_left, 'Left')
screen.onkey(snake.turn_right, 'Right')


def food_move(obj):
    while True:
        new_x = randint(-250, 250)
        new_y = randint(-250, 250)
        respawn_food_count = 0
        for seg in snake.segments:
            if seg.distance(new_x, new_y) < 10:
                respawn_food_count += 1
        if respawn_food_count == 0:
            obj.setposition(new_x, new_y)
            food.new_color()
            break


print(food.fillcolor())

game_is_on = True
speed_game = 0.2
while game_is_on:
    screen.update()
    sleep(speed_game)
    snake.move()

    if snake.head.distance(food) < 15:
        snake.grow(int(food.fillcolor()[0]), int(food.fillcolor()[1]), int(food.fillcolor()[2]))
        food_move(food)
        scoreboard.update_score()
        speed_game -= 0.005

    if snake.wall_collision:
        scoreboard.game_over()
        game_is_on = False

    if snake.self_collision:
        scoreboard.game_over()
        game_is_on = False

screen.exitonclick()
