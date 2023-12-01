import re

with open('number.txt', 'w') as number_file:
    number_file.write('')

with open('name.txt', 'w') as name_file:
    name_file.write('')

print("Insert Mods (press Enter without typing anything to finish):")

all_numbers = []
all_formatted_names = []

while True:
    paragraph = input()

    if not paragraph:
        break

    numbers = re.findall(r'id=(\d+)', paragraph)
    all_numbers.extend(numbers)

    names = re.findall(r'^(\S+(?:\s+\S+)*)(?:\s+Steam\s+https)', paragraph, re.MULTILINE)
    all_formatted_names.extend(names)

with open('number.txt', 'w') as number_file:
    number_file.write(','.join(all_numbers))
    number_file.write('\n')

with open('name.txt', 'w') as name_file:
    formatted_names_list = ['@{};'.format(name) for name in all_formatted_names]
    name_file.write('\n'.join(formatted_names_list))
    name_file.write('\n\n')
    name_file.write(''.join(formatted_names_list))
    name_file.write('\n')
