
def updateRecord(record, prov1, prov2):
    if prov2:
        if prov1 == prov2['prov']: #if they match just update
            record['updatedProv'] = prov1   #add updated province
            record['Check'] = ''
        else:
            if prov1 is None:
                record['updatedProv'] = prov2['prov']
                if record['LOCNOTES'].strip().lower() == prov2.match.lower():
                    record['Check'] = ''
                else: 
                    record['Check'] = 'y'
            else:
                record['updatedProv'] = prov1 + '|' + prov2['prov']
                record['Check'] = 'y'
           
    else: 
        if prov1: #if province from QDS only, record and mark to check
            record['updatedProv'] = prov1
            record['Check'] = 'y' 
        else: #I DON"T KNOW HOW TO TEST FOR THIS _ if province from town only, then if exact match use the province, else use the province and mark for check
            record['updatedProv'] = None
            record['Check'] = ''
        
    