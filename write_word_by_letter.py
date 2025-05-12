import time
import sys

def write_word_by_letter(word, delay=0.3):
    """ writes a word to the console, letter by letter, with a delay."""
    for letter in word:
        sys.stdout.write(letter)
        sys.stdout.flush() # ensures the output is immediately displayed
        time.sleep(delay)
    print()

# if __name__ == "__main__":
#     word_to_write = "Just testing to write something here. Thanks for watching it!"
#     write_word_by_letter(word_to_write)

if __name__ == "__main__":
    word_to_write_slowly = "writing text slowly"
    write_word_by_letter(word_to_write_slowly)
