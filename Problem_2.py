class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        result = []

        def ispalindrome(s):
            if(s == ''):
                return True
            i = 0
            j = len(s)-1
            while(i<j):  
                if(s[i] == s[j]):
                    i = i+1
                    j = j-1
                else:
                    return False
            return True


        def recur(s,arr):
            
            if(len(s) == 0):
                result.append(arr.copy())
            else:
                for i in range(len(s)):
                    temp = s[:i+1]
                    if(ispalindrome(temp)):
                        arr.append(temp)
                        recur(s[i+1:],arr)
                        arr.pop(-1)

            
            
        recur(s,[])
        return result  


    

  