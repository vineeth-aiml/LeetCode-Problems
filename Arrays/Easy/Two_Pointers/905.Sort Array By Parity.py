# ============================================================
# 905. Sort Array By Parity
# ============================================================

# 🧩 Problem:
# Given an integer array nums, move all the even integers to the beginning
# followed by all the odd integers.
#
# Return any array that satisfies this condition.
#
# ------------------------------------------------------------
# Example 1:
# Input:  nums = [3,1,2,4]
# Output: [2,4,3,1]
#
# Example 2:
# Input:  nums = [0]
# Output: [0]
# ------------------------------------------------------------
#
# Constraints:
# 1 <= nums.length <= 5000
# 0 <= nums[i] <= 5000
#
# ------------------------------------------------------------
# 🧠 Edge Cases:
# - All even: [2,4,6] → [2,4,6]
# - All odd: [1,3,5] → [1,3,5]
# - Mixed: [3,1,2,4] → [2,4,3,1]
# - Single element: [0] or [1]
# ------------------------------------------------------------


# ============================================================
# --- 1️⃣ Brute Force Solution ---
# ============================================================
# 🧠 Idea:
# 1. Create two lists:
#    - evens → store even numbers
#    - odds  → store odd numbers
# 2. Concatenate evens + odds to get the final list.
#
# Simple and clear, but uses extra space.
#
# ⏱️ Time:  O(n)
# 💾 Space: O(n)
# ------------------------------------------------------------

def sortArrayByParity(nums):
    evens = []
    odds = []

    # Step 1: Separate even and odd numbers
    for x in nums:
        if x % 2 == 0:
            evens.append(x)
        else:
            odds.append(x)

    # Step 2: Combine both lists
    return evens + odds


# ✅ Test Brute Force
nums = [3, 1, 2, 4]
print(sortArrayByParity(nums))  # Output: [2,4,3,1] or [4,2,3,1]



# ============================================================
# --- 2️⃣ Two Pointers Solution (Optimized) ---
# ============================================================
# 🧠 Idea:
# - Use two pointers (left & right index).
# - `left` points to where the next even number should go.
# - `right` iterates over the array.
# - When nums[right] is even, swap it with nums[left] and move left forward.
#
# ✅ Works in-place, maintaining O(1) space.
#
# ⏱️ Time:  O(n)
# 💾 Space: O(1)
# ------------------------------------------------------------

def sortArrayByParity(nums):
    left = 0  # index to place next even number

    # Step 1: Iterate with right pointer
    for right in range(len(nums)):
        # Step 2: If even, swap it to front
        if nums[right] % 2 == 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1

    return nums


# ✅ Test Optimized
nums = [3, 1, 2, 4]
print(sortArrayByParity(nums))  # Output: [2,4,3,1] or [4,2,3,1]



# ============================================================
# 🧾 Summary Comparison
# ============================================================
# | Approach       | Time  | Space | Notes                     |
# |----------------|-------|--------|----------------------------|
# | Brute Force    | O(n)  | O(n)   | Uses extra arrays          |
# | Two Pointers   | O(n)  | O(1)   | ✅ Best — in-place swap     |
# ============================================================
