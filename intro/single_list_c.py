lowercase = 'abcdefghijklmnopqrstuvwxyz'
digits = '0123456789'

def get_all_possible(lowercase, digits):
	list = []
	for one in lowercase:
		for two in lowercase:
			for three in digits:
				for four in digits:
					list.append(one+two+three+four)
	return list 

list = get_all_possible(lowercase, digits);
# print list

answer = [i+j+k+l for i in lowercase for j in lowercase for k in digits for l in digits]
print answer == list