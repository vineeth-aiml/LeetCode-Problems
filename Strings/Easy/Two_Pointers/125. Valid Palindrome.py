# # 125. Valid Palindrome

# ## Problem
# Check if a string is a palindrome after converting uppercase to lowercase and removing non-alphanumeric characters.

# ### Examples
# - `"A man, a plan, a canal: Panama"` → `true`  
# - `"race a car"` → `false`  
# - `" "` → `true`  

# ---

# ## Brute Force (Steps)
# 1. Lowercase the string.  
# 2. Remove non-alphanumeric characters.  
# 3. Reverse the string and compare with original.  
# - Time: O(n), Space: O(n)  

def isPalindrome(s):
    s = s.lower()
    cleaned = ''
    for ch in s:
        if ch.isalnum():
            cleaned+=ch
    return cleaned == cleaned[::-1]
s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))
# ---

# ## Two Pointers (Steps)
# 1. Initialize `left = 0`, `right = len(s)-1`.  
# 2. While `left < right`:  
#    - Skip non-alphanumeric characters.  
#    - Compare lowercase `s[left]` and `s[right]`.  
#    - If unequal, return `false`.  
#    - Move `left++` and `right--`.  
# 3. Return `true`.  
# - Time: O(n), Space: O(1)  


def isPalindrome(s):
    l = 0
    r = len(s)-1

    while l < r:

        if not s[l].isalnum():
            l+=1
            continue
        if not s[r].isalnum():
            r-=1
            continue

        if s[l].lower() != s[r].lower():
            return False
        l+=1
        r-=1
    return True
s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))

