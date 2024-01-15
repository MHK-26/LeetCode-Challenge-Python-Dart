class Solution:
    def isValid(self, s: str) -> bool:
        """
        Determines if a string of parentheses is balanced.

        Args:
            s: The input string containing parentheses.

        Returns:
            True if the parentheses are balanced, False otherwise.
        """

        # Map for matching closing parentheses to opening parentheses
        HashMap = {"}": "{", ")": "(", "]": "["}

        # Stack to track opening parentheses
        stack = []

        for c in s:
            # If it's a closing parenthesis:
            if c in HashMap:
                # Check if the stack's top matches the expected opening parenthesis
                if stack and stack[-1] == HashMap[c]:
                    # If it matches, remove the opening parenthesis from the stack
                    stack.pop()
                else:
                    # If it doesn't match, the parentheses are not balanced
                    return False
            else:
                # If it's an opening parenthesis, push it onto the stack
                stack.append(c)

        # If the stack is empty, all parentheses are balanced
        return not stack  # Concisely return True if stack is empty
