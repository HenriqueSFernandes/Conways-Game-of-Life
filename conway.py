import matplotlib.pyplot as plt
from matplotlib import colors
import random
from matplotlib.animation import FuncAnimation

Y_SIZE = 100  # performance drops significantly if this value is too high
X_SIZE = 100  # performance drops significantly if this value is too high
ALIVE_PERCENTAGE = 6  # percentage of cells that are alive at the start
COLORMAP = colors.ListedColormap(["grey", "green"])
board = []
for i in range(Y_SIZE):

    board.append(
        random.choices(
            [0, 1], weights=(100 - ALIVE_PERCENTAGE, ALIVE_PERCENTAGE), k=X_SIZE
        )
    )
board2 = board.copy()
fig, ax = plt.subplots()


def update(i):
    global board, board2
    for row in range(Y_SIZE):
        for column in range(X_SIZE):
            neighbors = []
            alive = board[row][column]
            for neirow in range(row - 1, row + 2):
                for neicolumn in range(column - 1, column + 2):
                    if (
                        (neirow >= 0)
                        and (neirow < Y_SIZE)
                        and (neicolumn >= 0)
                        and (neicolumn < X_SIZE)
                        and ((neirow != row) or (neicolumn != column))
                    ):
                        neighbors.append(board[neirow][neicolumn])
            alive_count = neighbors.count(1)
            if (alive == 1 and alive_count < 2) or (alive == 1 and alive_count > 3):
                board2[row][column] = 0
            elif alive == 0 and alive_count == 3:
                board2[row][column] = 1
            board = board2.copy()
    ax.imshow(board, cmap=COLORMAP)
    ax.set_axis_off()


anim = FuncAnimation(fig, update, frames=20, interval=5)
plt.show()
