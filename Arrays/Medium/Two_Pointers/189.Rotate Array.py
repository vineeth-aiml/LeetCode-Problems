# ============================================================
# 189. Rotate Array
# ============================================================

# 🧩 Problem:
# Given an integer array nums, rotate the array to the right by k steps,
# where k is non-negative.
#
# ------------------------------------------------------------
# Example 1:
# Input:  nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
#
# Example 2:
# Input:  nums = [-1,-100,3,99], k = 2
# Output: [3,99,-1,-100]
# ------------------------------------------------------------
#
# Constraints:
# 1 <= len(nums) <= 10^5
# -2^31 <= nums[i] <= 2^31 - 1
# 0 <= k <= 10^5
#
# Follow-up:
# Could you do it in-place with O(1) extra space?
# ------------------------------------------------------------


# ============================================================
# --- 1️⃣ Brute Force Solution ---
# ============================================================
# 🧠 Idea:
# 1. Rotate the array one step at a time.
# 2. Each step:
#       - Save the last element.
#       - Shift all elements to the right by one.
#       - Put the saved element at index 0.
#
# Repeat this process k times.
#
# ⏱️ Time:  O(n × k)
# 💾 Space: O(1)
# ❌ Not efficient for large arrays but great for understanding.
# ------------------------------------------------------------

class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums)
        k = k % n  # Handle if k > n

        for _ in range(k):
            last = nums[-1]
            for i in range(n - 1, 0, -1):
                nums[i] = nums[i - 1]
            nums[0] = last


# ✅ Test Brute Force
nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
Solution().rotate(nums, k)
print(nums)  # Output: [5, 6, 7, 1, 2, 3, 4]



# ============================================================
# --- 2️⃣ Optimized Solution (Reverse Trick) ---
# ============================================================
# 🧠 Idea:
# 1. Reverse the entire array.
# 2. Reverse the first k elements.
# 3. Reverse the remaining n-k elements.
#
# Why it works:
# - Reversing the array reorders the elements such that rotating right
#   becomes a simple reversal pattern.
#
# Example:
# nums = [1,2,3,4,5,6,7], k=3
# Step 1: reverse all     → [7,6,5,4,3,2,1]
# Step 2: reverse first 3 → [5,6,7,4,3,2,1]
# Step 3: reverse rest    → [5,6,7,1,2,3,4]
#
# ⏱️ Time:  O(n)
# 💾 Space: O(1)
# ✅ In-place and most efficient.
# ------------------------------------------------------------

class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums)
        k = k % n

        def reverse(left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        # Step 1: Reverse entire array
        reverse(0, n - 1)

        # Step 2: Reverse first k elements
        reverse(0, k - 1)

        # Step 3: Reverse remaining elements
        reverse(k, n - 1)


# ✅ Test Optimized
nums = [0,1,2,3]
k = 2
Solution().rotate(nums, k)
print(nums)  # Output: [5, 6, 7, 1, 2, 3, 4]



# ============================================================
# 🧾 Summary Comparison
# ============================================================
# | Approach           | Time   | Space | In-place | Notes                   |
# |--------------------|--------|--------|-----------|-------------------------|
# | Brute Force        | O(n*k) | O(1)   | ✅ Yes    | Too slow for large k    |
# | Reverse Trick      | O(n)   | O(1)   | ✅ Yes    | ⚡ Best & clean method   |
# ============================================================
