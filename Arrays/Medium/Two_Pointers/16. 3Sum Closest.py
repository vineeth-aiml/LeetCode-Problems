# ============================================================
# 16. 3Sum Closest
# ============================================================

# 🧩 Problem:
# Given an integer array nums of length n and an integer target,
# find three integers in nums such that the sum is closest to target.
# Return the sum of the three integers.
#
# You may assume that each input would have exactly one solution.
#
# ------------------------------------------------------------
# Example 1:
# Input:  nums = [-1, 2, 1, -4], target = 1
# Output: 2
# Explanation: (-1 + 2 + 1 = 2) is closest to 1.
#
# Example 2:
# Input:  nums = [0, 0, 0], target = 1
# Output: 0
# Explanation: (0 + 0 + 0 = 0) is closest to 1.
# ------------------------------------------------------------
#
# Constraints:
# 3 <= nums.length <= 500
# -1000 <= nums[i] <= 1000
# -10^4 <= target <= 10^4
# ------------------------------------------------------------


# ============================================================
# --- 1️⃣ Brute Force Solution ---
# ============================================================
# 🧠 Idea:
# 1. Try every possible triplet combination (i, j, k).
# 2. Compute the sum for each triplet.
# 3. Keep track of the sum that gives the smallest difference from target.
#
# ❌ Extremely slow for large n (O(n³)), but easy to understand.
#
# ⏱️ Time:  O(n³)
# 💾 Space: O(1)
# ------------------------------------------------------------

class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        n = len(nums)
        closest_sum = float('inf')  # To store the closest sum found so far

        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    curr_sum = nums[i] + nums[j] + nums[k]
                    # Update closest if difference is smaller
                    if abs(target - curr_sum) < abs(target - closest_sum):
                        closest_sum = curr_sum

        return closest_sum


# ✅ Test Brute Force
nums = [-1, 2, 1, -4]
target = 1
print(Solution().threeSumClosest(nums, target))  # Output: 2



# ============================================================
# --- 2️⃣ Optimized Solution (Two Pointer Approach) ---
# ============================================================
# 🧠 Idea:
# 1. Sort the array → helps use the two-pointer technique.
# 2. Fix one element (nums[i]) and use two pointers (left, right)
#    to find the other two numbers.
# 3. Compare current sum with target and move pointers accordingly:
#       - If curr_sum < target → move left++
#       - If curr_sum > target → move right--
# 4. Keep track of the closest sum to target.
#
# ✅ Efficient and elegant O(n²) solution.
#
# ⏱️ Time:  O(n²)
# 💾 Space: O(1)
# ------------------------------------------------------------

class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        closest_sum = float('inf')

        for i in range(n - 2):
            left, right = i + 1, n - 1

            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]

                # Update closest sum if difference is smaller
                if abs(target - curr_sum) < abs(target - closest_sum):
                    closest_sum = curr_sum

                if curr_sum < target:
                    left += 1
                elif curr_sum > target:
                    right -= 1
                else:
                    return curr_sum  # Exact match → best possible case

        return closest_sum


# ✅ Test Optimized
nums = [-1, 2, 1, -4]
target = 1
print(Solution().threeSumClosest(nums, target))  # Output: 2



# ============================================================
# 🧾 Summary Comparison
# ============================================================
# | Approach        | Time     | Space | Notes                              |
# |-----------------|----------|--------|------------------------------------|
# | Brute Force     | O(n³)    | O(1)   | Simple but too slow                |
# | Two Pointer     | O(n²)    | O(1)   | ✅ Best, fast & uses sorting trick |
# ============================================================
