a = [900 + i for i in range(100)]

def is_palindrome(i):
	i = str(i)
	k = len(i)
	if i[:k//2][::-1] == i[(k+1)//2:]:
		return True
	else:
		return False
	
three_digit_product_palindromes = []
	
for i, v in enumerate(a):
	for j in a[i:]:
		if is_palindrome(v*j):
			three_digit_product_palindromes.append(v*j)
				
print max(three_digit_product_palindromes)