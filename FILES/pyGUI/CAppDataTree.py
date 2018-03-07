# ---------------------------------------------------------------------------- #
# Class UserPanels
# ---------------------------------------------------------------------------- #
import wx
import time

import specific_files.dfgui

class AppData_TreeCtrl(wx.TreeCtrl):
    def __init__(self, parent):#, appData):
        wx.TreeCtrl.__init__(self, parent, -1, wx.Point(0, 0), wx.Size(160, 250),
                           wx.TR_DEFAULT_STYLE | wx.NO_BORDER)

        # def Create_AppData_TreeCtrl(parent, appData):
        """
        todo:
         1. verify if already opened window like this - and update content. (will be in parenting caller).
            other option - pressing 'show app data' will toggle window off ?
         2. capture double click on dataType, and accordingly open window of table or list of vars or some graph or text editor or run excecutable
         3. verify if data is copied or referenced..
    
         4. when loaded file - add time tag for file reading time (will be in OnDrag..)
    
         chcek http://www.java2s.com/Tutorial/Python/0380__wxPython/Treenodebegineditevent.htm
    
        """

        frame_title = "Loaded data files"

        # tree = wx.TreeCtrl(parent, -1, wx.Point(0, 0), wx.Size(160, 250),
        #                    wx.TR_DEFAULT_STYLE | wx.NO_BORDER)
        #
        imglist = wx.ImageList(16, 16, True, 2)
        imglist.Add(wx.ArtProvider.GetBitmap(wx.ART_FOLDER, wx.ART_OTHER, wx.Size(16, 16)))
        imglist.Add(wx.ArtProvider.GetBitmap(wx.ART_NORMAL_FILE, wx.ART_OTHER, wx.Size(16, 16)))
        self.AssignImageList(imglist)

        self.Bind(wx.EVT_TREE_ITEM_ACTIVATED, self.treeItemActivatedCapture) # will catch mouse double click only if the above is not binded
        self.Bind(wx.EVT_RIGHT_DOWN         , self.onRightClick)  # catch mouse right click

        self.root = self.AddRoot(frame_title, 0)  #todo: init with None and replace if appData not empty
        self.items = []

    def populateTree(self, appData):
        for ndx, item in enumerate(appData.mainDict):
            prefix = "(#" + str(ndx) + ") "
            self.items.append(self.AppendItem(self.root, prefix + item.alias, 0))
            sub_item = self.items[-1]
            self.AppendItem(sub_item, item.Name, 1)
            self.AppendItem(sub_item, item.Path, 1)
            self.AppendItem(sub_item, item.Type, 1)
            self.AppendItem(sub_item, str(item.fileID), 1)
            self.AppendItem(sub_item, item.dataTimeStamp, 1)

            # tree.SetItemData(sub_item, item)  # will create copy also of the data
            self.SetItemData(sub_item, item.fileID)

        self.Expand(self.root)

    def treeItemActivatedCapture(self, event=None):
        if __debug__:
            print "tree dbl clk"

        # print time.time()
        # print time.ctime()
        treeItem            = event.EventObject
        selectedItem        = event.EventObject.Selections[0]
        selectedItemLabel   = treeItem.GetItemText(selectedItem)
        selectedItemParent  = treeItem.GetItemParent(selectedItem)

        appDataRelevantFileID = treeItem.GetItemData(selectedItem)
        if appDataRelevantFileID == None:
            appDataRelevantFileID = treeItem.GetItemData(selectedItemParent)

        # treeItem.SelectItem(selectedItem)

        print "valid tree id? : " + str(event.EventObject.Selections[0].IsOk())
        print "number of items in whole tree: " + str(treeItem.GetCount())

        # if (treeItem.Children):
        #     treeItem.SelectChildren()

        # treeItem.CollapseAll()
        # treeItem.ExpandAll()

        # treeRoot = treeItem.GetRootItem()
        # treeItem.SelectItem(treeRoot)

        if appDataRelevantFileID > -1:  #todo: change -1 to some app constant
            print 'appDataRelFileID gt -1'
            if self.Parent.Parent._appDataRef.mainDict[appDataRelevantFileID].Type == 'DataFrame':
                parentWindowCtrl = self.Parent.Parent
                DFdata = parentWindowCtrl._appDataRef.mainDict[appDataRelevantFileID].loadedData

                # show data in wx table under parent, with stored identification related to main appData
                ## specific_files.dfgui.show(DFdata)
                trimmedDF = dfActions.get_trimmed_DF(DFdata, 15, 6) # todo: put as constants from INI
                # wxPnl = specific_files.dfgui.show_tabel_panel(DFdata, parentWindowCtrl)
                wxPnl = specific_files.dfgui.show_tabel_panel(trimmedDF, parentWindowCtrl)
                parentWindowCtrl.Create_DFtable(wxPnl)

                headersList = list(DFdata.columns.values) # or list(DFdata)  # can tty also sorted(DFdata)
        ##
        pieces = []
        item = treeItem.GetSelection()
        while item:
            piece = treeItem.GetItemText(item)
            pieces.insert(0, piece)
            item = treeItem.GetItemParent(item)
        print "item path tree : "
        print pieces
        ##
        # wx.MessageBox("msg box")

    def onRightClick(self, event):
        if __debug__:
            print("right clicked ")

        print time.ctime()
        treeItem        = event.EventObject
        selectedItem    = event.EventObject.Selections[0]
        selectedItemLabel   = treeItem.GetItemText(selectedItem)
        selectedItemParent  = treeItem.GetItemParent(selectedItem)

        appDataRelevantFileID = treeItem.GetItemData(selectedItem)
        if appDataRelevantFileID == None:
            appDataRelevantFileID = treeItem.GetItemData(selectedItemParent)

        if appDataRelevantFileID > -1:  # todo: change -1 to some app constant
            parentWindowCtrl = self.Parent.Parent
            DFdata = parentWindowCtrl._appDataRef.mainDict[appDataRelevantFileID].loadedData
            headersList = list(DFdata.columns.values)  # or list(DFdata)  # can tty also sorted(DFdata)

        pieces = []
        item = treeItem.GetSelection()
        while item:
            piece = treeItem.GetItemText(item)
            pieces.insert(0, piece)
            item = treeItem.GetItemParent(item)
        print "item path tree : "
        print pieces
        pass
        list(parentWindowCtrl._appDataRef.mainDict[0].loadedData)
