from AUI_GlobalImports import *

appDataObj  = appDB.myAppData()
appDataObj.initializeDataFields()
print appDataObj.lastPastedText

commonPath = u'C:/Users/Ran_the_User/Documents/GitHub\pyFiles\FILES\pyGUI/simOutputsData/'
#filePath = 'C:\Users\Ran_the_User\Documents\RAN\python\pandastable-master\pandastable\datasets/'
fileBaseNames = ['2018_2_5_3_28_47_quad_sim.csv'
                , '2018_2_5_3_29_25_quad_sim.csv'
                ,'2018_2_5_3_30_33_quad_sim.csv'
                ,'2018_2_5_3_31_24_quad_sim.csv']
fileNames = map(lambda n : commonPath + n, fileBaseNames)
#fileName1 = commonPath + fileBaseNames[0]
#fileName2 = commonPath + fileBaseNames[1]
#fileName3 = commonPath + fileBaseNames[2]

fileDictionaries = map(lambda n : files_handler.get_file_details(n), fileNames)
#fileDict1 = files_handler.get_file_details(fileName1)
#fileDict2 = files_handler.get_file_details(fileName2)
#fileDict3 = files_handler.get_file_details(fileName3)
map(lambda n: files_handler.load_CSV_to_appData(n, appDataObj, headerVar = False), fileDictionaries);
#files_handler.load_CSV_to_appData(fileDict1, appDataObj, headerVar = False);
#files_handler.load_CSV_to_appData(fileDict2, appDataObj, headerVar = False);
#files_handler.load_CSV_to_appData(fileDict3, appDataObj, headerVar = False);
loadedFiles = appDataObj.mainDict
print loadedFiles
#########################################
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
#########################################

# get the DataFrames themselves :     
fileA = loadedFiles[0].loadedData
fileB = loadedFiles[1].loadedData

print fileA.info()
print fileB.info()

testDF = fileA

a = testDF.head()
b = testDF.tail()
print a
print a.append(b)
# print b.append(a)  #upside


c= testDF.get_values()
print c
c= dfActions.get_header(testDF)  # get header. maybe find a better not questionable formula ??
print c

##########################################
t = dfActions.get_columns_by_name(testDF, 0) 
y = dfActions.get_columns_by_name(testDF, 1) 
fig1 = gui_plots.plot_Var_Vs_Time(y , t, title='Ran trial') # todo:
gui_plots.show_the_constructed_plots()
