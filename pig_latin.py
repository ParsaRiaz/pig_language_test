def to_pig_latin(sentence):
    vowels = "aeiou"
    words = sentence.split()
    pig_latin_words = []

    for word in words:
        if word[0] in vowels:
            pig_word = word + "way"
        else:
            pig_word = word[1:] + word[0] + "ay"
        pig_latin_words.append(pig_word)

    return " ".join(pig_latin_words)

# Get input from the user
sentence = input("Enter a sentence to convert to Pig Latin: ")
pig_latin_sentence = to_pig_latin(sentence)
print("Pig Latin: ", pig_latin_sentence)
