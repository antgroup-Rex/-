# keep common data for the app
# verify : http://www.python-course.eu/python3_global_vs_local_variables.php

import sys
sys.path.append('../from_demo_agw')
sys.path.append('../')

import glob
import os

class myAppData(dict):

    testField='a'

    def __init__(self):
        # self.mainDict       = dict()
        # self.lastPastedText = ''
        # self.lastPastedUrl  = ''
        # self.testField='b'
        pass

    def initializeDataFields(self):
        self.mainDict = dict()
        self.lastPastedText = 'selfInitTest1'
        self.lastPastedUrl = 'selfInitTest2'
        self.testField='c'


if __name__=='__main__':
    appDict = myAppData()
    print appDict.testField
    appDict.initializeDataFields()
    print appDict.testField

