#The highlight_word function changes the given word in a sentence to its upper-case version.
#For example, highlight_word("Have a nice day", "nice") returns "Have a NICE day". Can you write this function in just one line?

def highlight_word(sentence, word):
	new_sentence = ""
	length = len(word)
	words = sentence.split()
	for n, w in enumerate(words):
		if w[:length] == word:
			new_sentence += w[:length].upper() + w[length:]
		else:
			new_sentence += w
		if n != len(words)-1:
			new_sentence += " "
	return new_sentence

print(highlight_word("Have a nice day", "nice"))
print(highlight_word("Shhh, don't be so loud!", "loud"))
print(highlight_word("Automating with Python is fun", "fun"))
