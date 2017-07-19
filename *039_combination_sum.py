# world's fastest
def combinationSum(self, candidates, target):
    return self.cs1(candidates,target)

def cs1(self,ns,target):
    def cs(ns,k,target):
        ret = []
        for i in xrange(k,len(ns)):
            n = ns[i]
            if n > target: return ret
            if n == target:
                ret.append([n])
                continue
            for s in cs(ns,i,target-n):
                s.append(n)
                ret.append(s)
        return ret
    
    ns.sort()
    return cs(ns,0,target)

# # my solution
# def combinationSum_helper(self, candidates, target, sol):
#     import ast
#     if target in sol:
#         return

#     rtn_res = {}
#     for v in candidates:
#         if target  - v >= 0:
#             if target - v not in sol:
#                 self.combinationSum_helper(candidates, target - v, sol)

#             if target - v == 0:
#                 rtn_res[repr([v])] = 1

#             if target - v > 0 and target - v in sol:
#                 res = [s[:] for s in sol[target - v]]

#                 for s1 in res:
#                     s = ast.literal_eval(s1)
#                     s.append(v)
#                     s = sorted(s)
#                     rtn_res[repr(s)] = 1

#     if rtn_res:
#         sol[target] = rtn_res
#     return 

# def combinationSum(self, candidates, target):
#     import ast
#     sol = {}
#     self.combinationSum_helper(candidates, target, sol)
#     if target not in sol:
#         return []
#     return [ast.literal_eval(s) for s in sol[target]]     

if __name__ == '__main__':
	print combinationSum([2,3,6,7], 7)
