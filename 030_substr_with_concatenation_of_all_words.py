# world's fastest
def findSubstring(self, s, words):
    """
    :type s: str
    :type words: List[str]
    :rtype: List[int]
    """
    if not s or words==[]:
        return []
        
    lenstr=len(s)
    lenword=len(words[0])
    lensubstr=len(words)*lenword
    times={}
    
    for word in words:
        if word in times:
            times[word]+=1
        else:
            times[word]=1
            
    ans=[]
    for i in xrange(min(lenword,lenstr-lensubstr+1)):
        self.findAnswer(i,lenstr,lenword,lensubstr,s,times,ans)
    return ans
    
def findAnswer(self,strstart,lenstr,lenword,lensubstr,s,times,ans):
    wordstart=strstart
    curr={}
    while strstart+lensubstr<=lenstr:
        word=s[wordstart:wordstart+lenword]
        wordstart+=lenword
        if word not in times:
            strstart=wordstart
            curr.clear()
        else:
            if word in curr:
                curr[word]+=1
            else:
                curr[word]=1
            while curr[word]>times[word]:
                curr[s[strstart:strstart+lenword]]-=1
                strstart+=lenword
            if wordstart-strstart==lensubstr:
                ans.append(strstart)

# # my solution
# def findSubstring(s, words):
#     """
#     :type s: str
#     :type words: List[str]
#     :rtype: List[int]
#     """
#     res        = []
#     solution_dict = {w : 0 for w in words}
#     for w in words:
#     	solution_dict[w] += 1

#     for t in range(len(words[0])):
#     	s_words = []
#     	k       = t
#     	while k + len(words[0]) <= len(s):
#     		s_words.append(s[k:(k + len(words[0]))])
#     		k += len(words[0])
#     	# print 's_words is,', s_words

#     	if len(words) > len(s_words):
#     		continue

#     	moving_window_dict = {w : 0 for w in words}
#     	for i in range(len(words)):
#     		if s_words[i] in moving_window_dict:
#     			moving_window_dict[s_words[i]] += 1

#     	if moving_window_dict == solution_dict:
#     		res.append(t)

#     	if len(s_words) > len(words):
#     		for i in range(1, len(s_words) - len(words) + 1, 1):
#     			if s_words[i - 1] in moving_window_dict:
#     				moving_window_dict[s_words[i - 1]] -= 1
#     			if s_words[i + len(words) - 1] in moving_window_dict:
#     				moving_window_dict[s_words[i + len(words) - 1]] += 1
#     			if moving_window_dict == solution_dict:
#     				res.append(t + i * len(words[0]))

#     return res

if __name__ == '__main__':
	s = "wordgoodgoodgoodbestword"
	words = ["word","good","best","good"]
	print findSubstring(s, words)