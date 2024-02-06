#!/usr/bin/python3
"""
  calculate island perimeter
  provided with grid
  grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
"""


def island_perimeter(grid):
    """ add number of land sides """

    height = len(grid)
    width = len(grid[0])
    perimeter = 0
    if (height <= 100 and width <= 100):
        for row in range(height):
            for col in range(width):
                if grid[row][col] == 1:
                    # check top of land
                    if row > 0:
                        if grid[row - 1][col] == 0:
                            perimeter += 1
                    else:
                        perimeter += 1
                    #  check bottom of land
                    if row < height - 1:
                        if grid[row + 1][col] == 0:
                            perimeter += 1
                    else:
                        perimeter += 1
                    # check left of land
                    if col > 0:
                        if grid[row][col - 1] == 0:
                            perimeter += 1
                    else:
                        perimeter += 1
                    #  check right of land
                    if col < width - 1:
                        if grid[row][col + 1] == 0:
                            perimeter += 1
                    else:
                        perimeter += 1

        return (perimeter)
