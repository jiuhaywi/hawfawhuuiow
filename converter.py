import os

# File names
file_normal = "Normal.txt"
file_alex = "Alex.txt"

# Check if files exist
if not os.path.exists(file_normal) or not os.path.exists(file_alex):
    print(f"Error: One or both files ({file_normal}, {file_alex}) are missing.")

# Menu for translation direction
print("Select an option:")
print("1: Translate Normal to Alex")
print("2: Translate Alex to Normal")
print("3: Translate a sentence from Normal to Alex")
print("4: Translate a sentence from Alex to Normal")
choice = input("Enter 1, 2, 3, or 4: ")

if choice not in ["1", "2", "3", "4"]:
    print("Invalid choice. Please enter 1, 2, 3, or 4.")

def translate_word():

    # Get the word to translate
    word_to_translate = input("Enter the word to translate: ").strip()

    # Open and read files
    with open(file_normal, "r", encoding="utf-8") as norm_file:
        normal_words = norm_file.readlines()

    with open(file_alex, "r", encoding="utf-8") as alex_file:
        alex_words = alex_file.readlines()

    # Ensure the two files have the same number of lines
    if len(normal_words) != len(alex_words):
        print("Error: The files do not have the same number of lines.")
        return

    # Perform translation
    try:
        if choice == "1":
            # Normal to Alex
            index = normal_words.index(word_to_translate + "\n")
            print(f"The Alex translation is: {alex_words[index].strip()}")

        elif choice == "2":
            # Alex to Normal
            index = alex_words.index(word_to_translate + "\n")
            print(f"The Normal translation is: {normal_words[index].strip()}")

    except ValueError:
        print("Word not found in the selected file.")

def translate_sentence():

    # Get the sentence to translate
    sentence_to_translate = input("Enter the sentence to translate: ").strip()

    # Open and read files
    with open(file_normal, "r", encoding="utf-8") as norm_file:
        normal_words = [line.strip() for line in norm_file.readlines()]

    with open(file_alex, "r", encoding="utf-8") as alex_file:
        alex_words = [line.strip() for line in alex_file.readlines()]

    # Ensure the two files have the same number of lines
    if len(normal_words) != len(alex_words):
        print("Error: The files do not have the same number of lines.")
        return

    # Translate sentence word by word
    translated_words = []
    words = sentence_to_translate.split()

    if choice == "3":
        # Normal to Alex
        for word in words:
            if word in normal_words:
                index = normal_words.index(word)
                translated_words.append(alex_words[index])
            else:
                translated_words.append(word)  # Leave untranslated

    elif choice == "4":
        # Alex to Normal
        for word in words:
            if word in alex_words:
                index = alex_words.index(word)
                translated_words.append(normal_words[index])
            else:
                translated_words.append(word)  # Leave untranslated

    # Output the translated sentence
    print("Translated sentence:", " ".join(translated_words))

while True:
    if choice in ["1", "2"]:
        translate_word()
    elif choice in ["3", "4"]:
        translate_sentence()
