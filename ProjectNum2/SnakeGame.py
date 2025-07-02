import tkinter as tk
import random

# Constants
WIDTH = 600
HEIGHT = 400
SNAKE_SIZE = 20
SPEED = 100  # milliseconds between moves

class SnakeGame:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("🐍 Snake Game by Nikhil")

        self.canvas = tk.Canvas(self.window, width=WIDTH, height=HEIGHT, bg="black")
        self.canvas.pack()

        self.snake = [(100, 100), (80, 100), (60, 100)]
        self.snake_dir = "Right"
        self.food = self.spawn_food()

        self.draw_snake()
        self.draw_food()

        self.window.bind("<KeyPress>", self.change_dir)
        self.move_snake()
        self.window.mainloop()

    def draw_snake(self):
        self.canvas.delete("snake")
        for x, y in self.snake:
            self.canvas.create_rectangle(x, y, x + SNAKE_SIZE, y + SNAKE_SIZE, fill="green", tag="snake")

    def draw_food(self):
        x, y = self.food
        self.canvas.create_oval(x, y, x + SNAKE_SIZE, y + SNAKE_SIZE, fill="red", tag="food")

    def spawn_food(self):
        x = random.randint(0, (WIDTH - SNAKE_SIZE) // SNAKE_SIZE) * SNAKE_SIZE
        y = random.randint(0, (HEIGHT - SNAKE_SIZE) // SNAKE_SIZE) * SNAKE_SIZE
        return x, y

    def change_dir(self, event):
        key = event.keysym
        opposite = {'Up':'Down', 'Down':'Up', 'Left':'Right', 'Right':'Left'}
        if key in ['Up', 'Down', 'Left', 'Right'] and key != opposite.get(self.snake_dir):
            self.snake_dir = key

    def move_snake(self):
        head_x, head_y = self.snake[0]
        dx, dy = 0, 0
        if self.snake_dir == "Right":
            dx = SNAKE_SIZE
        elif self.snake_dir == "Left":
            dx = -SNAKE_SIZE
        elif self.snake_dir == "Up":
            dy = -SNAKE_SIZE
        elif self.snake_dir == "Down":
            dy = SNAKE_SIZE

        new_head = (head_x + dx, head_y + dy)

        # Check collisions
        if (new_head in self.snake or
            new_head[0] < 0 or new_head[0] >= WIDTH or
            new_head[1] < 0 or new_head[1] >= HEIGHT):
            self.game_over()
            return

        self.snake.insert(0, new_head)

        if new_head == self.food:
            self.canvas.delete("food")
            self.food = self.spawn_food()
            self.draw_food()
        else:
            self.snake.pop()

        self.draw_snake()
        self.window.after(SPEED, self.move_snake)

    def game_over(self):
        self.canvas.create_text(WIDTH // 2, HEIGHT // 2, fill="white", font="Arial 30 bold", text="GAME OVER")

# Run the game
SnakeGame()
