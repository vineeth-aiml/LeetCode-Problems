# 🔹 125. Valid Palindrome
# Pattern: Two Pointers (Opposite Direction)
# Category: String

# =========================================================
# 🧩 Problem:
# String palindrome aa kadha check cheyali
# Only alphanumeric characters consider cheyali
# Case insensitive (A == a)
# =========================================================

# 📥 Input:
# "A man, a plan, a canal: Panama"

# 📤 Output:
# True

# =========================================================
# ⚠️ Constraints
# =========================================================
# Ignore:
# - spaces
# - special characters
# Case insensitive compare cheyali


# =========================================================
# 🧠 APPROACH 3: OPTIMAL (Two Pointers)
# =========================================================
# Idea:
# Direct ga string meeda work cheyali
# Left & Right pointers use cheyali
# Non-alphanumeric skip cheyali


# =========================================================
# 🔁 IMPLEMENTATION STEPS (VERY IMPORTANT)
# =========================================================
# Step 1: l = 0, r = n-1 initialize chey
# Step 2: while l < r loop run chey
#
# Step 3: Left pointer clean chey
#         → alphanumeric kakapothe skip chey
#
# Step 4: Right pointer clean chey
#         → alphanumeric kakapothe skip chey
#
# Step 5: Compare characters
#         → s[l].lower() != s[r].lower() → return False
#
# Step 6: Match ayithe
#         → l++, r-- move chey
#
# Step 7: Loop complete ayithe → return True


def isPalindrome_optimal(s):
    l = 0
    r = len(s) - 1

    while l < r:

        # Step 3: left skip
        while l < r and not s[l].isalnum():
            l += 1

        # Step 4: right skip
        while l < r and not s[r].isalnum():
            r -= 1

        # Step 5: compare
        if s[l].lower() != s[r].lower():
            return False

        # Step 6: move pointers
        l += 1
        r -= 1

    # Step 7: all matched
    return True


# =========================================================
# 🔍 DRY RUN (STEP-BY-STEP FLOW)
# =========================================================
# "A man, a plan, a canal: Panama"

# Step 1:
# l=0 ('A'), r=29 ('a') → match

# Step 2:
# skip space, comma

# Step 3:
# l='m', r='m' → match

# Step 4:
# continue until middle

# Final:
# return True


# =========================================================
# 🚀 DATA FLOW UNDERSTANDING
# =========================================================
# Each iteration lo:
# 👉 invalid chars skip avuthayi
# 👉 valid chars compare avuthayi

# Total operations:
# 👉 each char at most once visit avuthundi

# So:
# Time = O(n)
# Space = O(1)


# =========================================================
# 🧠 FINAL THINKING FLOW
# =========================================================
# 1. Palindrome ante reverse compare
# 2. Brute → clean + reverse
# 3. Constraint → O(1) space
# 4. Need direct compare
# 5. Skip invalid chars
# 6. Two pointers use chey
# 7. Optimize → no extra memory


# =========================================================
# 🧠 MEMORY TRICK
# =========================================================
# 👉 "Skip → Compare → Move"
# 👉 "Invalid skip, valid compare"


# =========================================================
# ✅ Example Run
# =========================================================
s1 = "A man, a plan, a canal: Panama"
print(isPalindrome_optimal(s1))  # True

s2 = "race a car"
print(isPalindrome_optimal(s2))  # False