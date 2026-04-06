# 🔹 125. Valid Palindrome
# Pattern: Two Pointers (Opposite Direction)
# Category: String

# =========================================================
# 🧩 Problem:
# Oka string icharu
# Alphanumeric characters matrame consider cheyali
# Uppercase / lowercase difference ignore cheyali
# String palindrome aa kaadha ani check cheyali
# =========================================================

# 📥 Input:
# "A man, a plan, a canal: Panama"

# 📤 Output:
# True

# Explanation:
# valid characters only teesukunte:
# "amanaplanacanalpanama"
# reverse chesina same untundi kabatti palindrome

# =========================================================
# ⚠️ Constraints (ELA IDENTIFY CHEYALI)
# =========================================================
# Special characters ignore cheyali
# Spaces ignore cheyali
# Case ignore cheyali
# So direct string compare saripodu
# Clean chesi compare cheyyachu
# Leda two pointers tho direct handle cheyyachu

# =========================================================
# ⚠️ Edge Cases
# =========================================================
# "" → True
# "a" → True
# "aa" → True
# "ab" → False
# ".,," → True   (no alphanumeric characters)
# "0P" → False

# =========================================================
# 🧠 APPROACH 1: BRUTE FORCE
# =========================================================
# Idea:
# First valid alphanumeric lowercase chars ni new string lo build cheyyi
# Tarvata reverse tho compare cheyyi

def is_palindrome_bruteforce(s):
    cleaned = ""

    for ch in s:
        if ch.isalnum():
            cleaned += ch.lower()

    return cleaned == cleaned[::-1]

# Time: O(n)
# Space: O(n) ❌


# =========================================================
# 🧠 APPROACH 2: BETTER
# =========================================================
# Idea:
# List use chesi cleaned string build cheyyadam
# string concatenation kanna better practice

def is_palindrome_better(s):
    chars = []

    for ch in s:
        if ch.isalnum():
            chars.append(ch.lower())

    cleaned = "".join(chars)
    return cleaned == cleaned[::-1]

# Time: O(n)
# Space: O(n) ❌


# =========================================================
# 🧠 APPROACH 3: OPTIMAL (Two Pointers)
# =========================================================
# Idea:
# Left pointer start nundi
# Right pointer end nundi
# Non-alphanumeric aithe skip cheyyi
# Compare lowercase characters
# mismatch aithe False
# complete aithe True

def is_palindrome_optimal(s):
    l = 0
    r = len(s) - 1

    while l < r:
        # left invalid chars skip cheyyi
        while l < r and not s[l].isalnum():
            l += 1

        # right invalid chars skip cheyyi
        while l < r and not s[r].isalnum():
            r -= 1

        # compare lowercase chars
        if s[l].lower() != s[r].lower():
            return False

        l += 1
        r -= 1

    return True

# Time: O(n) ✅
# Space: O(1) ✅


# =========================================================
# 🔍 DRY RUN (Optimal)
# =========================================================
# s = "A man, a plan, a canal: Panama"

# Step 1:
# l = 0 -> 'A'
# r = last -> 'a'
# compare 'a' and 'a' -> same

# Step 2:
# l moves to space -> skip
# r moves to 'm'
# compare 'm' and 'm' -> same

# Step 3:
# continue skipping spaces, commas, colon
# compare only valid chars

# Final:
# all matched
# return True


# =========================================================
# 🚀 APPROACH COMPARISON
# =========================================================
# Brute Force:
# + Easy to think
# - Extra cleaned string build chestundi

# Better:
# + Cleaner than repeated string concat
# - Still extra space use chestundi

# Optimal:
# + O(1) extra space
# + Direct ga original string meeda work chestundi
# + Interview lo best answer


# =========================================================
# 🧠 FINAL THINKING FLOW
# =========================================================
# 1. Palindrome ante front and back compare cheyali
# 2. But special chars ignore cheyali
# 3. Case kuda ignore cheyali
# 4. First thought:
#    cleaned string create chesi compare cheyyadam
# 5. But extra space padutundi
# 6. Observe:
#    manaki valid chars matrame compare chesthe saripothundi
# 7. So left and right pointers use chesi
#    invalid chars ni skip chestham
# 8. Valid chars compare chestham
# 9. mismatch aithe False
# 10. complete aithe True


# =========================================================
# ✅ Example Run
# =========================================================
s1 = "A man, a plan, a canal: Panama"
print("Brute Force:", is_palindrome_bruteforce(s1))
print("Better:", is_palindrome_better(s1))
print("Optimal:", is_palindrome_optimal(s1))

s2 = "race a car"
print("Brute Force:", is_palindrome_bruteforce(s2))
print("Better:", is_palindrome_better(s2))
print("Optimal:", is_palindrome_optimal(s2))