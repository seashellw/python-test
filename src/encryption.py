"""
加密的那个
"""

# import re

# input_str = re.sub(r'\s', "", input("Please input the string: "))

secret_key = "feather"

plaintext = "c language is wonderful."

alphabet_set = list("abcdefghijklmnopqrstuvwxyz")

secret_key_list = list(secret_key)

new_list = []

for key in secret_key_list:
    if key not in new_list:
        new_list.append(key)

secret_key_list = new_list

for key in alphabet_set[::-1]:
    if key not in secret_key_list:
        secret_key_list.append(key)

key_map = {}

for index, item in enumerate(alphabet_set):
    key = secret_key_list[index]
    if not key_map.get(item):
        key_map[item] = key

ciphertext_list = list(plaintext)
for index, key in enumerate(ciphertext_list):
    if key in key_map:
        ciphertext_list[index] = key_map[key]

ciphertext = "".join(ciphertext_list)
print(ciphertext)