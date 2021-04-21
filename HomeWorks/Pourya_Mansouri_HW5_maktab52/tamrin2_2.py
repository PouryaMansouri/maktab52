import re

input_path = "./input-q-2.txt"
output_path = "./output-q-2-2.txt"

with open(input_path) as input_file:
    file = input_file.read()
    # TODO: Find all numbers --> Done
    matcher_digit = re.compile(r"\d*\d")
    numbers = matcher_digit.findall(file)
    # TODO: remove all reference --> Done
    matcher_reference = re.compile(r"\[\d*\]")
    without_reference = matcher_reference.sub(' ', file)
    # TODO: remove all dots in file --> Done
    matcher_dot = re.compile("\.")
    without_dot = matcher_dot.sub('', without_reference)
    # TODO: remove all numbers in file --> Done
    without_digit = matcher_digit.sub('', without_dot)
    words = without_digit.split()

# TODO: 1980s is a word or numbers?
all_words_dict = dict()
for _ in words:
    all_words_dict[_] = all_words_dict.get(_, 0) + 1
# TODO: fine unique words --> Done
unique_words = [_ for _ in all_words_dict.keys() if all_words_dict[_] == 1]

with open(output_path, 'w') as out_file:
    out_file.write("all word with count:\n")
    out_file.write(str(all_words_dict) + "\n\n")
    out_file.write("Unique words in file:\n")
    out_file.write(str(unique_words) + "\n\n")
    out_file.write("All numbers:\n")
    out_file.write(str(numbers) + "\n\n")
    out_file.write(f"There are {unique_words=} and {numbers=} in this file")

output_path = "./output-q-2-3.txt"
capital_words = [_ for _ in words if _[0].isupper()]
with open(output_path, 'w') as out_file:
    out_file.write(', '.join(capital_words))
