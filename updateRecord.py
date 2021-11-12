




def updateRecords(records, prov1, prov2):
    # for record in records:
        if len(record.QDS) <=6:
            check = 'y'
        else:
            if prov1 == prov2:
                updateProv = prov1
                # OR? record.MAJORAREA = prov1
            else:
                updateProv = prov1 + ', ' + prov2
                # OR? record.MAJORAREA = prov1 + ', ' + prov2
                check = 'y'
    return updateProv
    #return record

