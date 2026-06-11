def ispalindrome(text):
    cleaned_text = "".join(text.split()).lower()
    return cleaned_text ==cleaned_text[::-1]

word1 = "hello"
word2 = "coding"

print(f"palindrome of {word1} is : {ispalindrome(word1)}")
print(f"palindrome of {word2} is : {ispalindrome(word2)}")