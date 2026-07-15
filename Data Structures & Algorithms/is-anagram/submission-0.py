class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)== len(t):
            count_s = {}
            count_t = {}
            for let_s in s:
                if let_s in count_s:
                    count_s[let_s]+=1
                else:
                    count_s[let_s]=1
            for let_t in t:
                if let_t in count_t:
                    count_t[let_t]+=1
                else:
                    count_t[let_t]=1
            if count_s == count_t:
                return True
        return False

        
        