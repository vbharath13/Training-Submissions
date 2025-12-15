# Word Frequency Analyzer using Dictionary and Set Operations

def word_frequency_analyzer(text):
    # Convert text to lowercase and split into words
    words = text.lower().split()

    # Remove punctuation (basic way)
    clean_words = [word.strip(".,!?;:") for word in words]

    # Use a dictionary to count word frequencies
    word_count = {}

    for word in clean_words:
        if word in word_count:
            word_count[word] += 1  # Increment count if word already exists
        else:
            word_count[word] = 1   # Create new key-value pair

    # Use a set to show unique words
    unique_words = set(clean_words)

    # Display results
    print("\n Word Frequency Analysis:")
    for word, count in word_count.items():
        print(f"{word}: {count}")

    print(f"\n Total unique words: {len(unique_words)}")
    print("Unique words:", unique_words)


# Main program
if __name__ == "__main__":
    text_input = input("Enter a sentence or paragraph: ")
    word_frequency_analyzer(text_input)
