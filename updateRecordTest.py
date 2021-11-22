from updateRecord import updateRecord


records = [{'BRAHMS': '821', 'prov1': 'Northern Cape', 'prov2':'Northern Cape'}, {'BRAHMS': '814', 'prov1': None, 'prov2':'Northern Cape'}, {'BRAHMS': '814', 'prov1': 'Northern Cape', 'prov2': None}, {'BRAHMS': '821', 'prov1': 'Northern Cape', 'prov2':'Western Cape'}]


for record in records:
    updateRecord(record, record['prov1'], record['prov2'])
    print(record['updatedProv'] + ', ' + record['Check'])
