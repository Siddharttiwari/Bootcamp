def celebrity(M):
        n = len(M)
        
        # Top and Down pointers
        top, down = 0, n - 1
        
        # Traverse for all the people
        while top < down:
            
            # If top knows down,
            # it can not be a celebrity
            if M[top][down] == 1:
                top += 1
            
            # If down knows top,
            # it can not be a celebrity
            elif M[down][top] == 1:
                down -= 1
            
            # If both do not know each other,
            # both cannot be the celebrity
            else:
                top += 1
                down -= 1
        
        # Return -1 if no celebrity is found
        if top > down:
            return -1
        
        # Check if the person pointed
        # by top is celebrity
        for i in range(n):
            if i == top:
                continue
            
            # Check if it is not a celebrity
            if M[top][i] == 1 or M[i][top] == 0:
                return -1
        
        # Return the index of celebrity
        return top
