import pygame
from configs import *
from colors import *
from node import Node
from algos import a_star, dijkstra
def make_grid(rows, cols):
    grid = []
    for i in range(rows):
        grid.append([])
        for j in range(cols):
            node = Node(i, j)
            grid[i].append(node)
    return grid

def draw_grid(win, rows, cols):
    for i in range(rows):
        pygame.draw.line(win, BLACK, (0, i * GRID_HEIGHT), (WIDTH, i * GRID_HEIGHT))
        for j in range(cols):
            pygame.draw.line(win, BLACK, (j * GRID_WIDTH, 0), (j * GRID_WIDTH, HEIGHT))

def draw(win, grid, rows, cols):
    win.fill(WHITE)
    for row in grid:
        for node in row:
            node.draw(win)
    draw_grid(win, rows, cols)
    pygame.display.update()

def get_clicked_pos(pos, rows, cols):
    y, x = pos
    row = y // GRID_WIDTH
    col = x // GRID_HEIGHT
    return row, col


def main(win, width):
    grid = make_grid(ROWS, COLS)
    start = None
    end = None
    run = True
    started = False

    while run:
        draw(win, grid, ROWS, COLS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if started:
                continue

            if pygame.mouse.get_pressed()[0]: # LEFT
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, COLS)
                node = grid[row][col]
                if not start and node != end:
                    start = node
                    start.make_start()
                elif not end and node != start:
                    end = node
                    end.make_end()
                elif node != end and node != start:
                    node.make_barrier()

            elif pygame.mouse.get_pressed()[2]: # RIGHT
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, COLS)
                node = grid[row][col]
                node.reset()
                if node == start:
                    start = None
                elif node == end:
                    end = None

            if event.type == pygame.KEYDOWN:
                if start and end:
                    for row in grid:
                            for node in row:
                                node.update_neighbors(grid)
                    if event.key == pygame.K_a:
                        a_star(lambda: draw(win, grid, ROWS, COLS), grid, start, end)
                    elif event.key == pygame.K_d:
                        dijkstra(lambda: draw(win, grid, ROWS, COLS), grid, start, end)

                if event.key == pygame.K_c:
                    start = None
                    end = None
                    grid = make_grid(ROWS, COLS)

    pygame.quit()