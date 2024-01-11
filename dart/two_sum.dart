class Solution {
  List<int> twoSum(List<int> nums, int target) {
    final Map<int, int> hashMap = {};

    for (int i = 0; i < nums.length; i++) {
      int diff = target - nums[i];
      if (hashMap.containsKey(diff)) {
        return [hashMap[diff]!, i];
      } else {
        hashMap[nums[i]] = i;
      }
    }
    return [0, 0];
  }
}
