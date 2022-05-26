"""
加密的那个
"""

import re

secret_key = re.sub(r'\s', "", input("Please input the secret_key: "))

plain_text = re.sub(r'[\r\n]', "", input("Please input the plain_text: "))

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

cipher_text_list = list(plain_text)
for index, key in enumerate(cipher_text_list):
    if key in key_map:
        cipher_text_list[index] = key_map[key]

cipher_text = "".join(cipher_text_list)

print(cipher_text)