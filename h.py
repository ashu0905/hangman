import h_header_files
words = []
word = ""
word_length = int
i = int
vowels = []
displayed_word = ""
attempts = int
guesses = int
j = int
k = int
l = int
letter = chr
a = int
vowels.append('a')
vowels.append('e')
vowels.append('i')
vowels.append('o')
vowels.append('u')
words.append("shot")
words.append("penalty")
words.append("match")
words.append("header")
words.append("formation")
words.append("coach")
words.append("supporter")
words.append("pass")
words.append("football")
words.append("manager")
word = h_header_files.random.choice(words)
word_length = len(word)
i = 0
attempts = 3
guesses = 3
while i < word_length:
    if word[i] in vowels:
        displayed_word = displayed_word + str.upper(word[i])
        i += 1
    else:
        displayed_word = displayed_word + "_"
        i += 1
print(displayed_word)
print("Guess the word using consonants (y) You can guess each letter thrice & have 3 attempts for guessing the word in total.")
j = 0
k = attempts
l = guesses
while k > 0:
    while j < word_length:
        if displayed_word[j] == '_':
            while l > 0:
                letter = input("Guess the " + str(j+1) + "th letter: ")
                if len(letter) > 1:
                    print("You can enter only 1 character at a time...")
                    continue
                else:
                    letter = input("Type the " + str(j+1) + "th letter again: ")
                if letter in word and word[j] == letter:
                    displayed_word = displayed_word[:j] + str.upper(letter) + displayed_word[j+1:]
                    print("displayed_word =   ", displayed_word)
                    a = j+1
                    while a < word_length:
                        if word[a] == letter:
                            displayed_word = displayed_word[:a] + str.upper(letter) + displayed_word[a + 1:]
                            a += 1
                        else:
                            a += 1
                else:
                    l -= 1
                    if l > 0:
                        print("You guessed the letter wrong...You have {} chances left to guess the letter...".format(l))
                        continue
                letter = ''
                break
            j += 1
            continue
        else:
            j += 1
            l = guesses
    if "_" in displayed_word:
        k -= 1
        if k == 0 and "_" in displayed_word:
            print("You failed to guess the word :-( See you later...")
            break
        j = 0
        l = guesses
        continue
    else:
        print("You guessed the word right !!! The word is " + displayed_word + " :-)")
        break
