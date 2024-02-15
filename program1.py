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
                if list1:
                    element1 = list1.pop()
                else:
                    pass
                if mydict[char]!= element1:
                    return False
            else:
                list1.append(char)
        return not list1
    

object = Solution()
# print(obj1.isValid("()"))
# print(obj1.isValid("()[]{}"))
# print(obj1.isValid("(]"))
  

