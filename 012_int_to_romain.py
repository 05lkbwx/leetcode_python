# world's fastest
def intToRoman(num):
    M = ["", "M", "MM", "MMM"];
    C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"];
    X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"];
    I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"];
    return M[num/1000] + C[(num%1000)/100] + X[(num%100)/10] + I[num%10];

## some guy's short solution
# def intToRoman(num):
# 	romanPieces = ["","I","II","III","IV","V","VI","VII","VIII","IX", "","X","XX","XXX","XL","L","LX","LXX","LXXX","XC", "","C","CC","CCC","CD","D","DC","DCC","DCCC","CM", "","M","MM","MMM","MMMM"]
# 	return romanPieces[num / 1000 + 30] + romanPieces[(num / 100) % 10 + 20] + romanPieces[(num / 10) % 10 + 10] + romanPieces[num % 10]

# # my solution
# def intToRoman(num):
#     """
#     :type num: int
#     :rtype: str
#     """
#     romains = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
#     lv_idx  = {0:'M', 1:'D', 2:'C', 3:'L', 4:'X', 5:'V', 6:'I'}
#     cur_lv  = 0
#     resid   = num
#     result  = ''
#     while resid > 0:
#     	while romains[lv_idx[cur_lv]] > resid:
#     		cur_lv = cur_lv + 1
#     	result = result + lv_idx[cur_lv]
#     	resid  = resid  - romains[lv_idx[cur_lv]]
#     return result

if __name__ == '__main__':
	num = 10
	print intToRoman(num)