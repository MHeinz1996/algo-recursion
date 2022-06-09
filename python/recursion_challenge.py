def factorial(x):
	if x == 1:
		return 	1
	else:
		return x * factorial(x-1)

def palindrome(word):
	new_word = [str(x.lower()) for x in word if x != ' ']

	if len(new_word) <= 1:
		return True
	elif new_word[0] != new_word[len(new_word)-1]:
		return False
	else:
		if str(new_word[0]) == str(new_word[len(new_word)-1]):
			new_word.pop(0)
			new_word.pop()
			return palindrome(new_word)
		else:
			return False

def bottles(num):
	if num == 2:
		return f"{num} bottles of beer on the wall, {num} bottles of beer.\nTake one down and pass it around, {num-1} more bottle of beer on the wall.\n1 bottle of beer on the wall, 1 bottle of beer.\nTake one down and pass it around, no more bottles of beer on the wall.\nNo more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, 99 bottles of beer on the wall."
	else:
		return f"{num} bottles of beer on the wall, {num} bottles of beer.\nTake one down and pass it around, {num-1} more bottles of beer on the wall." + f"\n{bottles(num-1)}"

def roman_num(num):
	roman_numeral_to_arabic_map = {
		'M': 1000,
		'CM': 900,
		'D': 500,
		'CD': 400,
		'C': 100,
		'XC': 90,
		'L': 50,
		'XL': 40,
		'X': 10,
		'IX': 9,
		'V': 5,
		'IV': 4,
		'I': 1,
	}
	
	if num == 0:
		return ''
	else:
		for key in roman_numeral_to_arabic_map:
			if((num/roman_numeral_to_arabic_map[key]) >= 1):
				return f"{key}" + f"{roman_num(num - roman_numeral_to_arabic_map[key])}"

print(palindrome('Race car'))