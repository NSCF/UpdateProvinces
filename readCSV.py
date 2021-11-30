import csv

def readCSV(fileName):
  records = []
  with open(fileName, newline='') as csvfile:
      reader = csv.DictReader(csvfile)
      for row in reader:
          records.append(row)
  return records