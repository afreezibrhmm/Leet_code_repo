from collections import Counter

def anagram(s,t):
    if len(s)!=len(t):
        return False
    return Counter(s)==Counter(t)

w1,w2 = "bike","kibe"
w3,w4 = "rat","cat"

print(f"Is the w1 and w2 are anagrams?",anagram(w1,w2))
print(f"Is the w3 and w4 are anagrams?",anagram(w3,w4))
