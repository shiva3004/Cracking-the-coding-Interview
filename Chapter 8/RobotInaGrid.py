maze = [
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', '', ' ', ' '],
        ['', '', '', ' ', ' '],
        ['', ' ', ' ', ' ', ' ']
        ]


def printl(lis):
    for l in lis:
        print(l)

def getPath(maze, row, col, path):
    if len(maze) == 0 or maze == None:
        return False
    if row < 0 or col < 0 or not maze[row][col]:
        return False
    is_origin = (row == 0) and (col == 0)
    if is_origin or getPath(maze, row, col-1, path) or getPath(maze, row-1, col, path):
        path.append((row, col))
        return True
    return False

path = []
if getPath(maze, len(maze)-1, len(maze[0])-1, path):
    printl(path)
else:
    print('No path to be found')

