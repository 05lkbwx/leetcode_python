# world' fastest
def combinationSum2(self, candidates, target):
    candidates.sort()
    stackc, res = [(0, 0, [])], []
    while stackc:
        total, idx, path = stackc.pop()
        if total == target:
            res.append(path)
            continue
        for i in xrange(idx, len(candidates)):
            tmpsum = total + candidates[i]
            if tmpsum > target: break
            if i > idx and candidates[i] == candidates[i-1]: continue
            stackc.append((tmpsum, i+1, path + [candidates[i]]))
    return res

# # my solution
# def combinationSum(candidates, target):
#     import ast
#     rst = cs1(candidates,target)
#     tmp = {}
#     for s in rst:
#         tmp[repr(s)] = 1
#     return [ast.literal_eval(s) for s in tmp]

# def cs1(ns,target):
#     def cs(ns, k, target):
#         if k >= len(ns):
#             return []

#         ret = []
#         for i in range(k, len(ns), 1):
#             n = ns[i]
#             if n > target: 
#                 return ret
#             if n == target:
#                 ret.append([n])
#                 return ret
#             for s in cs(ns, i + 1, target - n):
#                 s.append(n)
#                 ret.append(s)
#         return ret

#     ns = sorted(ns)    
#     return cs(ns, 0, target)

if __name__ == '__main__':
    print combinationSum([10, 1, 2, 7, 6, 1, 5], 8)
