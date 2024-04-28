import unicode.cnv as cnv

# Sample string containing multiple letters
letters_string = "अआइईउऊ"

# Empty string to store individual letters
a = ""

# Splitting the string into individual letters
for letter in letters_string:
    a = cnv.convert_data_to_unicode(letter) + " " + a

print("Individual letters:", a)

six_letter_words = []

# Splitting the string into individual letters
individual_letters = a.split()

# Concatenating the letters into groups of six, trimming spaces
group_of_six = ""
for letter in individual_letters:
    if letter != '':  # Ignore empty strings
        group_of_six += letter
        if len(group_of_six) == 6:
            six_letter_words.append(group_of_six)
            group_of_six = ""

# Print the six-letter words
print("Six-letter words:", six_letter_words)

# Empty string to store concatenated six-letter words
b = ""

# Reverting the Unicode to letters
for word in six_letter_words:
    b = b+cnv.convert_data_to_letter(word)

print("Concatenated six-letter words:", b)
print(letters_string)