from collections import deque
class Solution(object):
    def pacificAtlantic(self, heights):
        
        p_que = deque()
        p_set = set()

        a_que = deque()
        a_set = set()

        m,n = len(heights), len(heights[0])

        for i in range(n):
            p_que.append((0,i))
            p_set.add((0,i))
        for j in range(1,m):
            p_que.append((j,0))
            p_set.add((j,0))
        for i in range(m):
            a_que.append((i,n-1))
            a_set.add((i,n-1))  
        for j in range(n-1):
            a_que.append((m-1,j))
            a_set.add((m-1,j))  

        def get_coord(que,seen):
            while que:
                i,j = que.popleft()
                for i_off, j_off in [(0,1),(1,0),(-1,0),(0,-1)]:
                    r,c = i+i_off,j+j_off
                    if 0<=r<=m-1 and 0<=c<=n-1 and heights[r][c]>=heights[i][j] and (r,c) not in seen:
                        seen.add((r,c))
                        que.append((r,c))
        get_coord(p_que,p_set)
        get_coord(a_que,a_set)    
        return list(p_set & a_set)                