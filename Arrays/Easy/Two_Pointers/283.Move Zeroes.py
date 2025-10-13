# ============================================================
# 283. Move Zeroes
# ============================================================

# 🧩 Problem:
# Given an integer array nums, move all 0's to the end of it while maintaining
# the relative order of the non-zero elements.
#
# You must do this in-place, without making a copy of the array.
#
# ------------------------------------------------------------
# Example 1:
# Input:  nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
#
# Example 2:
# Input:  nums = [0]
# Output: [0]
# ------------------------------------------------------------
#
# Constraints:
# 1 <= len(nums) <= 10^4
# -2^31 <= nums[i] <= 2^31 - 1
#
# Follow-up:
# Try to minimize the total number of operations.
# ------------------------------------------------------------


# ============================================================
# --- 1️⃣ Brute Force Solution ---
# ============================================================
# 🧠 Idea:
# 1. Collect all non-zero elements into a temp list.
# 2. Count how many zeros were removed.
# 3. Extend the temp list with that many zeros.
# 4. Copy back into the original array (in-place).
#
# ⏱️ Time:  O(n)
# 💾 Space: O(n)
# ------------------------------------------------------------

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        temp = []

        # Step 1: Collect all non-zero elements
        for x in nums:
            if x != 0:
                temp.append(x)

        # Step 2: Count zeros
        zero_cnt = len(nums) - len(temp)

        # Step 3: Add zeros at end
        temp.extend([0] * zero_cnt)

        # Step 4: Copy back to nums
        for i in range(len(nums)):
            nums[i] = temp[i]


# ✅ Test Brute Force
nums = [0, 1, 0, 3, 12]
Solution().moveZeroes(nums)
print(nums)  # Output: [1, 3, 12, 0, 0]



# ============================================================
# --- 2️⃣ Two Pointers Solution (Optimized) ---
# ============================================================
# 🧠 Idea:
# Use two pointers to do everything in-place.
#
# - slow: position to place next non-zero
# - fast: scans every element
#
# Steps:
# 1. Initialize slow = 0
# 2. For each fast in range(len(nums)):
#       if nums[fast] != 0:
#           swap(nums[slow], nums[fast])
#           slow += 1
# ------------------------------------------------------------
# ⏱️ Time:  O(n)
# 💾 Space: O(1)
# ✅ Most efficient and clean.
# ------------------------------------------------------------

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        slow = 0  # position for next non-zero

        for fast in range(len(nums)):
            if nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1


# ✅ Test Optimized
nums = [0, 1, 0, 3, 12]
Solution().moveZeroes(nums)
print(nums)  # Output: [1, 3, 12, 0, 0]



# ============================================================
# 🧾 Summary Comparison
# ============================================================
# | Approach        | Time  | Space | In-place | Notes                  |
# |-----------------|-------|--------|-----------|------------------------|
# | Brute Force     | O(n)  | O(n)   | ❌ No     | Uses extra array       |
# | Two Pointers    | O(n)  | O(1)   | ✅ Yes    | Best & minimal ops     |
# ============================================================
