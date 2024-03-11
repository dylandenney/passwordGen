import random

def randomize_case(word):
    """
    This function takes a single word as input and returns a new string where each letter
    of the original word is randomly capitalized or lowercased.

    :param word: The word to be transformed.
    :return: A new string where each character of `word` might be either uppercase or lowercase, decided randomly.
    """
    return ''.join(random.choice([char.upper(), char.lower()]) for char in word)

def generate_password_from_file(dictionary_file):
    """
    Generates a secure password by combining randomly selected words from a given dictionary file,
    interspersing them with a random number and a special character.

    The process involves reading a list of words from a file, selecting three words at random,
    randomizing the case of these words, and then inserting a randomly chosen number and special character
    at random positions within the concatenated string of words.

    :param dictionary_file: The file path of the dictionary file containing possible words to use.
    :return: A secure password string that combines letters, numbers, and special characters.
    """
    # Define a string of special characters and numbers to choose from
    special_characters = "!@#$%^&*"
    numbers = "0123456789"

    # Open the dictionary file and read lines into a list, stripping whitespace
    with open(dictionary_file, 'r') as file:
        # Read each line from the file, remove leading/trailing whitespace, and ignore empty lines
        words = [line.strip() for line in file if line.strip()]

    # Randomly select three words from the list
    selected_words = random.sample(words, 3)
    # Apply random case transformation to each of the selected words
    selected_words = [randomize_case(word) for word in selected_words]

    # Combine the selected words into a single string, separated by spaces
    password = ' '.join(selected_words)

    # Randomly select one special character and one number
    special_char = random.choice(special_characters)
    number = random.choice(numbers)

    # Determine random positions within the password string to insert the special character and number
    # We add 2 to the range for positions because we are inserting two additional characters
    positions = random.sample(range(len(password) + 2), 2)  # +2 accounts for the insertion of two characters

    # Insert the special character and number into the password at the determined positions
    # We sort positions to ensure that the insertion happens from left to right, maintaining the correct indexes
    for pos, char in zip(sorted(positions), [special_char, number]):
        password = password[:pos] + char + password[pos:]

    return password

# Specify the path to your dictionary file
dictionary_file = 'wordlist'
# Generate a password using the specified dictionary file
password = generate_password_from_file(dictionary_file)
# Print the generated password
print(password)

