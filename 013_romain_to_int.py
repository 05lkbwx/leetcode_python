# world's fastest
def romanToInt(s):
    romans = {'M': 1000, 'D': 500 , 'C': 100, 'L': 50, 'X': 10,'V': 5,'I': 1}
    prev_value = running_total =0
    for i in range(len(s) - 1, -1, -1):
        int_val = romans[s[i]]
        if int_val < prev_value:
            running_total -= int_val
        else:
            running_total += int_val
        prev_value = int_val
    return running_total

# # my solution
# def romanToInt(s):
# 	def kick_off(s, romains, scale):
# 		if len(s) > 0:
# 			i = len(romains) - 1
# 			while i >= 0:
# 			 	if len(s) >= len(romains[i]) and s[:len(romains[i])] == romains[i]:
# 			 		return (i + 1) * scale, len(romains[i])
# 			 	i = i - 1
# 			return 0, 0
# 		return 0, 0

# 	result_i = 0
# 	cur_idx  = 0
# 	M = ["M", "MM", "MMM"]
# 	C = ["C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
# 	X = ["X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
# 	I = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
# 	delta_i, delta_idx = kick_off(s[cur_idx:], M, 1000);	result_i = result_i + delta_i;	cur_idx  = cur_idx  + delta_idx;
# 	delta_i, delta_idx = kick_off(s[cur_idx:], C, 100);		result_i = result_i + delta_i;	cur_idx  = cur_idx  + delta_idx;
# 	delta_i, delta_idx = kick_off(s[cur_idx:], X, 10);		result_i = result_i + delta_i;	cur_idx  = cur_idx  + delta_idx;
# 	delta_i, delta_idx = kick_off(s[cur_idx:], I, 1);		result_i = result_i + delta_i;	cur_idx  = cur_idx  + delta_idx;
# 	return result_i

if __name__ == '__main__':
	s = 'DCXXI'
	print romanToInt(s)