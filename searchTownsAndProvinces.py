import re
from RegEx import *

locality = ["locality near Jacobsdal.", "Durban North", "koffiefontein", "Unknown"]


def searchProvinces ():
    for x in locality:
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
        result12 = re.search(regexNamibia, x, re.I)
        result13 = re.search(regexZimbabwe, x, re.I)
        result14 = re.search(regexBotswana, x, re.I)
        result15 = re.search(regexMozambique, x, re.I)
        result16 = re.search(regexAngola, x, re.I)
        result17 = re.search(regexZambia, x, re.I)
        result18 = re.search(regexMalawi, x, re.I)
        if result1 or result2:
            print("KwaZulu-Natal")
        elif result3:
            print("Eastern Cape")
        elif result4:
            print("Free State")
        elif result5:
            print("Gauteng")
        elif result6 == regexLimpopo:
            print("Limpopo")
        elif result7:
            print("Mpumalanga")
        elif result8:
            print("North West")
        elif result9 or result10:
            print("Nothern Cape")
        elif result11:
            print("Western Cape")
        elif result12:
            print("Namibia")
        elif result13:
            print("Zimbabwe")
        elif result14:
            print("Botswana")
        elif result15:
            print("Mozambique")
        elif result16:
            print("Angola")
        elif result17:
            print("Zambia")
        elif result18:
            print("Malawi")
        else:
            print("No match")

searchProvinces()