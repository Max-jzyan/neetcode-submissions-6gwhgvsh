class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        def dfs(i: int,j: int) -> None:
            stack = [[i,j]]
            while stack:
                y, x = stack.pop()
                grid[y][x] = '0'
                if y > 0 and grid[y-1][x] == '1':
                    stack.append([y-1,x])
                if x > 0 and grid[y][x-1] == '1':
                    stack.append([y,x-1])
                if ROWS - 1> y and grid[y+1][x] == '1':
                    stack.append([y+1,x])
                if COLS - 1 > x and grid[y][x+1] == '1':
                    stack.append([y,x+1])
        
        ans = 0
        for i, l in enumerate(grid):
            for j, ch in enumerate(l):
                if ch == '1':
                    dfs(i,j)
                    ans += 1
        return ans
                