class Solution(object):
    def isPalindrome(self, x):
        
        n=0
        k=x

        if x<0:
            return False
        while x!=0:
           
           n=n*10+x%10

           x=x//10 
        
        return k==n
        