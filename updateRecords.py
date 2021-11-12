




def updateRecords(infile, prov1, prov2):
    for record in records:
        if prov1 == prov2:
            updateProv = prov1
            check = ' '
        else:
            updateProv = prov1 + ', ' + prov2
            check = 'y'
    return updateProv

updateRecords('test.csv','NC', 'NC')
print(updateRecords)