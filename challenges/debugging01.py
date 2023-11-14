# Intended output:
#
# > say_hello("kay")
# => "hello kay"
def say_hello(name):
    return f"hello {name}"


def encode(text, key):
    cipher = make_cipher(key)
    ciphertext_chars = []
    for i in text:
        # Add check to see if 'i' exists in the cipher list
        # pass if it does not exist
        if i in cipher:
            ciphered_char = chr(65 + cipher.index(i))
            ciphertext_chars.append(ciphered_char)
        else:
            pass

    return "".join(ciphertext_chars)


def decode(encrypted, key):
    cipher = make_cipher(key)

    plaintext_chars = []
    for i in encrypted:
        plain_char = cipher[65 - ord(i)]
        plaintext_chars.append(plain_char)

    return "".join(plaintext_chars)


def make_cipher(key):
    alphabet = [chr(i + 98) for i in range(1, 26)]
    cipher_with_duplicates = list(key) + alphabet

    cipher = []
    for i in range(0, len(cipher_with_duplicates)):
        if cipher_with_duplicates[i] not in cipher_with_duplicates[:i]:
            cipher.append(cipher_with_duplicates[i])

    return cipher


# When you run this file, these next lines will show you the expected
# and actual outputs of the functions above.
# print(
#     f"""
#  Running: encode("theswiftfoxjumpedoverthelazydog", "secretkey")
# Expected: EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL
#   Actual: {encode('theswiftfoxjumpedoverthelazydog', 'secretkey')}
# """
# )

# print(
#     f"""
#  Running: decode("EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL", "secretkey")
# Expected: theswiftfoxjumpedoverthelazydog
#   Actual: {decode('EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL', 'secretkey')}
# """
# )


## ====== Challenge ====== ##


def get_most_common_letter(text):
    counter = {}
    for char in text:
        if char.isalpha():  # Only count alphabetic characters
            counter[char] = counter.get(char, 0) + 1
    letter = sorted(counter.items(), key=lambda item: item[1], reverse=True)[0][0]
    return letter


print(
    f"""
Running:  get_most_common_letter("the roof, the roof, the roof is on fire!"))
Expected: 'o'
Actual:   {get_most_common_letter("the roof, the roof, the roof is on fire!")}
"""
)
