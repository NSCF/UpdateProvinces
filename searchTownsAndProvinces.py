import re
from RegEx import *

def searchProvinces (locality):

    x = locality #because I'm lazy
    
    result1 = re.search(regexKZN1, x, re.I)
    result2 = re.search(regexKZN2, x, re.I)
    result3 = re.search(regexEasternCape, x, re.I)
    result4 = re.search(regexFreeState, x, re.I)
    result5 = re.search(regexGauteng, x, re.I)
    result6 = re.search(regexLimpopo, x, re.I)
    result7 = re.search(regexMpumalanga, x, re.I)
    result8 = re.search(regexNorthWest, x, re.I)
    result9 = re.search(regexNorthernCape1, x, re.I)
    result10 = re.search(regexNorthernCape2, x, re.I)
    result11 = re.search(regexWesternCape, x, re.I)
    
    if result1 or result2:
        group = None
        if result1:
            group = result1.group()
        else:
            group = result2.group()
        return {"prov":"KwaZulu-Natal","match": group}
    elif result7:
        return {"prov":"Mpumalanga", "match":result7.group()}
    elif result3:
        return {"prov":"Eastern Cape","match":result3.group()}
    elif result4:
        return {"prov":"Free State", "match":result4.group()}
    elif result5:
        return {"prov":"Gauteng", "match":result5.group()}
    elif result6:
        return {"prov":"Limpopo", "match":result6.group()}
    elif result8:
        return {"prov":"North West", "match":result8.group()}
    elif result9 or result10:
        group = None
        if result9:
            group = result9.group()
        else:
            group = result10.group()
        return {"prov":"Northern Cape", "match": group}
    elif result11:
        return {"prov":"Western Cape", "match":result11.group()}
    else:
        return None

