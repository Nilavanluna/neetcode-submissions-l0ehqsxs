class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # Create a map to connect closing brackets to opening ones
        bracket_map = {")": "(", "}": "{", "]": "["}

        for c in s:
            if c in bracket_map:
                # If we see a closing bracket, we must check the stack
                # 1. Check if stack is empty (nothing to match)
                # 2. Check if the top of the stack matches the map
                if stack and stack[-1] == bracket_map[c]:
                    stack.pop()
                else:
                    return False
            else:
                # It's an opening bracket, so push it onto the stack
                stack.append(c)

        # Return True only if all brackets were matched and popped
        return not stack