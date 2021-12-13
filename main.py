#import necessary functions
from readCSV import readCSV
from writecsvHs import writecsv
from searchTownsAndProvinces import searchProvinces
from getQDSProvince import getQDSProvince
from updateRecord import updateRecord


#import the records dataset
fileName = 'TransvaalRecords_withLocality.csv'
records = readCSV(fileName)

hasLocalityProvince = 0 #got a province from Sarena's function
hasQDSProvince = 0 #got a province from Mahlatse's function
provinceAdded = 0 #total number of records where the province is updated
mustCheck = 0 # the number of records that need to be checked

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