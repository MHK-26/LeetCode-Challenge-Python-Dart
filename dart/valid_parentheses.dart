class Solution {
  bool isValid(String s) {
    final Map<String, String> hashMap = {"}": "{", ")": "(", "]": "["};
    final List<String> stack = [];

    for (final char in s.runes.map((rune) => String.fromCharCode(rune))) {
      if (hashMap.containsKey(char)) {
        if (stack.isNotEmpty && stack.last == hashMap[char]) {
          stack.removeLast();
        } else {
          return false;
        }
      } else {
        stack.add(char);
      }
    }

    return stack.isEmpty;
  }
}
