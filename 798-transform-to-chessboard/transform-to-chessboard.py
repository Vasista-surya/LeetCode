class Solution(object):
    def movesToChessboard(self, board):
        n=len(board)
        for i in range(n):
            for j in range(n):
                if board[0][0]^board[i][0]^board[0][j]^board[i][j]:
                    return -1

        rs=sum(board[0])
        cs=sum(board[i][0] for i in range(n))

        rw=sum(board[i][0] == i%2 for i in range(n))
        cw=sum(board[0][j] == j%2 for j in range(n))

        if not (n//2 <=rs<=(n+1)//2): return -1
        if not (n//2 <=cs <= (n+1)//2): return -1

        if n%2:
            if rw %2: rw=n-rw
            if cw %2:cw = n-cw
        else :
            rw=min(rw,n-rw)
            cw=min(cw,n-cw)

        return (rw+cw)//2
        """
        :type board: List[List[int]]
        :rtype: int
        """
        