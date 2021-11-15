
def updateRecord(record, prov1, prov2):
    if prov1 == prov2: #if they match just update
            record['updatedProv'] = prov1   #add updated province
            record['Check'] = ''
           
    elif prov1 or prov2 is None:
        if prov2 is None: #if province from QDS only, record and mark to check
            record['updatedProv'] = prov1
            record['Check'] = 'y' 
        else: #I DON"T KNOW HOW TO TEST FOR THIS _ if province from town only, then if exact match use the province, else use the province and mark for check
            record['updatedProv'] = prov2
            record['Check'] = 'y'
        
    else: #if they don't match, record both and mark to check
        updateProv['updatedProv'] = prov1 + '|' + prov2
        record['Check'] = 'y'
        
    return updatedProv
    #return record
