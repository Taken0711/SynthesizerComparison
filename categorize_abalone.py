import csv


def classify(c):
    if c <= 8:
        return "1-8"
    if c == 9:
        return "9"
    if c == 10:
        return "10"
    return "11+"


with open("abalone.data", "r", newline='') as in_file, open("categorized_abalone.data", "w", newline='') as out_file:
    abalone_reader = csv.reader(in_file)
    abalone_writer = csv.writer(out_file)

    # Write header
    abalone_writer.writerow(next(abalone_reader))

    for e in abalone_reader:
        abalone_writer.writerow(e[:-1] + [classify(int(e[-1]))])

