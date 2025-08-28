class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        
        N, M = len(matrix), len(matrix[0])
        result = []
        row = column = 0
        
        # Total elements to process
        for _ in range(N * M):
            result.append(matrix[row][column])
            
            # intuition we can go UP or DOWN
            # For UP the rows and cols sums to even
            # For DOWN the rows and cols sums to odd

            if (row + column) % 2 == 0:  # Moving up
                if column == M - 1:      # Hit right boundary
                    row += 1
                elif row == 0:           # Hit top boundary
                    column += 1
                else:                    # Normal diagonal move
                    row -= 1
                    column += 1
            else:                        # Moving down
                if row == N - 1:         # Hit bottom boundary
                    column += 1
                elif column == 0:        # Hit left boundary
                    row += 1
                else:                    # Normal diagonal move
                    row += 1
                    column -= 1
        
        return result
