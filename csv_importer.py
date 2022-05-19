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
    dataArray.append("airport,city,lat,long")
    dataDiagram.append("airport,city,lat,long")
    # Retrive the CSV data
    for line in f:
        
        words = line.split(",") # split the csv data into array
        length = len(words)
        
        # Split method for text with comma inside double 
        for i in range(length):
            if '"' in words[i]:
                if '"""' in words[i]:
                    break
                words[i] += "," + words[i+1]
                words.remove(words[i+1])
                break
            
        length = len(words)
        for i in range(length):
            if words[i].isdigit():
                words[i] = int(words[i])
        # Split method for text with comma inside double 
        
        # Retrive the required column airport
        for i in range(len(words)):
            # print (i, words[i])
            if words[i] == 'airport':
                airportItem = i
                # break
            if words[airportItem] != 'iata':
                colData_1 = words[airportItem].replace('|', ',')
                # print (i, colData_1)
        
        # Retrive the required column city        
        for i in range(len(words)):
            if words[i] == 'city':
                cityItem = i
                # break
            if words[cityItem] != 'iata':
                colData_2 = words[cityItem].replace('|', ',')
                # print (i, colData_2)
        
        # Retrive the required column latitude        
        for i in range(len(words)):
            if words[i] == 'lat':
                latItem = i
                # break
            if words[latItem] != 'iata':
                colData_3 = words[latItem]
                # print (i, colData_3)
        
        # Retrive the required column longtude
        for i in range(len(words)):
            if words[i] == 'long\n':
                longItem = i
                break
            colData_4 = words[longItem]
            if colData_4 != 'iata':
                colData_4 = colData_4.replace('\n','')
                textData = colData_1 + ',' + colData_2 + ',' + colData_3 + ',' + colData_4
                dataArray.append(textData) #insert the required data to array
            
                if(colData_3 != "" and colData_4 != ""):
                    latFloat = float(colData_3) 
                    longFloat = float(colData_4)
                    
                    #coordinate data validation 
                    if((latFloat >= 32 and latFloat <= 37) and (longFloat >= -100 and longFloat <= -80) ):
                        xData.append(latFloat)
                        yData.append(longFloat)
                        textDiagram = colData_1 + ',' + colData_2 + ',' + colData_3 + ',' + colData_4
                        dataDiagram.append(textDiagram)
                        break
    #Retrive the array data to text loop
    newData = list(dict.fromkeys(dataArray))  
    newDiagram = list(dict.fromkeys(dataDiagram))
    
#All row file create     
with open('airport-data.txt', 'x') as w:
    w.write('\n'.join(str(item) for item in newData) + '\n')
    
#All row within coordinate data validation    
with open('coordiante.txt', 'x') as r:
    r.write('\n'.join(str(item) for item in newDiagram) + '\n')    

#Scatter diagram layout    
plt.scatter(xData, yData)
plt.xlabel('Latitude')
plt.ylabel('Longtitude')
plt.xlim(32,37)
plt.ylim([-100,-80])
plt.show()