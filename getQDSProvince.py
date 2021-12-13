from readCSV import readCSV

# read the QDSprovinces CSV file
fileName = 'QDSProvinces.csv'
QDSProvinces = readCSV(fileName)

# tranform to dictionary for fast lookup
# we want a dictionary that looks like this

indexExample = {
  "2345CC": "Limpopo",
  "2244DC": "Western Cape"
}

qdsIndex = {}

for QDSProv in QDSProvinces:
  indexKey = QDSProv['COD']
  if indexKey in qdsIndex:
    qdsIndex[indexKey].append(QDSProv['PROVINCE'])
  else:
    prov = QDSProv['PROVINCE']
    qdsIndex[indexKey] = [prov]

#the index now looks like this
demo = { 
  "2454CC": ["Gauteng"],
  "3425CC": ["Limpopo"]
}

for key in qdsIndex:
  list = qdsIndex[key]
  if len(list) > 1:
    qdsIndex[key] = None
  else:
    qdsIndex[key] = list[0]
    

#now the index looks like thos
demo = { 
  "2454CC": "GP",
  "3425CC": "LP",
  "5425DD": None
}

provinceAbbreviations = {
  'NC': 'Northern Cape',
  'WC': 'Western Cape',
  'EC': 'Eastern Cape',
  'KZN': 'KwaZulu-Natal',
  'FS': 'Free State',
  'NW': 'North West',
  'LP': 'Limpopo',
  'MP': 'Mpumalanga',
  'GP': 'Gauteng'
}


#function for looking up provinced using QDSs

def getQDSProvince(qds):
  if qds and len(qds) == 6:
    provAbbrev = qdsIndex[qds]
    if provAbbrev in provinceAbbreviations: 
      return provinceAbbreviations[provAbbrev]
    else:
      return None
  else:
    return None


