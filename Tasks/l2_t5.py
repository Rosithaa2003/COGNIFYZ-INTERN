def count_words_in_file(filename):
    word_count = {}

    try:
        with open(filename, 'r') as file:
            # Read the file line by line
            for line in file:
                # Split each line into words
                words = line.strip().split()

                # Count the occurrences of each word
                for word in words:
                    # Remove punctuation and convert to lowercase
                    cleaned_word = word.strip('.,!?').lower()

                    if cleaned_word:
                        # Update the word count dictionary
                        word_count[cleaned_word] = word_count.get(cleaned_word, 0) + 1

    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return

    # Sort the word count dictionary by keys (words)
    sorted_word_count = sorted(word_count.items(), key=lambda x: x[0])

    # Display the results
    for word, count in sorted_word_count:
        print(f"{word}: {count}")

# Prompt the user for the filename
filename = input("Enter the filename: ")

# Call the function to count words in the file
count_words_in_file(filename)
