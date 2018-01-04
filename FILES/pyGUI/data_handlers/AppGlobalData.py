# keep common data for the app
# verify : http://www.python-course.eu/python3_global_vs_local_variables.php

import sys
sys.path.append('../from_demo_agw')
sys.path.append('../')

import glob
import os

########################################
class fileObj():
    Name =''        # full file path and name
    Type = ''
    Path=''
    alias =''
    loadedData ={}

########################################
class myAppData(dict):

    testField='a'

    def __init__(self):
        # self.mainDict       = dict()
        # self.lastPastedText = ''
        # self.lastPastedUrl  = ''
        # self.testField='b'
        pass

    def initializeDataFields(self):
        self.mainDict = list()  # dict()
        self.lastPastedText = 'selfInitTest1'
        self.lastPastedUrl  = 'selfInitTest2'
        self.testField      ='c'

    def import_data_from_CSV(self,fileName):
        
        pass

    def addDataFromFile(self, fileObj):
        # global tmp1
        self.mainDict.append(fileObj)

##################################################

if __name__=='__main__':
    appDict = myAppData()
    print appDict.testField
    appDict.initializeDataFields()
    print appDict.testField

    tmp1 = fileObj()
    tmp1.Name='rtrial.file'
    tmp1.alias='tryial'
    tmp1.loadedData=[]
    tmp1.Path='.'
    tmp1.Type='.py'

    tmp2 = fileObj()
    tmp2.Name = 'C:\Users\Ran_the_User\Documents\GitHub\pyFiles\FILES\myODE_case\quad_sim.csv'

    appDict.addDataFromFile(tmp1)
    appDict.addDataFromFile(tmp2)

    print "appdict:"
    print appDict
