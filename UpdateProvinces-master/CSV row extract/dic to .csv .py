
import csv
a_file = open("sample0.csv", "w")
a_dict = {"Change0": 1, "b": 2}

writer = csv.writer(a_file)
for key, value in a_dict.items():
    writer.writerow([key, value])

a_file.close()