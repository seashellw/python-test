"""
装水的那个
"""

import re

input_list = input("Please input the list: ").split(" ")
input_list = [re.sub(r'\s', "", item) for item in input_list]
input_list = list(filter(lambda x: x, input_list))
input_list = [int(item) - 1 for item in input_list]

water_number = 0

start_index = 0
end_index = len(input_list) - 1

for layer in range(max(input_list)):
    layer_flags = [(item >= layer) for item in input_list]
    while not layer_flags[start_index]:
        start_index += 1
    while not layer_flags[end_index]:
        end_index -= 1
    if start_index >= end_index:
        break
    for item in layer_flags[start_index:end_index + 1]:
        if not item:
            water_number += 1

print(water_number)
