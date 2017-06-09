# world's best solution:
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type strs: List[str]
        :rtype: int
        """
        if not s or len(s) == 0:
            return 0
        
        start = 0
        record = 0
        dic = {}
        
        for end in range(len(s)):
            char = s[end]
            if char in dic and dic[char] >= start:
                start = dic[char] + 1
            if end - start + 1 > record:
                record = end - start + 1 
            dic[char] = end
        
        return record

# my solution:
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len  = 0
    	prev_end = -1
    	for i in range(len(s)):
    		k = prev_end + 1
    		while k < len(s) and s[k] not in list(set(s[i:k])):
    			k = k + 1
    		max_len  = max(max_len, k - i)
    		prev_end = k - 1
    	return max_len
