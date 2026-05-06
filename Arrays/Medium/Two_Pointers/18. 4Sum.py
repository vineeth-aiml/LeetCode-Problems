# 🔹 18. 4Sum
# Pattern: Two Pointers + Sorting
# Category: Array

# =========================================================
# 🧩 Problem:
# Oka integer array nums and target istaru
#
# 4 distinct elements select chesi
# vaalla sum target ki equal avvali
#
# Unique quadruplets matrame return cheyali
# =========================================================

# 📥 Input:
# nums = [1,0,-1,0,-2,2]
# target = 0

# 📤 Output:
# [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

# Explanation:
# 4 numbers combinations target ki equal ayyevi:
#
# -2 + -1 + 1 + 2 = 0
# -2 + 0 + 0 + 2 = 0
# -1 + 0 + 0 + 1 = 0

# =========================================================
# ⚠️ Constraints (ELA IDENTIFY CHEYALI)
# =========================================================
# nums length up to 200
#
# Brute force O(n^4) possible
# But very expensive
#
# Unique quadruplets kavali
# Duplicates avoid cheyali
#
# Sorting + Two pointers best approach

# =========================================================
# ⚠️ Edge Cases
# =========================================================
# [] → []
#
# [1,2,3], target = 100
# → []
#
# [2,2,2,2], target = 8
# → [[2,2,2,2]]
#
# Negative numbers untayi
# Duplicate values untayi

# =========================================================
# 🧠 APPROACH 1: BRUTE FORCE
# =========================================================
# Idea:
#
# 4 nested loops use chesi
# Every possible quadruplet try cheyyi
#
# Sum target ki equal aithe
# result lo add cheyyi
#
# Duplicates avoid cheyadaniki
# set use chestham

def four_sum_bruteforce(nums, target):

    n = len(nums)
    result = set()

    for i in range(n):

        for j in range(i + 1, n):

            for k in range(j + 1, n):

                for l in range(k + 1, n):

                    total = (
                        nums[i]
                        + nums[j]
                        + nums[k]
                        + nums[l]
                    )

                    if total == target:

                        quad = tuple(sorted([
                            nums[i],
                            nums[j],
                            nums[k],
                            nums[l]
                        ]))

                        result.add(quad)

    return [list(x) for x in result]

# Time: O(n^4) ❌
# Space: O(number of quadruplets)

# =========================================================
# 🧠 APPROACH 2: OPTIMAL
# =========================================================
# Idea:
#
# First array ni sort cheyyi
#
# First 2 numbers ni loops tho fix chestham
#
# Remaining 2 numbers kosam
# left and right pointers use chestham
#
# total small aithe:
# left++
#
# total large aithe:
# right--
#
# total == target aithe:
# answer add cheyyi
#
# duplicates skip cheyyi

def four_sum_optimal(nums, target):

    nums.sort()

    n = len(nums)

    result = []

    for i in range(n - 3):

        # duplicate i skip
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        for j in range(i + 1, n - 2):

            # duplicate j skip
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue

            left = j + 1
            right = n - 1

            while left < right:

                total = (
                    nums[i]
                    + nums[j]
                    + nums[left]
                    + nums[right]
                )

                # quadruplet dorikindi
                if total == target:

                    result.append([
                        nums[i],
                        nums[j],
                        nums[left],
                        nums[right]
                    ])

                    left += 1
                    right -= 1

                    # duplicate left skip
                    while (
                        left < right and
                        nums[left] == nums[left - 1]
                    ):
                        left += 1

                    # duplicate right skip
                    while (
                        left < right and
                        nums[right] == nums[right + 1]
                    ):
                        right -= 1

                # sum small
                elif total < target:
                    left += 1

                # sum large
                else:
                    right -= 1

    return result

# Time: O(n^3) ✅
# Space: O(1) extra space ✅

# =========================================================
# 🔍 DRY RUN (Optimal)
# =========================================================
# nums = [1,0,-1,0,-2,2]
#
# Step 1:
# sort cheyyi
#
# [-2,-1,0,0,1,2]

# i = 0 -> -2
# j = 1 -> -1

# left = 2 -> 0
# right = 5 -> 2

# total:
# -2 + -1 + 0 + 2
# = -1

# small kabatti
# left++

# left = 3 -> 0
#
# total = -1 again
# left++

# left = 4 -> 1
#
# total:
# -2 + -1 + 1 + 2
# = 0 ✅

# add:
# [-2,-1,1,2]

# Continue pointers

# Next answers:
# [-2,0,0,2]
# [-1,0,0,1]

# =========================================================
# 🚀 APPROACH COMPARISON
# =========================================================
# Brute Force:
#
# + Easy to think
# - O(n^4) very slow

# Optimal:
#
# + Sorting + Two pointers
# + O(n^3)
# + Interview best solution
# + Duplicate handling easy

# =========================================================
# 🧠 FINAL THINKING FLOW
# =========================================================
# 1. 4 numbers kavali
#
# 2. First thought:
#    4 loops use cheyyadam
#
# 3. But complexity huge
#
# 4. Observe:
#    2Sum lo two pointers use chesam
#
# 5. Same logic ni extend cheyyachu
#
# 6. First 2 numbers fix chestham
#
# 7. Remaining 2 numbers
#    left/right pointers tho find chestham
#
# 8. Sorting valla
#    pointer movement easy avutundi
#
# 9. Duplicates skip cheyyali
#
# 10. total == target aithe
#     result lo add cheyyali

# =========================================================
# ✅ Example Run
# =========================================================

nums1 = [1,0,-1,0,-2,2]
target1 = 0

print("Brute Force:")
print(four_sum_bruteforce(nums1, target1))

print()

print("Optimal:")
print(four_sum_optimal(nums1, target1))

print()

nums2 = [2,2,2,2,2]
target2 = 8

print("Brute Force:")
print(four_sum_bruteforce(nums2, target2))

print()

print("Optimal:")
print(four_sum_optimal(nums2, target2))