import matplotlib.pyplot as plt
from matplotlib import colors
import random
from matplotlib.animation import FuncAnimation

x_size = 100
y_size = 100
alive_weight = 25
colormap = colors.ListedColormap(["grey", "green"])

board = []

for i in range(y_size):
    board.append(
        random.choices([0, 1], weights=(100 - alive_weight, alive_weight), k=x_size)
    )

fig, ax = plt.subplots()


def update(i):
    for row in range(y_size):
        for column in range(x_size):
            neighbors = []
            alive = board[row][column]
            for neirow in range(row - 1, row + 2):
                for neicolumn in range(column - 1, column + 2):
                    if (
                        (neirow >= 0)
                        and (neirow < y_size)
                        and (neicolumn >= 0)
                        and (neicolumn < x_size)
                        and ((neirow != row) or (neicolumn != column))
                    ):
                        neighbors.append(board[neirow][neicolumn])
            alive_count = neighbors.count(1)
            if (alive == 1 and alive_count < 2) or (alive == 1 and alive_count > 3):
                board[row][column] = 0
            elif alive == 0 and alive_count == 3:
                board[row][column] = 1

    ax.imshow(board, cmap=colormap)
    ax.set_axis_off()


anim = FuncAnimation(fig, update, frames=20, interval=5)
plt.show()
