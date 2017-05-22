#show tif files
# possible refs:
# https://blog.philippklaus.de/2011/08/handle-16bit-tiff-images-in-python
# https://matplotlib.org/users/image_tutorial.html

import wx
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.backends.backend_wxagg import \
        FigureCanvasWxAgg as FigCanvas, \
        NavigationToolbar2WxAgg as NavigationToolbar
import sys
sys.path.append('../from_demo_agw')
sys.path.append('../')

import glob
import os

# import DragAndDrop as DD
# import AUI_MAIN as AMain

class ShowTifInPath(wx.Panel):

    def __init__(self,parent):

        wx.Panel.__init__(self, parent)

        self.fig = plt.figure()
        self.canvas = FigCanvas(self, -1, self.fig)

        self.lastFileName = ''
        self.filesPath = ''

        self.canvas.Bind(wx.EVT_KEY_DOWN    , self.OnDwnKeyPress)    
        self.canvas.Bind(wx.EVT_KEY_UP      , self.OnUpKeyPress)
        self.canvas.Bind(wx.EVT_ENTER_WINDOW, self.ChangeCursor)

    def ChangeCursor(self, event):
        self.canvas.SetCursor(wx.StockCursor(wx.CURSOR_BULLSEYE))

    def updateTif(self,tifFullName):
        img = mpimg.imread(tifFullName)
        self.imgplot.set_data(img)
        self.canvas.draw()
        # self.vbox.Fit(self)  #bad for getting correct resize
        self.canvas.Refresh()

        return self.imgplot

    def showTif(self,tifFullName):
        img = mpimg.imread(tifFullName)
        self.imgplot = plt.imshow(img)

        cBar = plt.colorbar()
        self.toolbar = NavigationToolbar(self.canvas)
        # plt.axis('off')

        self.vbox = wx.BoxSizer(wx.VERTICAL)
        self.vbox.Add(self.canvas, 1, wx.LEFT | wx.TOP | wx.GROW)
        self.vbox.Add(self.toolbar, 0, wx.EXPAND)

        self.SetSizer(self.vbox)

        self.vbox.Fit(self)

        return self.imgplot, cBar

    def OnDwnKeyPress(self, event):
        print "dwnKey"

    def OnUpKeyPress(self, event):
        print "onUpKey"
        pressedKey = event.GetKeyCode()
        if (pressedKey==wx.WXK_LEFT) | (pressedKey==wx.WXK_DOWN):
            print"left / down key"
            #currentIndex % len(relevant items)
            filesList = list(panel.filesInfo)
            if (filesList[3] > 0):
                filesList[3] = (filesList[3]) - 1
            else:
                filesList[3] = len(filesList[2])-1;
            panel.filesInfo = tuple(filesList)
            newFileName = panel.filesInfo[2][filesList[3]]
            panel.updateTif(newFileName)

        elif (pressedKey==wx.WXK_RIGHT) | (pressedKey==wx.WXK_UP):
            print "right / up key"
            #currentIndex % len(relevant items)
            filesList = list(panel.filesInfo)
            if (filesList[3] < (len(filesList[2])-1)):
                filesList[3]= (filesList[3]) + 1
            else:
                filesList[3] = 0;
            panel.filesInfo = tuple(filesList)
            newFileName = panel.filesInfo[2][filesList[3]]
            panel.updateTif(newFileName)

        elif (pressedKey == wx.WXK_NUMPAD_ADD) :
            print "+ key"
        elif (pressedKey == wx.WXK_NUMPAD_SUBTRACT):
            print "- key"

        return pressedKey

    def getSimilarFilesInfo(self,firstDropedFileFullName):
        full_path = os.path.dirname(firstDropedFileFullName)
        fullFileName, file_extension = os.path.splitext(firstDropedFileFullName)
        allSimilarFiles = glob.glob(full_path + "\\*" + file_extension)
        fileIndexInList = allSimilarFiles.index(firstDropedFileFullName)
        print firstDropedFileFullName
        # print fullFileName
        # print full_path
        print file_extension
        print allSimilarFiles
        print fileIndexInList

        return (full_path, file_extension, allSimilarFiles, fileIndexInList)

class MinimumDropTarget(wx.PyDropTarget):
    ''' handles ony file types '''
    def __init__(self):
        wx.PyDropTarget.__init__(self)

        self.doComposite = wx.DataObjectComposite()
        self.filedo = wx.FileDataObject()

        self.doComposite.Add(self.filedo)
        self.SetDataObject(self.doComposite)

    def OnData(self, x, y, result):
        """
        Handles drag/dropping files/text or a bitmap
        """

        if self.GetData():
            # formatType, formatId = self.GetReceivedFormatAndId()
            formatType = self.GetReceivedFormatAndId()
            if formatType == wx.DF_FILENAME:
                return self.OnFileDrop()

        return result  # you must return this


    def GetReceivedFormatAndId(self):
        format     = self.doComposite.GetReceivedFormat()
        formatType = format.GetType()
        return formatType

    def OnFileDrop(self):
        print "OnFileDrop:"
        filesNames = self.filedo.GetFilenames()
        # for name in filesNames:
        #     print name

        firstDropedFileFullName         = filesNames[0]

        panel.updateTif(firstDropedFileFullName)

        panel.filesInfo = panel.getSimilarFilesInfo(firstDropedFileFullName)

        return wx.DragCopy


if __name__=='__main__':
    tiff_file = '.\\tif\\CCITT_2.TIF'

    app     = wx.App()#PySimpleApp()
    fr      = wx.Frame(None, title='main test')
    panel   = ShowTifInPath(fr)

    # log = AMain.Log()
    # obj =  DD.OtherDropTarget(panel, log)
    # obj =  DD.FileDropPanel(panel, log)
    obj=MinimumDropTarget()
    fr.SetDropTarget(obj)

    # panel.draw()
    panel.showTif(tiff_file)
    panel.filesInfo = panel.getSimilarFilesInfo(tiff_file)

    app.SetTopWindow(fr)
    fr.Show()
    app.MainLoop()

    #from PIL import Image
    #im = Image.open(tiff_file)
    ##im.show()
    #
    #import matplotlib.pyplot as plt
    #I = plt.imread(tiff_file)   #ndarray type
    #plt.show()

