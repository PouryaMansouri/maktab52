import re

input_path = "./input-q-2.txt"
output_path = "./output-q-2-1.txt"


def file_reader(path2):
    with open(path2) as file:
        for row in file.readlines():
            yield row.strip()


with open(output_path, 'w') as f:
    for _ in file_reader(input_path):
        # TODO: remove all reference --> Done
        matcher_reference = re.compile(r"\[\d*\]")
        _ = matcher_reference.sub(' ', _)
        # TODO: split sentence --> Done
        matcher_line = re.compile(r"\.\s")
        lines = matcher_line.split(_)
        # TODO: write to file --> Done
        for line in lines:
            if line != '':
                f.write(line.strip() + '.\n')
