from collections import deque

class Solution:
    def removeInvalidParentheses(self, s: str):
        result = []
        
        queue = deque([s])
        visited = {s}
        
        found = False
        
        while queue:
            for _ in range(len(queue)):
                current = queue.popleft()
                
                # Check if current string is valid
                if self.is_valid(current):
                    result.append(current)
                    found = True
                
                # Don't generate strings with more removals
                if found:
                    continue
                
                # Remove one parenthesis at a time
                for i in range(len(current)):
                    
                    if current[i] not in "()":
                        continue
                    
                    next_string = current[:i] + current[i + 1:]
                    
                    if next_string not in visited:
                        visited.add(next_string)
                        queue.append(next_string)
            
            # First valid level = minimum removals
            if found:
                break
        
        return result

    def is_valid(self, s: str):
        balance = 0
        
        for ch in s:
            if ch == '(':
                balance += 1
            
            elif ch == ')':
                balance -= 1
            
            # More ')' than '('
            if balance < 0:
                return False
        
        # All '(' must be matched
        return balance == 0
