# keep common data for the app
# verify : http://www.python-course.eu/python3_global_vs_local_variables.php

import sys
sys.path.append('../from_demo_agw')
sys.path.append('../')

import glob
import os

class myAppData(dict):

    def __init__(self):
        self.mainDict       = dict()
        self.lastPastedText = ''
        self.lastPastedUrl  = ''

if __name__=='__main__':
    appDict = myAppData()




