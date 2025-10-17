# ============================================================
# 922. Sort Array By Parity II
# ============================================================

# 🧩 Problem:
# Given an integer array nums, half of the integers in nums are odd,
# and the other half are even.
#
# Sort the array so that:
#   - nums[i] is even when i is even
#   - nums[i] is odd  when i is odd
#
# Return any array that satisfies this condition.
#
# ------------------------------------------------------------
# Example 1:
# Input:  nums = [4,2,5,7]
# Output: [4,5,2,7]
#
# Example 2:
# Input:  nums = [2,3]
# Output: [2,3]
# ------------------------------------------------------------
#
# Constraints:
# 2 <= len(nums) <= 2 * 10^4
# len(nums) is even.
# Half of the integers in nums are even.
# 0 <= nums[i] <= 1000
# ------------------------------------------------------------
#
# 🧠 Edge Cases:
# - nums = [0,2] → already valid
# - nums = [1,3] → invalid (since both odd, but constraint prevents this)
# - nums = [4,2,5,7]
# ------------------------------------------------------------


# ============================================================
# --- 1️⃣ Brute Force Solution ---
# ============================================================
# 🧠 Idea:
# 1. Separate even and odd numbers into two lists.
# 2. Create a new result array of the same size.
# 3. Fill even indices with even numbers.
# 4. Fill odd indices with odd numbers.
#
# ⏱️ Time:  O(n)
# 💾 Space: O(n)
# ------------------------------------------------------------

def sortArrayByParityII(nums):
    evens = []
    odds = []

    # Step 1: Split numbers
    for num in nums:
        if num % 2 == 0:
            evens.append(num)
        else:
            odds.append(num)

    # Step 2: Fill result
    result = [0] * len(nums)
    even_i, odd_i = 0, 1

    for e in evens:
        result[even_i] = e
        even_i += 2
    for o in odds:
        result[odd_i] = o
        odd_i += 2

    return result


# ✅ Test Brute Force
nums = [4, 2, 5, 7]
print(sortArrayByParityII(nums))  # Output: [4,5,2,7]



# ============================================================
# --- 2️⃣ Two Pointers (Optimized In-Place) ---
# ============================================================
# 🧠 Idea:
# - Use two pointers:
#     even = 0 → points to even index
#     odd  = 1 → points to odd index
# - Move through array:
#     - If nums[even] is odd and nums[odd] is even → swap.
#     - Else → move pointer forward if it’s already correct.
#
# ✅ Works in-place without extra array.
#
# ⏱️ Time:  O(n)
# 💾 Space: O(1)
# ------------------------------------------------------------

def sortArrayByParityII(nums):
    n = len(nums)
    even, odd = 0, 1

    while even < n and odd < n:
        if nums[even] % 2 == 0:
            even += 2
        elif nums[odd] % 2 == 1:
            odd += 2
        else:
            # Swap misplaced elements
            nums[even], nums[odd] = nums[odd], nums[even]
            even += 2
            odd += 2

    return nums


# ✅ Test Optimized
nums = [4, 2, 5, 7]
print(sortArrayByParityII(nums))  # Output: [4,5,2,7] (or any valid variation)



# ============================================================
# 🧾 Summary Comparison
# ============================================================
# | Approach       | Time | Space | Notes |
# |----------------|------|--------|--------|
# | Brute Force    | O(n) | O(n)   | Uses extra arrays for evens/odds |
# | Two Pointers   | O(n) | O(1)   | ✅ In-place and efficient |
# ============================================================
