# find a word from a paragraph

def find_word_in_paragraph(paragraph, word_to_find):
    words = paragraph.split()
    return word_to_find in words

my_paragraph = "A little mouse named Mimi lived in a big, green field."
word = "Mimi"

if find_word_in_paragraph(my_paragraph, word):
    print(f"The word '{word}' was found in the paragraph.")
else:
    print(f"The word '{word}' was NOT found in the paragraph.")

word2 = "green"

if find_word_in_paragraph(my_paragraph, word2):
    print(f"The word '{word2}' was found in the paragraph.")
else:
    print(f"The word '{word2}' was NOT found in the paragraph.")
