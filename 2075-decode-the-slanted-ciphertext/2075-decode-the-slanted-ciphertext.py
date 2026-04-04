class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        if rows == 1:
            return encodedText
        
        n = len(encodedText)
        cols = n // rows
        
        # Build matrix
        matrix = [encodedText[i*cols:(i+1)*cols] for i in range(rows)]
        
        result = []
        
        # Traverse diagonals
        for start_col in range(cols):
            i, j = 0, start_col
            
            while i < rows and j < cols:
                result.append(matrix[i][j])
                i += 1
                j += 1
        
        # Remove trailing spaces
        return ''.join(result).rstrip()