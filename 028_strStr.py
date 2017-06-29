# world's fastest
def strStr(self, haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    return haystack.find(needle)

# # my solution
# def strStr(haystack, needle):
#     """
#     :type haystack: str
#     :type needle: str
#     :rtype: int
#     """
#     if needle == "":
#         return 0

#     if len(haystack) < len(needle):
#         return -1

#     for i in range(0, len(haystack) - len(needle) + 1, 1):
#     	if haystack[i:(i + len(needle))] == needle:
#     		return i
#     return -1

if __name__ == '__main__':
	s = 'homework'
	print s[2:(2+3)]