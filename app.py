"""
装水的那个
"""

input_list = ["3", "1", "2", "5", "2", "4"]

input_list = [int(item) - 1 for item in input_list]

print(input_list)

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
