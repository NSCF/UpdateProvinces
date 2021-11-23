from writecsvHs import writecsv

records = [{'BRAHMS': '813', 'COLLECTOR': 'Curator Pretoria Bot. Garden', 'NUMBER': 'PRE 43343', 'SPECIES': 'Xanthium strumarium L.', 'COUNTRY': 'South Africa', 'MAJORAREA': 'Transvaal', 'LOCNOTES': 'DIVISION OF BOTANY', 'LLRES': '', 'QDS': '', 'LATDEC': '0', 'LONGDEC': '', 'updatedProv': '', 'Check': 'y'},
 {'BRAHMS': '814', 'COLLECTOR': 'Curator Pretoria Bot. Garden', 'NUMBER': '7924', 'SPECIES': 'Xanthium strumarium L.', 'COUNTRY': 'South Africa', 'MAJORAREA': 'Transvaal', 'LOCNOTES': 'DIVISION OF BOTANY', 'LLRES': '', 'QDS': '', 'LATDEC': '0', 'LONGDEC': '0', 'updatedProv': '', 'Check': 'y'},
 {'BRAHMS': '823', 'COLLECTOR': 'Curator Pretoria Bot. Garden', 'NUMBER': 'PRE 43352', 'SPECIES': 'Xanthium strumarium L.', 'COUNTRY': 'South Africa', 'MAJORAREA': 'Transvaal', 'LOCNOTES': 'LABORATORY GROUNDS', 'LLRES': '', 'QDS': '', 'LATDEC': '0', 'LONGDEC': '0', 'updatedProv': '', 'Check': 'y'}, 
 {'BRAHMS': '828', 'COLLECTOR': 'van Niekerk, M.', 'NUMBER': 'TRV 7523', 'SPECIES': 'Callilepis lancifolia Burtt Davy', 'COUNTRY': 'South Africa', 'MAJORAREA': 'Transvaal', 'LOCNOTES': 'GREAT OLIFANTS RIVER', 'LLRES': '', 'QDS': '', 'LATDEC': '0', 'LONGDEC': '0', 'updatedProv': 'LP', 'Check': 'y'},
 {'BRAHMS': '829', 'COLLECTOR': 'Crawley, V.G.', 'NUMBER': 'TRV 10405', 'SPECIES': 'Callilepis lancifolia Burtt Davy', 'COUNTRY': 'South Africa', 'MAJORAREA': 'Transvaal', 'LOCNOTES': 'WOLHUTERSKOP', 'LLRES': '1/4dg', 'QDS': '2527DA', 'LATDEC': '-25.62166', 'LONGDEC': '27.62166', 'updatedProv': 'MP', 'Check': 'y'}]

writecsv(records, 'provTest.csv')