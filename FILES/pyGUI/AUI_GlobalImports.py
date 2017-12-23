''''''
# import wx # ran note: used directly by CSizeReportCtrl
import wx.html
import wx.grid

import os
import sys
# import time # ran note: used directly by CProgressGauge

import specific_files.AppGlobalData         as appDB

# import specific_files.pyTesting_xml_to_nexX as rNX  #ran - TODO : set the import just as class preparation
import from_demo_agw.ZoomBar                as zB
import from_demo_agw.XMLtreeview            as Xtr
import from_demo_agw.DragAndDrop            as DD
import from_demo_agw.ShapedWindows          as ShpWin

try:
    dirName = os.path.dirname(os.path.abspath(__file__))
except:
    dirName = os.path.dirname(os.path.abspath(sys.argv[0]))

sys.path.append(os.path.split(dirName)[0])

''' separated files from the original main AUI file '''
from Intro_html_text        import *
from CSizeReportCtrl        import *
from CProgressGauge         import *

import random
import from_demo_agw.images as images

from AUI_settingsPanel import *
from AUI_JsonControlPanel import *