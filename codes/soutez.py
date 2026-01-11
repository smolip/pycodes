from astar.search import AStar

grid = [
    ['.', '.', '.','.','.'],
    ['S', '#', '.','#','.'],
    ['.', '.', '.','.','.'],
    ['.', '#', '.','#','.'],
    ['3', '2', '#','1','0']
]

grid2 = [
    [0, 0, 0,0,0],
    [0, 1, 0,1,0],
    [0, 0, 0,0,0],
    [0, 1, 0,1,0],
    [0, 0, 1,0,0]
]

list=[1,0,3,2]

def hledejBod(grid, bod):
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if (bod == grid[i][j]):
                return (i,j)
    return [-1,-1]

start = hledejBod(grid, 'S')
nula = hledejBod(grid, '0')
jedna = hledejBod(grid, '1')
dva = hledejBod(grid, '2')
tri = hledejBod(grid, '3')




def findLenPath(start, bod):
    for i in range(0, len(list)):
        path = AStar(grid2).search(start, bod)
        return len(path)-1

print(findLenPath(start, jedna))
print(findLenPath(start, nula))
print(findLenPath(start, tri))
print(findLenPath(start, dva))

