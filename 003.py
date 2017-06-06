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
