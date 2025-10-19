# ============================================================
# 15. 3Sum
# ============================================================

# 🧩 Problem:
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
# such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
#
# The solution set must not contain duplicate triplets.
#
# ------------------------------------------------------------
# Example 1:
# Input:  nums = [-1, 0, 1, 2, -1, -4]
# Output: [[-1, -1, 2], [-1, 0, 1]]
#
# Example 2:
# Input:  nums = [0, 1, 1]
# Output: []
#
# Example 3:
# Input:  nums = [0, 0, 0]
# Output: [[0, 0, 0]]
# ------------------------------------------------------------
#
# Constraints:
# 3 <= len(nums) <= 3000
# -10^5 <= nums[i] <= 10^5
# ------------------------------------------------------------
#
# 🧠 Edge Cases:
# - nums = [0, 0, 0, 0] → [[0,0,0]] (only one unique triplet)
# - nums = [1, 2, -3] → [[-3,1,2]]
# - nums = [1, 2, 3] → [] (no zero sum)
# ------------------------------------------------------------


# ============================================================
# --- 1️⃣ Brute Force Solution (O(n³)) ---
# ============================================================
# 🧠 Idea:
# - Check every possible triplet (i, j, k) where i < j < k.
# - If their sum is 0 → store the triplet.
# - To avoid duplicates:
#     - Sort each triplet before adding.
#     - Use a set() to store unique tuples.
#
# ⏱️ Time:  O(n³)
# 💾 Space: O(m)  → for storing unique triplets
# ------------------------------------------------------------

def threeSum_bruteforce(nums):
    n = len(nums)
    result = set()

    # Step 1: Check all possible triplets
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if nums[i] + nums[j] + nums[k] == 0:
                    triplet = tuple(sorted([nums[i], nums[j], nums[k]]))
                    result.add(triplet)

    # Step 2: Convert set of tuples → list of lists
    return [list(t) for t in result]


# ✅ Test Brute Force
nums = [-1, 0, 1, 2, -1, -4]
print("Brute Force Output:", threeSum_bruteforce(nums))
# Output: [[-1, -1, 2], [-1, 0, 1]]



# ============================================================
# --- 2️⃣ Optimized Two-Pointer Solution (O(n²)) ---
# ============================================================
# 🧠 Idea:
# 1. Sort the array.
# 2. For each index i → treat nums[i] as the first number.
# 3. Use two pointers:
#     - left = i + 1
#     - right = end of array
#     - Compute total = nums[i] + nums[left] + nums[right]
# 4. Adjust pointers based on the sum:
#     - If total == 0 → store triplet, skip duplicates.
#     - If total < 0  → move left pointer right (need larger sum).
#     - If total > 0  → move right pointer left (need smaller sum).
# 5. Skip duplicates for nums[i] as well to avoid same triplets.
#
# ✅ Removes duplicates efficiently.
#
# ⏱️ Time:  O(n²)
# 💾 Space: O(1)  (ignoring output list)
# ------------------------------------------------------------

def threeSum(nums):
    nums.sort()
    n = len(nums)
    result = []

    for i in range(n - 2):
        # Skip duplicate 'i' values
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left, right = i + 1, n - 1
        target = -nums[i]

        while left < right:
            total = nums[left] + nums[right]

            if total == target:
                result.append([nums[i], nums[left], nums[right]])

                # Move both pointers skipping duplicates
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1

            elif total < target:
                left += 1
            else:
                right -= 1

    return result


# ✅ Test Optimized
nums = [-1, 0, 1, 2, -1, -4]
print("Two-Pointer Output:", threeSum(nums))
# Output: [[-1, -1, 2], [-1, 0, 1]]



# ============================================================
# 🧾 Summary Comparison
# ============================================================
# | Approach             | Time   | Space | Notes |
# |----------------------|--------|--------|--------------------------------|
# | Brute Force (3 Loops)| O(n³)  | O(n)   | Simple but very slow           |
# | Two Pointers         | O(n²)  | O(1)   | ✅ Optimal & skips duplicates   |
# ============================================================


# 💡 Summary:
# - Sort array to use two-pointer logic.
# - Fix one element, then find two others whose sum = -fixed.
# - Skip duplicates at every stage.
# - Works efficiently for large arrays up to 3000 elements.
# ============================================================
