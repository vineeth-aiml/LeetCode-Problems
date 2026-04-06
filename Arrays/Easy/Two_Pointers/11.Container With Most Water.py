# 🔹 11. Container With Most Water
# Pattern: Two Pointers (Opposite Direction)
# Category: Array

# =========================================================
# 🧩 Problem:
# heights array icharu
# Prathi index oka vertical line height ni represent chestundi
# 2 lines select chesi, x-axis tho kalipi container form avutundi
# Aa container lo maximum water entha hold chestundo find cheyali
# =========================================================

# 📥 Input:
# [1,8,6,2,5,4,8,3,7]

# 📤 Output:
# 49

# Explanation:
# index 1 height = 8
# index 8 height = 7
# width = 8 - 1 = 7
# min height = 7
# area = 7 * 7 = 49

# =========================================================
# ⚠️ Constraints (ELA IDENTIFY CHEYALI)
# =========================================================
# 2 lines choose cheyali
# maximum area kavali
# brute force lo anni pairs check chestham
# optimize cheyali ante two pointers observation kavali

# =========================================================
# ⚠️ Edge Cases
# =========================================================
# [1,1] → 1
# [4,3,2,1,4] → 16
# [1,2,1] → 2
# Minimum 2 elements untayi
# Equal heights unna case handle cheyali

# =========================================================
# 🧠 APPROACH 1: BRUTE FORCE
# =========================================================
# Idea:
# Prathi pair (i, j) try chesi
# area = (j - i) * min(height[i], height[j])
# maximum area track cheyyali

def max_area_bruteforce(height):
    n = len(height)
    max_water = 0

    for i in range(n):
        for j in range(i + 1, n):
            width = j - i
            h = min(height[i], height[j])
            area = width * h
            max_water = max(max_water, area)

    return max_water

# Time: O(n^2) ❌
# Space: O(1)


# =========================================================
# 🧠 APPROACH 2: OPTIMAL (Two Pointers)
# =========================================================
# Idea:
# Left pointer start nundi
# Right pointer end nundi
# Area calculate cheyyi
# Smaller height unna pointer ni move cheyyali
#
# Why?
# Area depends on:
# 1. width
# 2. smaller height
#
# Width anyway decrease avtundi pointer move chesthe
# So smaller height improve avvali ante
# smaller pointer ni move cheyyadam matrame use

def max_area_optimal(height):
    l = 0
    r = len(height) - 1
    max_water = 0

    while l < r:
        width = r - l
        h = min(height[l], height[r])
        area = width * h
        max_water = max(max_water, area)

        # smaller height pointer move cheyyi
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1

    return max_water

# Time: O(n) ✅
# Space: O(1) ✅


# =========================================================
# 🔍 DRY RUN (Optimal)
# =========================================================
# height = [1,8,6,2,5,4,8,3,7]

# Step 1:
# l = 0, r = 8
# width = 8
# min height = min(1,7) = 1
# area = 8 * 1 = 8
# max_water = 8
# smaller = left (1) → l += 1

# Step 2:
# l = 1, r = 8
# width = 7
# min height = min(8,7) = 7
# area = 7 * 7 = 49
# max_water = 49
# smaller = right (7) → r -= 1

# Step 3:
# l = 1, r = 7
# width = 6
# min height = min(8,3) = 3
# area = 18
# max_water = 49
# smaller = right → r -= 1

# Step 4:
# l = 1, r = 6
# width = 5
# min height = min(8,8) = 8
# area = 40
# max_water = 49
# equal heights → r -= 1

# Continue...
# Final answer = 49


# =========================================================
# 🚀 APPROACH COMPARISON
# =========================================================
# Brute Force:
# + Straightforward
# - All pairs check cheyali
# - O(n^2) slow

# Optimal:
# + O(n)
# + Two pointers perfect use case
# + Interview lo very common and important


# =========================================================
# 🧠 FINAL THINKING FLOW
# =========================================================
# 1. 2 lines pick chesi max area kavali
# 2. First brute force alochana:
#    every pair check cheddam
# 3. But O(n^2) too slow
# 4. Observe:
#    area = width * min(left_height, right_height)
# 5. Width pointer move chesthe thaggutundi
# 6. So area increase kavali ante smaller height improve avvali
# 7. Anduke smaller height pointer ni move chestham
# 8. Bigger height pointer move chesthe use undadu
#    because limiting factor smaller one


# =========================================================
# ✅ Example Run
# =========================================================
arr = [1,8,6,2,5,4,8,3,7]

print("Brute Force:", max_area_bruteforce(arr))
print("Optimal:", max_area_optimal(arr))