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
                    #  check bottom of land
                    if row < height - 1:
                        if grid[row + 1][col] == 0:
                            perimeter += 1
                    # check left of land
                    if col > 0:
                        if grid[row][col - 1] == 0:
                            perimeter += 1
                    #  check right of land
                    if col < width - 1:
                        if grid[row][col + 1] == 0:
                            perimeter += 1

        return (perimeter)
#!/usr/bin/python3
"""Island Perimeter"""


def island_perimeter(grid):
    """ calculate perimeter of an island """
    if isinstance(grid, list) and grid != []:
        north_grid = 0
        south_grid = row = len(grid)
        west_grid = 0
        east_grid = col = len(grid[0])
    perimeter = [0]
    for ver in range(row):

        for hor in range(col):
            if grid[ver][hor] == 1:
                # check north
                north = ver - 1
                if north >= north_grid:
                    if grid[north][hor] == 0:
                        # print(f"north:{1} row|col-->{ver}|{hor}")
                        perimeter[0] += 1
                else:
                    perimeter[0] += 1
                # check south
                south = ver + 1
                if south < south_grid:
                    if grid[south][hor] == 0:
                        perimeter[0] += 1
                        # print(f"south:{1} row|col-->{ver}|{hor}")
                else:
                    perimeter[0] += 1
                # check west
                west = hor - 1
                if west >= west_grid:
                    if grid[ver][west] == 0:
                        perimeter[0] += 1
                        # print(f"west:{1} row|col-->{ver}|{hor}")
                else:
                    perimeter[0] += 1
                # check east
                east = hor + 1
                if east < east_grid:
                    if grid[ver][east] == 0:
                        perimeter[0] += 1
                        # print(f"east:{1} row|col-->{ver}|{hor}")
                else:
                    perimeter[0] += 1
    return (perimeter[0])
