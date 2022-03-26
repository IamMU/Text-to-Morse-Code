# The Morse Code Tables
text_to_morse = {
    'a': '·−',
    'b': '−···',
    'c': '−·−·',
    'd': '−··',
    'e': '·',
    'f': '··−·',
    'g': '−−·',
    'h': '····',
    'i': '··',
    'j': '·−−−',
    'k': '−·−',
    'l': '·−··',
    'm': '−−',
    'n': '−·',
    'o': '−−−',
    'p': '·−−·',
    'q': '−−·−',
    'r': '·−·',
    's': '···',
    't': '−',
    'u': '··−',
    'v': '···−',
    'w': '·−−',
    'x': '−··−',
    'y': '−·−−',
    'z': '−−··',
    '0': '−−−−−',
    '1': '·−−−−',
    '2': '··−−−',
    '3': '···−−',
    '4': '····−',
    '5': '·····',
    '6': '−····',
    '7': '−−···',
    '8': '−−−··',
    '9': '−−−−·',
    ' ': '/'
}
# Reverse Mapping the Table to make another one for decrypting
morse_to_text = {v: k for k, v in text_to_morse.items()}

# FUNCTIONS


def encrypt(text_to_encrypt):
    result = ""

    # Looping through each character in the given text and replacing it with the
    # corresponding value
    for char in text_to_encrypt.lower():
        morse_char = text_to_morse[char]

        # Adding a space after each character to make the Morse Code more readable
        result += morse_char + "  "

    return result


def decrypt(text_to_decrypt):
    result = ""

    # Splitting the Morse Code into different indexes in a list
    text = text_to_decrypt.split("  ")

    for char in text:
        if char == "/":
            # Adding a space if there is a "/" in the code(My made "space")
            result += " "
        else:
            # Replacing the code with the alphabets
            result += morse_to_text[char]

    return result


# END-USER

# Dummy input to make the while loop work
user_input = ""

# While loop to allow the user to encrypt/decrypt multiple times in a single run
while not user_input.lower() == "quit":
    user_input = input("Encrypt/Decrypt/Quit:   ")

    if user_input.lower() == "encrypt":
        text = input("Enter text to encrypt:    ")

        print(f"Encrypted Text: {encrypt(text)}")
    elif user_input.lower() == "decrypt":
        text = input("Enter text to decrypt:    ")

        print(f"Encrypted Text: {decrypt(text)}")
    else:
        print(f'Error: {user_input} not accepted!\nPlease try again.')

