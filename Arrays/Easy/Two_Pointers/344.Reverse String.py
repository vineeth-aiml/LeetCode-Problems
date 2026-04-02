# 🔹 344. Reverse String
# Pattern: Two Pointers (Opposite Direction)
# Category: Array / String

# =========================================================
# 🧩 Problem:
# Character array ni reverse cheyali (in-place)
# O(1) extra space matrame use cheyali
# Return cheyyakudadhu, direct ga modify cheyali
# =========================================================

# 📥 Input:
# ["h","e","l","l","o"]

# 📤 Output:
# ["o","l","l","e","h"]

# =========================================================
# ⚠️ Constraints (ELA IDENTIFY CHEYALI)
# =========================================================
# "in-place" → new array create cheyakudadhu
# "O(1) space" → constant memory matrame

# =========================================================
# ⚠️ Edge Cases
# =========================================================
# [] → []
# ["a"] → ["a"]
# ["x","x"] → same
# Even / Odd length handle cheyali


# =========================================================
# 🧠 APPROACH 1: BRUTE FORCE (Implementation)
# =========================================================
# Idea:
# Last nundi traverse chesi new list lo store chesi
# malli original lo copy cheyadam

def reverse_bruteforce(s):
    n = len(s)
    temp = []

    # reverse order lo fill
    for i in range(n-1, -1, -1):
        temp.append(s[i])

    # copy back
    for i in range(n):
        s[i] = temp[i]

# Time: O(n)
# Space: O(n) ❌


# =========================================================
# 🧠 APPROACH 2: BETTER (Python Built-in)
# =========================================================
# Idea:
# Python lo direct reverse function undi

def reverse_better(s):
    s.reverse()              # method 1
    # s[:] = s[::-1]         # method 2 (slice)

# Time: O(n)
# Space: O(1) (internal)
# ⚠️ Interview lo logic explain cheyyali


# =========================================================
# 🧠 APPROACH 3: OPTIMAL (Two Pointers)
# =========================================================
# Idea:
# Edges nundi swap chestu middle varaku ravali

def reverse_optimal(s):
    l = 0
    r = len(s) - 1

    while l < r:
        s[l], s[r] = s[r], s[l]
        l += 1
        r -= 1

# Time: O(n)
# Space: O(1) ✅


# =========================================================
# 🔍 DRY RUN (Optimal)
# =========================================================
# ["h","e","l","l","o"]

# Step 1:
# l=0, r=4 → swap h,o
# ["o","e","l","l","h"]

# Step 2:
# l=1, r=3 → swap e,l
# ["o","l","l","e","h"]

# Step 3:
# l=2, r=2 → STOP


# =========================================================
# 🚀 APPROACH COMPARISON
# =========================================================
# Brute Force:
# + Easy
# - Extra space

# Built-in:
# + Fast coding
# - Logic explain cheyyali

# Optimal:
# + Best (O(1) space)
# + Interview favorite


# =========================================================
# 🧠 FINAL THINKING FLOW
# =========================================================
# 1. Reverse ante → brute force alochincham
# 2. Constraint → O(1) space
# 3. Brute force reject
# 4. Observe → pairs swap
# 5. Edges → Two pointers
# 6. Implement optimal


# =========================================================
# ✅ Example Run
# =========================================================
s1 = ["h","e","l","l","o"]
reverse_bruteforce(s1)
print("Brute:", s1)

s2 = ["h","e","l","l","o"]
reverse_better(s2)
print("Better:", s2)

s3 = ["h","e","l","l","o"]
reverse_optimal(s3)
print("Optimal:", s3)