with open('airports.csv', 'r') as f:
    results = []
    dataArray = []
    dataDiagram = []
    colData_1 = ''
    colData_2 = ''
    colData_3 = ''
    colData_4 = ''
    airportItem = 0
    cityItem = 0
    latItem = 0
    longItem = 0
    
    for line in f:
        words = line.split(',')
        results.append(words)
        # print (words[1])
        
        for i in range(len(words)):
            # print (i, words[i])
            if words[i] == 'airport':
                airportItem = i
                # break
            if words[airportItem] != 'iata' and words[airportItem] != 'airport':
                colData_1 = words[airportItem].replace('|', ',')
        
        for i in range(len(words)):
            if words[i] == 'city':
                cityItem = i
                # break
            if words[cityItem] != 'iata' and words[cityItem] != 'city':
                colData_2 = words[cityItem]
                
        for i in range(len(words)):
            if words[i] == 'lat':
                latItem = i
                # break
            if words[latItem] != 'iata' and words[latItem] != 'lat':
                colData_3 = words[latItem]
                # print (words[latItem])
        
        for i in range(len(words)):
            if words[i] == 'long\n':
                longItem = i
                # break
            if words[longItem] != 'iata' and words[longItem] != 'long' and words[longItem] != 'long\n':
                colData_4 = words[longItem]
                colData_4 = colData_4.replace('\n','')
                if colData_3 == 'USA':
                    print (colData_3, latItem, words)
                    break;    
                dataArray.append((colData_1,colData_2,colData_3,colData_4)) 
                
                latFloat = float(colData_3) 
                longFloat = float(colData_4)
                if((latFloat >= 32 and latFloat <= 37) and (longFloat >= -100 and longFloat <= -80) ):
                    dataDiagram.append((colData_1,colData_2,colData_3,colData_4))
                    break
                
                              
                
    newData = list(dict.fromkeys(dataArray))  
    newDiagram = list(dict.fromkeys(dataDiagram))   
    # print(results)       
    # print(newData)    
    
with open('airport-data.txt', 'x') as w:
    w.write('\n'.join(str(item) for item in newData) + '\n')
    
with open('coordiante.txt', 'x') as r:
    r.write('\n'.join(str(item) for item in newDiagram) + '\n')    
    