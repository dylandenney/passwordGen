# Password Generator

This Python script generates a secure password by randomizing the case of letters from words selected from a dictionary file. The generated password includes special characters and numbers to enhance security.

## Features

- Random case transformation of letters in words.
- Generation of a password that combines letters, special characters, and numbers.
- Customizable dictionary file for word selection.

## Prerequisites

Before you begin, ensure you have met the following requirements:
- Python 3.x installed on your system.
- `requirements.txt` file to install the necessary Python packages.

## Installation

1. Clone the repository or download the Python scripts to your local machine.
2. Install the required Python packages:

## Usage

To generate a password, run the `password_generator.py` script:


Make sure you have a dictionary file named `wordlist` in the same directory as the script. The script selects words from this file to create a password.

### Generating Your Own Word List with NLTK

Optionally, if you want to generate your own word list using the Natural Language Toolkit (NLTK), follow these steps:

1. Ensure NLTK is installed. It's included in the `requirements.txt`.
2. Run the `wordlist_generator.py` script:



This will download the NLTK word list corpus and print the first 10 words as a sample. You can modify the script to save your desired word list to a file.

## Contributing

Feel free to fork the repository and submit pull requests.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

