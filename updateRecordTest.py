from updateRecord import updateRecord


# records = [{'BRAHMS': '821', 'LOCNOTES': 'Pietersburg', 'QDS':'2228'}, {'BRAHMS': '814', 'LOCNOTES': '5 mile N of Pietersburg', 'QDS':'2528CC'}, {'BRAHMS': '814', 'LOCNOTES': 'Tzaneen', 'QDS': '3018DC'}, {'BRAHMS': '821', 'LOCNOTES': 'Near Tzaneen', 'QDS':'3119AA'}]
# prov1 = [{'prov':''}, {'prov':'Limpopo'}, {'prov':'Western Cape'}, {'prov':'Western Cape'}]
# prov2 = [{'prov':'Limpopo'}, {'prov': 'Limpopo'}, {'prov': 'Western Cape'}, {'prov':''}]

record = {'BRAHMS': '821', 'LOCNOTES': 'N of Pietersburg', 'QDS':'2228'}

# updateRecord(record, 'Limpopo', {'prov':'Limpopo', 'match': 'Pietersburg'})
updateRecord(record, 'Mpumalanga', {'prov':'Limpopo', 'match': 'Pietersburg'})
# updateRecord(record, None, {'prov':'Limpopo', 'match': 'Pietersburg'})
# updateRecord(record, 'Limpopo', None)
print(record['updatedProv'] + ', ' + record['Check'])

# for record in records:
#     x = 0
#     updateRecord(record, prov1[0], prov2[0])
#     print(record['updatedProv'] + ', ' + record['Check'])
#     x +=1
