def isAnagram(s , t) :
        lst = [0]*26
        for i in s:
            lst[ord(i)-97] += 1
        for i in t:
            temp = ord(i)-97
            if lst[temp] > 0:
                lst[temp] -= 1
            else:
                return False
        return sum(lst) == 0

s="anagram"
t="aaangrm"   

print(isAnagram(s,t))