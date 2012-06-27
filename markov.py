import random, string, markovddbraz, sys

# EDIT README TO REFLECT CHANGES

def process_file(filename):
	""" process_file(string) -> dictionary 
	The function reads a file and returns a dictionary built like this:
	{(word1, word2):[word3], (word2, word3): [word4, word5]}. If two consecutive words appear 
	more then once, it adds the third word as a value to that key.
	"""
	dictionary = {}
	with open(filename) as newfile:
		line = newfile.read()
	wordlist = line.split()

	if len(wordlist) > 0:
		#this is our loop to create a markov dictionary.
		for i in range(len(wordlist)-2):
			prefix =  (wordlist[i], wordlist[i+1])
			suffix = wordlist[i+2]
			if dictionary.get(prefix) is not None:
				# if current prefix is a key, add current suffix to list of values.
				dictionary[prefix].append(suffix)
			else:
				# adds a new key (current prefix) and begins a list of values with our current suffix.
				dictionary[prefix] = [suffix]

	return dictionary
 
def shift(original_tuple, anything):
	""" shift(tuple, string) -> tuple
	The function shift take a tuple and a string and return a new reversed tuple. 
	shift((1,2), 3) -> (2,3)
	"""
	new_tuple = (original_tuple[1],anything)
	return new_tuple

def build_sentence(mapping):
	""" build_sentence(dictionary) -> string
	The function takes a random key from dictionary, creates a string with the key and one
	random value from that key. It repeats this process until last string ends with !, ?, or .
	"""
	terminators = ['!', '?', '.']
	prefix = random.choice(mapping.keys())
	suffix = random.choice(mapping[prefix])
	sentence = string.capitalize(prefix[0]) + " " + prefix[1] + " " + suffix
	# this loop adds words.
	while suffix[-1] not in terminators:
		prefix = shift(prefix, suffix)
		suffix = random.choice(mapping[prefix])
		sentence += " " + suffix
	return sentence

def build_paragraph(dictionary, number):
	""" build_paragraph(dictionary, integer) -> string
	The function calls build_sentence() with the dictionary the number of times
	specified by integer. It joins the sentences and returns one string.
	"""
	sentences = [build_sentence(dictionary) for n in range(number)]
	paragraph = string.join(sentences)
	return paragraph


def build_tweet(dictionary):
	""" build_tweet(dictionary) -> string
	This function calls build_sentence() to add sentences for as long as the
	string is less than 140 characters.
	"""
	tweet = ""
	while True:
		new_tweet = build_sentence(dictionary)
		if len(new_tweet) > 140:
			continue
		elif len(new_tweet + tweet) > 140:
			break	
		else:
			if tweet == "":
				tweet += new_tweet
			else: 
				tweet += " " + new_tweet
	return tweet

def main():
	script, filename, output_style = sys.argv

	d = process_file(filename)
	if output_style == "paragraph":
		paragraph = build_paragraph(d, 10)
		print paragraph
	elif output_style == "tweet":
		tweet = build_tweet(d)
		print tweet
		#markovddbraz.tweet(tweet)
	else:
		print "Choose between paragraph and tweet"

if __name__ == "__main__":
	main()

