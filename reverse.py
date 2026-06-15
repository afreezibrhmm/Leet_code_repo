def reverse(s):
    l = 0
    r = len(s)-1

    while l< r:
        s[l],s[r]=s[r],s[l]
        l+=1
        r-=1
    return s
letters = ["p","y","t","h","o","n"]
print(f"original:{letters}")

reverse(letters)
print(f"reversed:{letters}")