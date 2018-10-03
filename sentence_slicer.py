"""
BASIC
sentence = input("Give me a sentence! ")

sentence_length = len(sentence)
sentence_start = sentence_length * 0.25
sentence_end = sentence_length * 0.75
sentence_start = round(sentence_start)
sentence_end = round(sentence_end)

print(sentence[sentence_start:sentence_end])
"""

#ADVANCED

sentence = input("Give me a sentence! ")


sentence_split = sentence.split()
sentence_length = len(sentence_split)


sentence_start = sentence_length * 0.25
sentence_end = sentence_length * 0.75
sentence_start = round(sentence_start)
sentence_end = round(sentence_end)

complete_sentence = " ".join(sentence_split[sentence_start:sentence_end])

print(complete_sentence)
