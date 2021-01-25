def num_to_word(n):
	ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
	ten = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
	tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
	if n < 10:
		return ones[n]
	if n == 10:
		return ten[0]
	if n>10 and n<20:
		return ten[n-10]
	if n==20:
		return tens[2]
	if n>20 and n<100:
		if n%10 == 0:
			return tens[n/10]
		else:
			return tens[n/10] + "-" + ones[n%10]
	else:
		if n == 1000:
			return "one thousand"
		elif n%100 == 0:
			return ones[n/100] + " hundred"
		else:
			return ones[n/100] + " hundred and " + num_to_word(n%100)
		
def count_letters(n):
	w = num_to_word(n)
	w = w.replace(" ", "")
	w = w.replace("-", "")
	return len(w)
	
		
print sum([count_letters(i) for i in range(1, 1001)])