wrong_words = ["stupid", "hard", "annoying", "impossible", "wrong"]

corrected_words = ["fun", "easy", "enjoyable", "possible", "right"]

sentence = input("Write a sentence:")
sentence = sentence.split()

index = 0
for word in sentence:
	if word in wrong_words:
		corrected_words_index = wrong_words.index(word)
		print(corrected_words_index)
		sentence[index] = corrected_words[corrected_words_index]
	index = index + 1	

sentence = " ".join(sentence)

print(sentence)		