class Solution:
    def reverse(self, x: int) -> int:
        temp = 0
        is_neg=False
        if x < 0:
            is_neg = True
            x *= -1
        while True:
            if abs(temp) >= 2147483647:
                return 0
            if x == 0:
                return temp if not is_neg else temp*-1
                #return temp
            ones_val = x %10
            x = round((x/10)-(x%10/10))
            temp = temp*10 + ones_val
