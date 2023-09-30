class Solution:
    def isPalindrome(self, x: int) -> bool:
        l=[]
        s=[]
        x=str(x)
        for i in x:
            s.append(i)
            l.append(i)
        l.reverse()
        if l == s:
            return True
        else:
            return False
