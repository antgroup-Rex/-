from AUI_GlobalImports import *

appDataObj  = appDB.myAppData()
appDataObj.initializeDataFields()
print appDataObj.lastPastedText

fileDict1 = files_handler.get_file_details(u'C:/Users/Ran_the_User/Documents/GitHub\pyFiles\FILES\pyGUI/quad_sim.csv')
filePath = 'C:\Users\Ran_the_User\Documents\RAN\python\pandastable-master\pandastable\datasets/'
fileDict2 = files_handler.get_file_details(u'C:/Users\Ran_the_User\Documents\RAN\python\pandastable-master\pandastable\datasets/titanic3.csv')
fileDict3 = files_handler.get_file_details(u'C:/Users\Ran_the_User\Documents\RAN\python\pandastable-master\pandastable\datasets/tips.csv')
files_handler.load_CSV_to_appData(fileDict1, appDataObj);
files_handler.load_CSV_to_appData(fileDict2, appDataObj);
files_handler.load_CSV_to_appData(fileDict3, appDataObj);
loadedFiles = appDataObj.mainDict
print loadedFiles
for ndx, itm in enumerate(loadedFiles):
    print ndx
    print itm.Name
    
for ndx, itm in enumerate(loadedFiles):
    print ndx
    print itm.Name
    print itm.Type
    print itm.alias
    print itm.dataTimeStamp
    print itm.fileID
    print itm.Path
    print "*********"
    
fileA = loadedFiles[0].loadedData
fileB = loadedFiles[1].loadedData

testDF = fileA

a = testDF.head()
b = testDF.tail()
print a
print a.append(b)
# print b.append(a)  #upside


c= testDF.get_values()
print c
c= list(testDF)  # get header. maybe find a better not questionable formula ??
print c

