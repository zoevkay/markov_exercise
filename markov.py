import random


# EDIT README TO REFLECT CHANGES

def process_file(filename):
	dictionary = {}

	newfile = open(filename)
	line = newfile.readline()
	newfile.close()
	
	#use .readlines() to divide txt into a list of lines.

	wordlist = line.split()
	if len(wordlist) > 0:
		n = 0
		#start loop here
		while n < len(wordlist) - 2:
			prefix =  (wordlist[n], wordlist[n+1])
			suffix = []
			suffix.append(wordlist[n+2])
			dictionary[prefix] = suffix
			n += 1

	else:
		pass
	return dictionary

def shift(muple, anything):
	new_tuple = (muple[1],anything)
	return new_tuple

def build_sentence(mapping):
	# take random key from dictionary, create a string with key and one value.
	prefix = random.choice(mapping.keys())
	suffix = random.choice(mapping[prefix])
	sentence = prefix[0] + " " + prefix[1] + " " + suffix
	return sentence




def main():
	d = process_file("sample2.txt")
	print build_sentence(d)

if __name__ == "__main__":
	main()