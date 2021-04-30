# TODO: remove reference

NUMBER_DICT = {'one': 1, 'two': 2, 'three': 3, 'four': 4,
               'five': 5, 'six': 6, 'seven': 7, 'eight': 8,
               'nine': 9, 'ten': 10, 'eleven': 11, 'twelve': 12,
               'thirteen': 13, 'fourteen': 14, 'fifteen': 15, 'sixteen': 16,
               'seventeen': 17, 'eighteen': 18, 'nineteen': 19, 'twenty': 20}

input_path = "./input-q-1.txt"
output_path = "./output-q-1.txt"


def file_reader(path2):
    with open(path2) as file:
        for row in file.readlines():
            yield row.strip().split(' ')


# TODO: use lambda and map to remove second for
with open(output_path, 'w') as f:
    for line in file_reader(input_path):
        for _ in range(len(line)):
            if line[_].lower() in NUMBER_DICT.keys():
                line[_] = str(NUMBER_DICT[line[_]])
        f.write(' '.join(line) + '\n')
