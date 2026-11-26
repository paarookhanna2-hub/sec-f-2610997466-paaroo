# Lab 12 - Document Analysis System

# print("========================================")
# print("       DOCUMENT ANALYSIS SYSTEM")
# print("========================================")

# sentence = input("Enter a sentence: ")

# words = sentence.split()
# total_words = len(words)
# total_characters = len(sentence)

# vowels = 0
# consonants = 0
# digits = 0
# spaces = 0
# special_characters = 0

# for ch in sentence:

#     if ch.lower() in "aeiou":
#         vowels = vowels + 1

#     elif ch.isalpha():
#         consonants = consonants + 1

#     elif ch.isdigit():
#         digits = digits + 1

#     elif ch == " ":
#         spaces = spaces + 1

#     else:
#         special_characters = special_characters + 1

# total_letters = vowels + consonants

# if total_letters > 0:
#     vowel_percentage = (vowels / total_letters) * 100
# else:
#     vowel_percentage = 0

# print("========================================")
# print("        DOCUMENT ANALYSIS REPORT")
# print("========================================")

# print("Sentence:", sentence)
# print("Total characters:", total_characters)

# print("--- Character Breakdown ---")

# print("Words:", total_words)
# print("Vowels:", vowels)
# print("Consonants:", consonants)
# print("Digits:", digits)
# print("Spaces:", spaces)
# print("Special characters:", special_characters)

# print("--- Summary ---")

# print("Total letters:", total_letters)
# print("Vowel percentage:", round(vowel_percentage, 1), "%")

# print("========================================")
# print("Analysis Complete!")
# print("========================================")