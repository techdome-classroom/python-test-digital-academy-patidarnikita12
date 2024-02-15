class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        list1 = []
        mydict ={")":"(","}":"{","]":"["}
        for char in s:
            if char in mydict:
                element1 = list1.pop() if list1 else '#'
                if mydict[char]!= element1:
                    return False
            else:
                list1.append(char)
        return not list1
    

obj1 = Solution()
print(obj1.isValid(""))

  

