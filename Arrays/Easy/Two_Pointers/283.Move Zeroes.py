# 🔹 283. Move Zeroes
# Pattern: Two Pointers (Same Direction)
# Category: Array

# =========================================================
# 🧩 Problem:
# Array lo unna 0 values anni end ki move cheyali
# Migatha non-zero elements order same undali
# In-place ga modify cheyali
# =========================================================

# 📥 Input:
# [0,1,0,3,12]

# 📤 Output:
# [1,3,12,0,0]

# =========================================================
# ⚠️ Constraints (ELA IDENTIFY CHEYALI)
# =========================================================
# "in-place" → new array create cheyakudadhu
# "order same undali" → non-zero elements relative order preserve avvali
# "modify directly" → return cheyyalsina avasaram ledu

# =========================================================
# ⚠️ Edge Cases
# =========================================================
# [] → []
# [0] → [0]
# [1] → [1]
# [0,0,0] → [0,0,0]
# [1,2,3] → [1,2,3]
# [0,1,0,0,2] → [1,2,0,0,0]

# =========================================================
# 🧠 APPROACH 1: BRUTE FORCE
# =========================================================
# Idea:
# Non-zero values ni temp list lo collect chesi
# tarvata original array lo copy chesi
# remaining positions lo zero fill cheyadam

def move_zeroes_bruteforce(nums):
    temp = []

    # non-zero values collect cheyyi
    for num in nums:
        if num != 0:
            temp.append(num)

    # temp ni original array lo copy cheyyi
    for i in range(len(temp)):
        nums[i] = temp[i]

    # remaining positions lo zero fill cheyyi
    for i in range(len(temp), len(nums)):
        nums[i] = 0

# Time: O(n)
# Space: O(n) ❌


# =========================================================
# 🧠 APPROACH 2: BETTER (Overwrite)
# =========================================================
# Idea:
# First non-zero elements ni front lo overwrite cheyyi
# tarvata remaining places lo zero pettu

def move_zeroes_better(nums):
    insert_pos = 0

    for i in range(len(nums)):
        if nums[i] != 0:
            nums[insert_pos] = nums[i]
            insert_pos += 1

    while insert_pos < len(nums):
        nums[insert_pos] = 0
        insert_pos += 1

# Time: O(n)
# Space: O(1) ✅


# =========================================================
# 🧠 APPROACH 3: OPTIMAL (Two Pointers)
# =========================================================
# Idea:
# l = next position where non-zero should come
# r = current traversal pointer
# non-zero kanipiste l position tho swap cheyyi

def move_zeroes_optimal(nums):
    l = 0

    for r in range(len(nums)):
        if nums[r] != 0:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1

# Time: O(n)
# Space: O(1) ✅


# =========================================================
# 🔍 DRY RUN (Optimal)
# =========================================================
# nums = [0,1,0,3,12]

# Start:
# l = 0

# r = 0 → nums[r] = 0
# zero kabatti skip
# [0,1,0,3,12]

# r = 1 → nums[r] = 1
# swap nums[l], nums[r] => swap nums[0], nums[1]
# [1,0,0,3,12]
# l = 1

# r = 2 → nums[r] = 0
# zero kabatti skip
# [1,0,0,3,12]

# r = 3 → nums[r] = 3
# swap nums[1], nums[3]
# [1,3,0,0,12]
# l = 2

# r = 4 → nums[r] = 12
# swap nums[2], nums[4]
# [1,3,12,0,0]
# l = 3

# Final Output:
# [1,3,12,0,0]


# =========================================================
# 🚀 APPROACH COMPARISON
# =========================================================
# Brute Force:
# + Easy
# - Extra array use chestundi

# Better:
# + O(1) space
# + Easy implementation
# - overwrite concept ardham undali

# Optimal:
# + O(1) space
# + order preserve avutundi
# + interview favorite


# =========================================================
# 🧠 FINAL THINKING FLOW
# =========================================================
# 1. Zeroes ni end ki move cheyali
# 2. Non-zero order same undali
# 3. First brute force alochana → temp list
# 4. But extra space vadakudadhu
# 5. Observe:
#    non-zero elements ni left side ki move chesthe saripothundi
# 6. So one pointer place maintain chestundi
# 7. Inko pointer traverse chestundi
# 8. Non-zero vachinappudu swap


# =========================================================
# ✅ Example Run
# =========================================================
nums1 = [0,1,0,3,12]
move_zeroes_bruteforce(nums1)
print("Brute:", nums1)

nums2 = [0,1,0,3,12]
move_zeroes_better(nums2)
print("Better:", nums2)

nums3 = [0,1,0,3,12]
move_zeroes_optimal(nums3)
print("Optimal:", nums3)