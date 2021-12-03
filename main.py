#import necessary functions
from readCSV import readCSV
from writecsvHs import writecsv
from searchTownsAndProvinces import searchProvinces
from updateRecord import updateRecord
from getQDSProvince import getQDSProvince

#import the records dataset
fileName = 'TransvaalRecords_withLocality.csv'
records = readCSV(fileName)

hasLocalityProvince = 0
hasQDSProvince = 0
provinceAdded = 0
mustCheck = 0

badQDSs = []

#loop each record
for record in records:
    # get the province using the locality string
    localityProvince = searchProvinces(record['LOCNOTES'])
    if localityProvince:
        hasLocalityProvince += 1
    # get the province using the QDS
    qdsProvince = None

    try:
        qdsProvince = getQDSProvince(record['QDS'])
    except(Exception):
        badQDSs.append(record['BRAHMS'])

    if qdsProvince:
        hasQDSProvince += 1

    #update the record based on locality province and QDS province
    updateRecord(record, qdsProvince, localityProvince)
    if record['updatedProv']:
        provinceAdded += 1
    
    if record['Check'] == 'y':
        mustCheck += 1

print('Provinces found for', hasLocalityProvince, 'records using locality')
print('Provinces found for', hasQDSProvince, 'records using QDS')
print('New province added for', provinceAdded, 'records')
print(mustCheck, 'records must be checked')

if len(badQDSs) > 0:
    print('We have bad QDSs in the following records:')
    print('|'.join(badQDSs))

#write the results
writecsv(records, 'Transvaal_updates.csv')
print('Results saved')