import collections
def main():
	string = input("welcome to list maker and reorganizer, please input and combination of integers seperated by commas: ")
	
	try:
		digits = [int(x) for x in string.split(",")]
		print("we will now move each digit to the right two positions and add 5")
		digits = map(lambda x: x + 5, digits)
		w = collections.deque(digits)
		w.rotate(2)
		print(w)
	except:
		print("invalid entry")
		return False

main()