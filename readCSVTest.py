from readCSV import readCSV

fileName = 'TransvaalRecords_withLocality.csv'

records = readCSV(fileName)

print('We got', len(records), 'records from', fileName)