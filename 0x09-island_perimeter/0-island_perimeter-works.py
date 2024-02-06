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
