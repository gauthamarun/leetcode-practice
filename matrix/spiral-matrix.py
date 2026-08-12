class Solution(object):
    def spiralOrder(self, matrix):
        m, n = len(matrix), len(matrix[0])
        left_wall = -1
        right_wall = n
        top_wall = 0
        bottom_wall = m
        up, left, right, down = 1,2,3,4
        result = []
        direction = right
        i,j =0,0

        while len(result)!=m*n:
            if direction==right:
                while j<right_wall:
                    result.append(matrix[i][j])
                    j+=1
                right_wall-=1
                i,j = i+1, j-1
                direction = down
            elif direction==down:
                while i<bottom_wall:
                    result.append(matrix[i][j])
                    i+=1
                bottom_wall-=1    
                i,j = i-1, j-1
                direction = left
            elif direction==left:
                while j>left_wall:
                    result.append(matrix[i][j])
                    j-=1
                left_wall+=1    
                i,j = i-1, j+1
                direction = up
            else:
                while i>top_wall:
                    result.append(matrix[i][j])
                    i-=1
                top_wall+=1    
                i,j = i+1, j+1
                direction = right

        return result            
                    

