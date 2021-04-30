def read_log(file, level):
    count = 0
    with open(file) as f:
        for row in f.readlines():
            if level in row:
                count += 1

    return f"in {file=} you have {count} log with {level=}"


file1_path = "./sample.log"
file2_path = "./person.log"

print(read_log(file1_path, "INFO"))
print(read_log(file2_path, "WARNING"))
