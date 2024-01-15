class Solution {
  // Function to check if a string of parentheses is balanced
  bool isValid(String s) {
    // Map for matching opening and closing parentheses
    final Map<String, String> hashMap = {
      "}": "{",
      ")": "(",
      "]": "["
    }; // Closing -> Opening

    // Stack to keep track of opening parentheses
    final List<String> stack = [];

    // Iterate through each character in the string
    for (final char in s.runes.map((rune) => String.fromCharCode(rune))) {
      // If it's a closing parenthesis:
      if (hashMap.containsKey(char)) {
        // Check if the stack's top matches the expected opening parenthesis
        if (stack.isNotEmpty && stack.last == hashMap[char]) {
          // If it matches, remove the opening parenthesis from the stack
          stack.removeLast();
        } else {
          // If it doesn't match, the string is not balanced
          return false;
        }
      } else {
        // If it's an opening parenthesis, push it onto the stack
        stack.add(char);
      }
    }

    // If the stack is empty at the end, all parentheses are balanced
    return stack.isEmpty;
  }
}
