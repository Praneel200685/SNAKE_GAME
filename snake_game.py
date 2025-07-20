class Snake_game:
        from turtle import Turtle, Screen
        from snake import Snake
        from food import Food
        from score import Scoreboard
        import time

        # Screen setup
        screen = Screen()
        screen.setup(width=600, height=600)
        screen.bgcolor("black")
        screen.title("Snake Game")
        screen.tracer(0)


        # Initialize Snake
        snake = Snake()
        food=Food()
        score=Scoreboard()
        #changing the direction of the snake
        screen.listen()
        screen.onkey(snake.up,"Up")
        screen.onkey(snake.down,"Down")
        screen.onkey(snake.left,"Left")
        screen.onkey(snake.right,"Right")
        # Main game loop

        game_on = True
        while game_on:
            screen.update()
            time.sleep(0.1)
            snake.snake_move()

            # Detect collision with food
            if snake.head.distance(food) < 14:
                food.refresh()
                snake.extend()
                score.upscore()
            # Detect wall collision
            if snake.head.xcor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() > 285 or snake.head.ycor() < -285:
                game_on = False
                score.game()
            #detect tail collision
            for segment in snake.segments:
                if segment==snake.head:
                   pass
                elif snake.head.distance(segment) <10:
                   game_on=False

        screen.mainloop()
