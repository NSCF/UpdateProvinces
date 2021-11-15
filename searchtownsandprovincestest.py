from searchTownsAndProvinces import *

locality = ["locality near Jacobsdal.", "Durban North", "koffiefontein", "Unknown"]
for x in locality:
    res = searchProvinces(x)
    print(res)