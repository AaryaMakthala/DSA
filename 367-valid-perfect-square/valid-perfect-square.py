class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        k=int(num**0.5)
        k=k*k
        if k == num:
            return True
        else:
            return False

        