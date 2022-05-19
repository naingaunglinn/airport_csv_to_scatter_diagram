import matplotlib.pyplot as plt

filePath = input("Pleae enter your file path: ")
with open(filePath, 'r') as f:
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
    xData = []
    yData = []
    for line in f:
        words = line.split(',(?=")')
        words = words[0].split(',(?=")')
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
                colData_2 = words[cityItem].replace('|', ',')
                
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
                dataArray.append((colData_1,colData_2,colData_3,colData_4)) 
                
                latFloat = float(colData_3) 
                longFloat = float(colData_4)
                if((latFloat >= 32 and latFloat <= 37) and (longFloat >= -100 and longFloat <= -80) ):
                    xData.append(latFloat)
                    yData.append(longFloat)
                    dataDiagram.append((colData_1,colData_2,colData_3,colData_4))
                    break
                
    newData = list(dict.fromkeys(dataArray))  
    newDiagram = list(dict.fromkeys(dataDiagram))
    
with open('airport-data.txt', 'x') as w:
    w.write('\n'.join(str(item) for item in newData) + '\n')
    
with open('coordiante.txt', 'x') as r:
    r.write('\n'.join(str(item) for item in newDiagram) + '\n')    
    
plt.scatter(xData, yData)
plt.xlabel('Latitude')
plt.ylabel('Longtitude')
plt.xlim(32,37)
plt.ylim([-100,-80])
plt.show()