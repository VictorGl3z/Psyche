# Problem Statement
# Write a function that stutters a word as if someone is struggling to read it.
# The first two letters are repeated twice with an ellipsis (...) and space after each,
# and then the word is pronounced with a question (?)
# Examples
# stutter("incredible") -> "in... in... incredible?"
# stutter("outstanding") -> "ou... ou... outstanding?"

def stutter(word):
    return '{0}... {0}... {1}?'.format(word[:2], word)
    
while True:
    word = input('Input your word: ')
    if len(word) > 2 and word.isalpha():
        break
    elif len(word) <= 2:
        print('Word is not long enough!')
        continue
    else:
        print('Unrecognized letters!')
        continue

print(stutter(word))