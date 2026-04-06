# 🔹 167. Two Sum II - Input Array Is Sorted
# Pattern: Two Pointers (Opposite Direction)
# Category: Array

# =========================================================
# 🧩 Problem:
# Sorted array icharu
# 2 numbers select chesi target sum ravali
# Return 1-based indices of those 2 numbers
# Exactly one solution untundi
# Same element ni rendu sarlu use cheyakudadhu
# =========================================================

# 📥 Input:
# numbers = [2,7,11,15], target = 9

# 📤 Output:
# [1,2]

# Explanation:
# 2 + 7 = 9
# indices are 1 and 2 (1-based indexing)

# =========================================================
# ⚠️ Constraints (ELA IDENTIFY CHEYALI)
# =========================================================
# Array already sorted undi
# Exactly one solution untundi
# Extra space avoid cheyyachu
# Sorted array ante two pointers strong hint

# =========================================================
# ⚠️ Edge Cases
# =========================================================
# [2,7], target=9 → [1,2]
# Negative numbers unna cases kuda untayi
# Large numbers unna cases kuda untayi
# Same index use cheyakudadhu
# 1-based indexing marchipokudadhu

# =========================================================
# 🧠 APPROACH 1: BRUTE FORCE
# =========================================================
# Idea:
# Prathi pair check cheyyi
# sum == target aithe indices return cheyyi

def two_sum_bruteforce(numbers, target):
    n = len(numbers)

    for i in range(n):
        for j in range(i + 1, n):
            if numbers[i] + numbers[j] == target:
                return [i + 1, j + 1]

# Time: O(n^2) ❌
# Space: O(1)


# =========================================================
# 🧠 APPROACH 2: BETTER (Hash Map)
# =========================================================
# Idea:
# Complement = target - current
# already seen aithe answer dorukutundi
# But sorted property ni use cheyyatledu

def two_sum_better(numbers, target):
    seen = {}

    for i in range(len(numbers)):
        complement = target - numbers[i]

        if complement in seen:
            return [seen[complement] + 1, i + 1]

        seen[numbers[i]] = i

# Time: O(n)
# Space: O(n) ❌


# =========================================================
# 🧠 APPROACH 3: OPTIMAL (Two Pointers)
# =========================================================
# Idea:
# Left pointer start nundi
# Right pointer end nundi
# current_sum calculate cheyyi
#
# current_sum == target → answer
# current_sum < target  → left ni move cheyyi (sum penchali)
# current_sum > target  → right ni move cheyyi (sum taggali)

def two_sum_optimal(numbers, target):
    l = 0
    r = len(numbers) - 1

    while l < r:
        current_sum = numbers[l] + numbers[r]

        if current_sum == target:
            return [l + 1, r + 1]

        elif current_sum < target:
            l += 1

        else:
            r -= 1

# Time: O(n) ✅
# Space: O(1) ✅


# =========================================================
# 🔍 DRY RUN (Optimal)
# =========================================================
# numbers = [2,7,11,15], target = 9

# Step 1:
# l = 0, r = 3
# current_sum = 2 + 15 = 17
# 17 > 9
# sum ekkuva undi kabatti right pointer ni left ki move cheyyi
# r = 2

# Step 2:
# l = 0, r = 2
# current_sum = 2 + 11 = 13
# 13 > 9
# malli sum ekkuva
# r = 1

# Step 3:
# l = 0, r = 1
# current_sum = 2 + 7 = 9
# target match ayyindi
# return [1, 2]


# =========================================================
# 🚀 APPROACH COMPARISON
# =========================================================
# Brute Force:
# + Easy
# - O(n^2) slow

# Better (Hash Map):
# + O(n) time
# - O(n) extra space
# - Sorted array advantage waste chestundi

# Optimal (Two Pointers):
# + O(n) time
# + O(1) space
# + Sorted property full use chestundi
# + Interview lo best answer


# =========================================================
# 🧠 FINAL THINKING FLOW
# =========================================================
# 1. 2 numbers sum target ravali
# 2. First brute force:
#    anni pairs check cheddam
# 3. But O(n^2) slow
# 4. Hash map tho O(n) cheyyachu
# 5. Kani array already sorted ani important clue undi
# 6. Sorted array lo:
#    small value left lo untundi
#    big value right lo untundi
# 7. current sum takkuva aithe left move chestham
#    because bigger value kavali
# 8. current sum ekkuva aithe right move chestham
#    because smaller value kavali
# 9. Ila one pass lo answer dorukutundi


# =========================================================
# ✅ Example Run
# =========================================================
numbers = [2,7,11,15]
target = 9

print("Brute Force:", two_sum_bruteforce(numbers, target))
print("Better:", two_sum_better(numbers, target))
print("Optimal:", two_sum_optimal(numbers, target))