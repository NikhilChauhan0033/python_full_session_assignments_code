import tkinter as tk
import random

GRID_LEN = 4
GRID_PADDING = 10
BACKGROUND_COLOR = "#92877d"
EMPTY_CELL_COLOR = "#9e948a"
TILE_COLORS = {
    2: "#eee4da", 4: "#ede0c8", 8: "#f2b179", 16: "#f59563",
    32: "#f67c5f", 64: "#f65e3b", 128: "#edcf72", 256: "#edcc61",
    512: "#edc850", 1024: "#edc53f", 2048: "#ffcc00"
}
TEXT_COLORS = {2: "#776e65", 4: "#776e65", 8: "#f9f6f2"}
FONT = ("Verdana", 24, "bold")

class Game2048(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.grid()
        self.master.title("2048 Game by Nikhil")
        self.master.bind("<Key>", self.key_pressed)

        self.score_label = tk.Label(self, text="Score: 0", font=("Verdana", 16, "bold"), bg="#bbada0", fg="white", pady=10)
        self.score_label.grid(row=0, column=0, columnspan=GRID_LEN)

        self.grid_cells = []
        self.init_grid()
        self.restart_button = tk.Button(self, text="Restart", font=("Verdana", 12), command=self.restart_game)
        self.restart_button.grid(row=GRID_LEN + 2, column=0, columnspan=GRID_LEN, pady=10)

        self.init_matrix()
        self.update_grid_cells()
        self.mainloop()

    def init_grid(self):
        self.background = tk.Frame(self, bg=BACKGROUND_COLOR, width=400, height=400)
        self.background.grid(row=1, column=0, columnspan=GRID_LEN)
        for i in range(GRID_LEN):
            row = []
            for j in range(GRID_LEN):
                cell = tk.Frame(
                    self.background,
                    bg=EMPTY_CELL_COLOR,
                    width=100,
                    height=100
                )
                cell.grid(row=i, column=j, padx=GRID_PADDING, pady=GRID_PADDING)
                label = tk.Label(
                    master=cell,
                    text="",
                    bg=EMPTY_CELL_COLOR,
                    justify=tk.CENTER,
                    font=FONT,
                    width=4,
                    height=2
                )
                label.grid()
                row.append(label)
            self.grid_cells.append(row)

    def init_matrix(self):
        self.matrix = [[0] * GRID_LEN for _ in range(GRID_LEN)]
        self.score = 0
        self.add_random_tile()
        self.add_random_tile()

    def restart_game(self):
        self.init_matrix()
        self.update_grid_cells()
        self.score_label.config(text="Score: 0")

    def add_random_tile(self):
        empty_cells = [(i, j) for i in range(GRID_LEN) for j in range(GRID_LEN) if self.matrix[i][j] == 0]
        if empty_cells:
            i, j = random.choice(empty_cells)
            self.matrix[i][j] = random.choice([2, 4])

    def update_grid_cells(self):
        for i in range(GRID_LEN):
            for j in range(GRID_LEN):
                value = self.matrix[i][j]
                label = self.grid_cells[i][j]
                if value == 0:
                    label.config(text="", bg=EMPTY_CELL_COLOR)
                else:
                    color = TILE_COLORS.get(value, "#ff0000")
                    border_color = "#ffd700" if value == 2048 else color
                    label.config(
                        text=str(value),
                        bg=color,
                        fg=TEXT_COLORS.get(value, "#f9f6f2"),
                        highlightthickness=4 if value == 2048 else 0,
                        highlightbackground=border_color
                    )
        self.score_label.config(text=f"Score: {self.score}")
        self.update_idletasks()

    def key_pressed(self, event):
        key = event.keysym
        if key in ['Up', 'Down', 'Left', 'Right']:
            if self.move(key):
                self.add_random_tile()
                self.update_grid_cells()
                if self.game_over():
                    self.grid_cells[1][1].config(text="Game", bg="black")
                    self.grid_cells[1][2].config(text="Over!", bg="black")

    def move(self, direction):
        def merge(row):
            new_row = [i for i in row if i != 0]
            for i in range(len(new_row) - 1):
                if new_row[i] == new_row[i + 1]:
                    new_row[i] *= 2
                    self.score += new_row[i]
                    new_row[i + 1] = 0
            return [i for i in new_row if i != 0] + [0] * (GRID_LEN - len([i for i in new_row if i != 0]))

        moved = False
        if direction == 'Left':
            for i in range(GRID_LEN):
                new = merge(self.matrix[i])
                if new != self.matrix[i]:
                    self.matrix[i] = new
                    moved = True

        elif direction == 'Right':
            for i in range(GRID_LEN):
                new = merge(self.matrix[i][::-1])[::-1]
                if new != self.matrix[i]:
                    self.matrix[i] = new
                    moved = True

        elif direction == 'Up':
            for j in range(GRID_LEN):
                col = [self.matrix[i][j] for i in range(GRID_LEN)]
                new = merge(col)
                for i in range(GRID_LEN):
                    if self.matrix[i][j] != new[i]:
                        self.matrix[i][j] = new[i]
                        moved = True

        elif direction == 'Down':
            for j in range(GRID_LEN):
                col = [self.matrix[i][j] for i in range(GRID_LEN)][::-1]
                new = merge(col)[::-1]
                for i in range(GRID_LEN):
                    if self.matrix[i][j] != new[i]:
                        self.matrix[i][j] = new[i]
                        moved = True
        return moved

    def game_over(self):
        for i in range(GRID_LEN):
            for j in range(GRID_LEN):
                if self.matrix[i][j] == 0:
                    return False
                if j < GRID_LEN - 1 and self.matrix[i][j] == self.matrix[i][j + 1]:
                    return False
                if i < GRID_LEN - 1 and self.matrix[i][j] == self.matrix[i + 1][j]:
                    return False
        return True

# Start game
Game2048()
