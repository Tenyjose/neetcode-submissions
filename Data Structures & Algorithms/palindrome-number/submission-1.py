class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        
        div = 1
        while x >= 10*div:
            div *= 10

        while x:
            left = x%10
            right = x //div

            if left != right:
                return False

            #x = x%div  # chooping of the left digit, 1221 becomes 221
            #x = x//10  # chooping of the right digit, 221 becomes 22
            x = (x%div) // 10

            div = div // 100

        return True
            
