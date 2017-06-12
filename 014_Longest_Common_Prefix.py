# world's fastest
def longestCommonPrefix(strs):
    if not strs:
        return("")
    strsArr = zip(*strs)
    for i, arr in enumerate(strsArr):
        if len(set(arr)) > 1:
            return(strs[0][:i])
    return(min(strs))

# # my solution
# import numpy as np
# def longestCommonPrefix(strs):
#     """
#     :type strs: List[str]
#     :rtype: str
#     """
#     # if len(strs) == 0:
#     # 	return ''
#     # for i in range(len(strs)):
#     # 	if strs[i] == "": return ''
#     if len(strs) == 0:
#         return ''

#     lengths = np.zeros(len(strs))
#     for i in range(len(strs)):	lengths[i] = len(strs[i])
#     common_len = int(min(lengths))
#     for i in range(len(strs)):	strs[i] = strs[i][:common_len]
#     conc_str = np.array(list("".join(strs)))
#     cur_indices = (common_len * np.array(range(len(strs)))).tolist()
#     for i in range(common_len):
#     	if len(set(conc_str[cur_indices])) > 1:
#     		return strs[0][:i]
#     	cur_indices = (1 + np.array(cur_indices)).tolist()
#     return strs[0][:common_len]

if __name__ == '__main__':
	# strs = ['21111', '117', '12890', '121']
	strs = [""]
	print longestCommonPrefix(strs)