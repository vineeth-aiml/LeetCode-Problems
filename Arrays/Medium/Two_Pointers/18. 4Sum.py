# ============================================================
# 18. 4Sum
# ============================================================
# 🧩 Problem:
# Given an array nums of n integers, return all unique quadruplets 
# [nums[a], nums[b], nums[c], nums[d]] such that:
#
# 0 <= a, b, c, d < n
# a, b, c, d are distinct
# nums[a] + nums[b] + nums[c] + nums[d] == target
#
# You may return the answer in any order.
# 
# ------------------------------------------------------------
# Example 1:
# Input: nums = [1,0,-1,0,-2,2], target = 0
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
#
# Example 2:
# Input: nums = [2,2,2,2,2], target = 8
# Output: [[2,2,2,2]]
# ------------------------------------------------------------
#
# Constraints:
# 1 <= nums.length <= 200
# -10^9 <= nums[i] <= 10^9
# -10^9 <= target <= 10^9
# ------------------------------------------------------------
# 🧠 Edge Cases:
# - No solution: nums = [1,2,3], target = 100 → []
# - All elements same: nums = [2,2,2,2], target = 8 → [[2,2,2,2]]
# - Mixed positive and negative numbers
# ------------------------------------------------------------
# ============================================================

# ============================================================
# --- 1️⃣ Brute Force Solution ---
# ============================================================
# 🧠 Idea:
# 1. Generate all quadruplets using 4 nested loops.
# 2. Check if the sum == target.
# 3. Use a set to avoid duplicates.
#
# ⏱️ Time: O(n^4)
# 💾 Space: O(n) for storing results
# ------------------------------------------------------------
def fourSum_bruteforce(nums, target):
    nums.sort()
    n = len(nums)
    result = set()
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                for l in range(k+1, n):
                    if nums[i] + nums[j] + nums[k] + nums[l] == target:
                        result.add((nums[i], nums[j], nums[k], nums[l]))
    return [list(quad) for quad in result]

# ✅ Test Brute Force
nums = [1,0,-1,0,-2,2]
target = 0
print(fourSum_bruteforce(nums, target))
# Output: [[-2,-1,1,2], [-2,0,0,2], [-1,0,0,1]]

# ============================================================
# --- 2️⃣ Optimized Two Pointers Solution ---
# ============================================================
# 🧠 Idea:
# 1. Sort the array to handle duplicates and use two pointers.
# 2. Use two nested loops for the first two numbers (i, j).
# 3. Use two pointers (left, right) for the remaining two numbers.
# 4. Skip duplicates to ensure unique quadruplets.
#
# ⏱️ Time: O(n^3)
# 💾 Space: O(1) extra (besides output)
# ------------------------------------------------------------
def fourSum(nums, target):
    nums.sort()
    n = len(nums)
    result = []

    for i in range(n-3):
        if i > 0 and nums[i] == nums[i-1]:
            continue  # skip duplicates for i
        for j in range(i+1, n-2):
            if j > i+1 and nums[j] == nums[j-1]:
                continue  # skip duplicates for j

            left = j+1
            right = n-1
            while left < right:
                total = nums[i] + nums[j] + nums[left] + nums[right]
                if total == target:
                    result.append([nums[i], nums[j], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    # skip duplicates for left
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    # skip duplicates for right
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
                elif total < target:
                    left += 1
                else:
                    right -= 1
    return result

# ✅ Test Optimized
nums = [1,0,-1,0,-2,2]
target = 0
print(fourSum(nums, target))
# Output: [[-2,-1,1,2], [-2,0,0,2], [-1,0,0,1]]

# =====================================================================
# 🧾 Summary Comparison                                               |
# =====================================================================
# | Approach        | Time       | Space | Notes                       |
# |-----------------|------------|-------|-----------------------------|
# | Brute Force     | O(n^4)     | O(n)  | Simple, but very slow       |
# | Two Pointers    | O(n^3)     | O(1)  | ✅ Best, handles duplicates |
# ======================================================================
