from sys import argv, exit
import csv


def main():

    if len(argv) != 3:
        print("Usage: dna.py [STR Counts.csv] [DNA Sequence.txt]...")
        exit(1)

    sequence = open(f"{argv[2]}", 'r')
    s = sequence.read()

    # create dictionary to store values from
    str_count = {
        "AGATC": count(s, 'AGATC',),
        "TTTTTTCT": count(s, 'TTTTTTCT'),
        "AATG": count(s, 'AATG'),
        "TCTAG":  count(s, 'TCTAG'),
        "GATA": count(s, 'GATA'),
        "TATC": count(s, 'TATC'),
        "GAAA": count(s, 'GAAA'),
        "TCTG": count(s, 'TCTG'),
    }

    filename = argv[1]
    dna_reader_1 = csv.DictReader(open(f"{filename}"))
    for row in dna_reader_1:
        test = len(row)
        break

    found = False

    dna_reader_2 = csv.DictReader(open(f"{filename}"))

    if test == 4:
        for row in dna_reader_2:
            if int(row["AGATC"]) == str_count["AGATC"] and int(row["AATG"]) == str_count["AATG"] and int(row["TATC"]) == str_count["TATC"]:
                print(row["name"])
                found = True
    elif test == 9:
        for row in dna_reader_2:
            if (int(row["AGATC"]) == str_count["AGATC"] and int(row["AATG"]) == str_count["AATG"] and int(row["TATC"]) == str_count["TATC"]
                and int(row["TTTTTTCT"]) == str_count["TTTTTTCT"] and int(row["TCTAG"]) == str_count["TCTAG"]
                    and int(row["GATA"]) == str_count["GATA"] and int(row["GAAA"]) == str_count["GAAA"] and int(row["TCTG"]) == str_count["TCTG"]):
                print(row["name"])
                found = True

    if found != True:
        print("No match")


def count(s, seq):

    length = len(s)

    record = 0
    while length > 0:
        index = 0
        count = 0
        while True:
            test = s[index:(index+len(seq))]
            if s[index:(index+len(seq))] == seq:
                count += 1
                index += len(seq)
            else:
                if count > record:
                    record = count
                break
        s = s[1:]
        length -= 1
    return record


main()