# Get text input from the user
text = input("Text: ")

# Split the text into words
words = text.split()

# Create an empty dictionary to count words
word_counts = {}

# Count occurrences
for word in words:
    word = word.lower()  # Normalize to lowercase
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

# Determine the length of the longest word for alignment
max_length = max(len(word) for word in word_counts)

# Print the results sorted by word
for word in sorted(word_counts):
    print(f"{word:{max_length}} : {word_counts[word]}")
