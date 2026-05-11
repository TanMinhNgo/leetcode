def updateBoard(self, board: list[list[str]], click: list[int]) -> list[list[str]]:
    m, n = len(board), len(board[0])
    x, y = click
    if board[x][y] == "M":
        board[x][y] = "X"
        return board

    def count_mines(i, j):
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if 0 <= i + dx < m and 0 <= j + dy < n and board[i + dx][j + dy] == "M":
                    count += 1
        return count

    def dfs(i, j):
        if board[i][j] != "E":
            return
        mines_count = count_mines(i, j)
        if mines_count > 0:
            board[i][j] = str(mines_count)
        else:
            board[i][j] = "B"
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if 0 <= i + dx < m and 0 <= j + dy < n:
                        dfs(i + dx, j + dy)

    dfs(x, y)
    return board