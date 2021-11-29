#write new csv file
import csv

def writecsv(list_dict, outFile):
    with open(outFile, 'w', newline = '') as csvfile:
        fieldnames = list(list_dict[0].keys())
        writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
        writer.writeheader()
        for the_dict in list_dict:
            writer.writerow(the_dict)  

  




