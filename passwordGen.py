import random

def randomize_case(word):
    """Randomly capitalize letters in a word."""
    return ''.join(random.choice([char.upper(), char.lower()]) for char in word)

def generate_password_from_file(dictionary_file):
    special_characters = "!@#$%^&*"
    numbers = "0123456789"

    # Load words from a file
    with open(dictionary_file, 'r') as file:
        words = [line.strip() for line in file if line.strip()]

    # Randomly select three words and randomize their case
    selected_words = random.sample(words, 3)
    selected_words = [randomize_case(word) for word in selected_words]

    # Combine words with spaces
    password = ' '.join(selected_words)

    # Randomly select one special character and one number and determine their positions
    special_char = random.choice(special_characters)
    number = random.choice(numbers)

    # Insert the special character and number at random positions in the password
    positions = random.sample(range(len(password) + 2), 2)  # +2 because we're adding two characters
    for pos, char in zip(sorted(positions), [special_char, number]):
        password = password[:pos] + char + password[pos:]

    return password

# Specify the path to your dictionary file
dictionary_file = 'wordlist'
password = generate_password_from_file(dictionary_file)
print(password)

