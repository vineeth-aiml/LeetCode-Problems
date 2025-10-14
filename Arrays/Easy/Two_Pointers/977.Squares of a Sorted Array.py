# ============================================================
# 977. Squares of a Sorted Array
# ============================================================

# 🧩 Problem:
# Given an integer array nums sorted in non-decreasing order,
# return an array of the squares of each number, also sorted in non-decreasing order.
#
# ------------------------------------------------------------
# Example 1:
# Input:  nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
#
# Example 2:
# Input:  nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]
# ------------------------------------------------------------
#
# Constraints:
# 1 <= nums.length <= 10^4
# -10^4 <= nums[i] <= 10^4
# nums is sorted in non-decreasing order.
#
# ------------------------------------------------------------
# 🧠 Edge Cases:
# - All positives: [1,2,3] → [1,4,9]
# - All negatives: [-3,-2,-1] → [1,4,9]
# - Mixed values: [-4,-1,0,3,10]
# - Single element: [0] or [5]
# ------------------------------------------------------------


# ============================================================
# --- 1️⃣ Brute Force Solution ---
# ============================================================
# 🧠 Idea:
# 1. Square every element.
# 2. Sort the resulting list.
# Simple but sorting makes it O(n log n).
#
# ⏱️ Time:  O(n log n)
# 💾 Space: O(n)
# ------------------------------------------------------------

def sortedSquares(nums):
    result = [x * x for x in nums]  # Step 1: Square all
    result.sort()                   # Step 2: Sort
    return result


# ✅ Test Brute Force
nums = [-4, -1, 0, 3, 10]
print(sortedSquares(nums))  # Output: [0, 1, 9, 16, 100]



# ============================================================
# --- 2️⃣ Two Pointers Solution (Optimized) ---
# ============================================================
# 🧠 Idea:
# - Since nums is sorted, negatives on left may become large positives after squaring.
# - Compare absolute values from both ends.
# - Fill result array from right → left (largest squares first).
#
# Steps:
# 1. Create result array of same size.
# 2. Initialize two pointers (l=0, r=n-1).
# 3. Move inward, picking the larger square each time.
#
# ✅ Avoids sorting — O(n) linear time.
#
# ⏱️ Time:  O(n)
# 💾 Space: O(n)
# ------------------------------------------------------------

def sortedSquares(nums):
    n = len(nums)
    result = [0] * n
    l, r = 0, n - 1

    for i in range(n - 1, -1, -1):  # Fill from end
        if abs(nums[l]) > abs(nums[r]):
            result[i] = nums[l] * nums[l]
            l += 1
        else:
            result[i] = nums[r] * nums[r]
            r -= 1
    return result


# ✅ Test Optimized
nums = [-7, -3, 2, 3, 11]
print(sortedSquares(nums))  # Output: [4, 9, 9, 49, 121]



# ============================================================
# 🧾 Summary Comparison
# ============================================================
# | Approach       | Time       | Space | Notes |
# |----------------|------------|--------|--------|
# | Brute Force    | O(n log n) | O(n)   | Sort after squaring |
# | Two Pointers   | O(n)       | O(n)   | ✅ Best — linear scan only |
# ============================================================
