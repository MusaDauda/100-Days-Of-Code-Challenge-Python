vowel = 0
consonants = 0
for letter in "supercalifragilisticexpialidocious":
    if letter.lower() in "aeiou":
        vowel += 1
    elif letter.lower() in " ":
        pass
    else:
        consonants += 1

print(f"There are {vowel} vowels and {consonants} consonants")