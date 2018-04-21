# ---------------------------------------------------------------------------- #
# Class UserPanels
# ---------------------------------------------------------------------------- #
import wx
import time

import specific_files.dfgui


import data_handlers.DataFrames_actions    	as dfActions

class AppData_TreeCtrl(wx.TreeCtrl):
    def __init__(self, parent):#, appData):
#        wx.TreeCtrl.__init__(self, parent, -1, 
#                             wx.Point(0, 0), wx.Size(160, 250),
#                             wx.TR_DEFAULT_STYLE | wx.NO_BORDER)
        
        wx.TreeCtrl.__init__(self, parent, -1
                             , wx.DefaultPosition, wx.DefaultSize,
                               wx.TR_HAS_BUTTONS
                               | wx.TR_EDIT_LABELS
                               | wx.TR_MULTIPLE
                               | wx.TR_DEFAULT_STYLE 
                               | wx.NO_BORDER
                               #| wx.TR_HIDE_ROOT
                               #, self.log
                             )

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

        self.Bind(wx.EVT_TREE_ITEM_ACTIVATED, self.treeItemActivated) # will catch mouse double click only if the above is not binded
#        self.Bind(wx.EVT_RIGHT_DOWN         , self.onRightClick)  # catch mouse right click
        
        self.Bind(wx.EVT_RIGHT_DOWN, self.OnRightDown)
        self.Bind(wx.EVT_RIGHT_UP, self.OnRightUp)
        
        self.Bind(wx.EVT_TREE_BEGIN_LABEL_EDIT, self.OnBeginEdit)
        self.Bind(wx.EVT_TREE_END_LABEL_EDIT,   self.OnEndEdit)

        self.root = self.AddRoot(frame_title, 0)  #todo: init with None and replace if appData not empty
        self.items = []
###################################################

    def OnBeginEdit(self, event):
        print("OnEdit Begin\n")
        item = event.GetItem()
        if item and self.GetItemText(item) == "The Root Item":
            wx.Bell() 
            print ("You can't edit this one...\n")
            event.Veto()
            
    def OnEndEdit(self, event):
#        self.log.WriteText
        print("OnEdit end: %s %s\n" %
                           (event.IsEditCancelled(), event.GetLabel()) )
        # todo : allow label edit only for main label
        item = event.GetItem()
        label = event.GetLabel()
        if item and ("(#" in label):
#        if label == '':
            print("You can't change this property...\n")
            event.Veto()
###################################################


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

    def treeItemActivated(self, event=None):
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
            print "appDataRelevantFileID == None"
            print "treeItem"
            print treeItem
            print "selectedItem"
            print selectedItem
            print "selectedItemLabel"
            print selectedItemLabel
            print "selectedItemParent:"
            print selectedItemParent
            if selectedItemLabel!="Loaded data files":
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
                ##                 specific_files.dfgui.show(DFdata)
                trimmedDF = DFdata
                ###
                trimmedDFrows = min(15, len(DFdata)) # todo: put as constants from INI
                trimmedDFcols = min(6, len(list(DFdata))) # todo: put as constants from INI
                trimmedDF = dfActions.get_trimmed_DF(DFdata, trimmedDFrows, trimmedDFcols)
                wxPnl = specific_files.dfgui.show_tabel_panel(trimmedDF, parentWindowCtrl)
                parentWindowCtrl.Create_DFtable(wxPnl)

                headersList = list(DFdata.columns.values) # or list(DFdata)  # can tty also sorted(DFdata)
                print headersList
        ##
        pieces = []
        # todo: condition with .not. multi selection tree
        # item = treeItem.GetSelection()
        item = selectedItem
        while item:
            piece = treeItem.GetItemText(item)
            pieces.insert(0, piece)
            item = treeItem.GetItemParent(item)
        print "item path tree : "
        print pieces
        ##
        # wx.MessageBox("msg box")
###################################################


    def OnRightDown(self, event):
        
        pt = event.GetPosition()
        item, flags = self.HitTest(pt)

        if item:
            self.item = item
#            self.log.write
            print("OnRightDown: %s, %s, %s" % (self.GetItemText(item), type(item), item.__class__) + "\n")
            self.SelectItem(item)
            ########
            self.OnRightUp(event)
            ########

    def OnRightUp(self, event):

        item = self.item
        
        if not item:
            event.Skip()
            return

        print("OnRightUp: %s, %s, %s" % (self.GetItemText(item), type(item), item.__class__) + "\n")

        print "starting popup"
        
        # Item Text Appearance
        # ishtml = self.IsItemHyperText(item)
        back   = self.GetItemBackgroundColour(item)
        fore   = self.GetItemTextColour(item)
        isbold = self.IsBold(item)
        font   = self.GetItemFont(item)

#        # Icons On Item
#        normal   = self.GetItemImage(item, wx.TreeItemIcon_Normal)
#        selected = self.GetItemImage(item, CT.TreeItemIcon_Selected)
#        expanded = self.GetItemImage(item, CT.TreeItemIcon_Expanded)
#        selexp   = self.GetItemImage(item, CT.TreeItemIcon_SelectedExpanded)

        # Enabling/Disabling Windows Associated To An Item
        # haswin = self.GetItemWindow(item)

        # Enabling/Disabling Items
        # enabled = self.IsItemEnabled(item)

        # Generic Item's Info
        children  = self.GetChildrenCount(item)
        # itemtype  = self.GetItemType(item)
        text      = self.GetItemText(item)
        pydata    = self.GetPyData(item)
        # separator = self.IsItemSeparator(item)
        
        self.current = item
        self.itemdict = {"back": back, "fore": fore, "isbold": isbold, "font": font,
                         "children": children, "text": text, "pydata": pydata}
        
        ''''''
        menu = wx.Menu()

        item1 = menu.Append(wx.ID_ANY, "Change item background colour")
        item2 = menu.Append(wx.ID_ANY, "Modify item text colour")
        menu.AppendSeparator()

        if isbold:
            strs = "Make item text not bold"
        else:
            strs = "Make item text bold"

        item3 = menu.Append(wx.ID_ANY, strs)
        item4 = menu.Append(wx.ID_ANY, "Change item font")
        menu.AppendSeparator()

        # if ishtml:
        #     strs = "Set item as non-hyperlink"
        # else:
        strs = "Set item as hyperlink"
            
        item5 = menu.Append(wx.ID_ANY, strs)
        menu.AppendSeparator()

        item13 = menu.Append(wx.ID_ANY, "Insert separator")
        menu.AppendSeparator()
        
        # if haswin:
        #     enabled = self.GetItemWindowEnabled(item)
        #     if enabled:
        #         strs = "Disable associated widget"
        #     else:
        #         strs = "Enable associated widget"
        # else:
        strs = "Enable associated widget"
            
        item6 = menu.Append(wx.ID_ANY, strs)

        # if not haswin:
        item6.Enable(False)

        item7 = menu.Append(wx.ID_ANY, "Disable item")
        
        menu.AppendSeparator()
        item8 = menu.Append(wx.ID_ANY, "Change item icons")
        menu.AppendSeparator()
        item9 = menu.Append(wx.ID_ANY, "Get other information for this item")
        menu.AppendSeparator()

        item10 = menu.Append(wx.ID_ANY, "Delete item")
        if item == self.GetRootItem():
            item10.Enable(False)
            item13.Enable(False)
            
        item11 = menu.Append(wx.ID_ANY, "Prepend an item")
        item12 = menu.Append(wx.ID_ANY, "Append an item")

#        self.Bind(wx.EVT_MENU, self.OnItemBackground, item1)
#        self.Bind(wx.EVT_MENU, self.OnItemForeground, item2)
        self.Bind(wx.EVT_MENU, self.OnItemBold, item3)
#        self.Bind(wx.EVT_MENU, self.OnItemFont, item4)
#        self.Bind(wx.EVT_MENU, self.OnItemHyperText, item5)
#        self.Bind(wx.EVT_MENU, self.OnEnableWindow, item6)
#        self.Bind(wx.EVT_MENU, self.OnDisableItem, item7)
#        self.Bind(wx.EVT_MENU, self.OnItemIcons, item8)
#        self.Bind(wx.EVT_MENU, self.OnItemInfo, item9)
#        self.Bind(wx.EVT_MENU, self.OnItemDelete, item10)
#        self.Bind(wx.EVT_MENU, self.OnItemPrepend, item11)
#        self.Bind(wx.EVT_MENU, self.OnItemAppend, item12)
#        self.Bind(wx.EVT_MENU, self.OnSeparatorInsert, item13)
#        
        self.PopupMenu(menu)
        menu.Destroy()
        
    def OnItemBold(self, event):

        self.SetItemBold(self.current, not self.itemdict["isbold"])


    def OnItemDelete(self, event):

        strs = "Are You Sure You Want To Delete Item " + self.GetItemText(self.current) + "?"
        dlg = wx.MessageDialog(None, strs, 'Deleting Item', wx.YES_NO | wx.NO_DEFAULT | wx.CANCEL | wx.ICON_QUESTION)

        if dlg.ShowModal() in [wx.ID_NO, wx.ID_CANCEL]:
            dlg.Destroy()
            return

        dlg.Destroy()

        self.DeleteChildren(self.current)
        self.Delete(self.current)
        self.current = None
        
        # todo: delete item for appObj
                

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
###################################################
