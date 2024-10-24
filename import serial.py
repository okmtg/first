from firebase import firebase

db=firebase.FirebaseApplication("https://microbittest-e396d-default-rtdb.europe-west1.firebasedatabase.app/")
db.delete("temp",None)

import serial

ser = serial.Serial(timeout = 1)
ser.baudrate = 115200
ser.port = "COM26"
ser.open()

dataCount = 0
dataList = []
dataDic = {}
final_list=[]
x=0
while x<30:

    dataCount += 1
    data = ser.readline()
    data = data.decode("utf-8").strip()
    dataList.append(data)
    if dataCount >= 10:
        for entry in dataList:
            if entry not in dataDic:
                dataDic[entry] = { "count" : 0 }
            else:
                dataDic[entry]["count"] += 1
        currentData = ""
        currentDataCount = 0
        for entry in dataDic:
            if dataDic[entry]["count"] > currentDataCount:
                currentData = entry
                currentDataCount = dataDic[entry]["count"]
            
            
        print(currentData)
        final_list.append(currentData)
        x+=1
        dataCount = 0
        dataList.clear()
        dataDic.clear()
         
        record={"Lightlevel": currentData }
        db.post("/temp", record)
        allrec=db.get("/temp", None)
        
        for ke in allrec:
            print(allrec[ke])


    

    