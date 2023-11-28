class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x <0:
            return False
        if x/10 <1:
            return True
        temp=0

        while True:


            if x/10 <1:
                return False
            ones_val = x%10
            x= round((x/10)-(x%10/10))
            if x==temp:
                return True
            temp = (temp*10) + ones_val
            if temp==0:
                #this is first time round ending in zero
                return False
            if temp == x:
                return True






