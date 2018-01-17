# ---------------------------------------------------------------------------- #
# Class UserPanels
# ---------------------------------------------------------------------------- #
import wx
import time


class AppData_TreeCtrl(wx.TreeCtrl):
    def __init__(self, parent, appData):
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

        root = tree.AddRoot(frame_title, 0)  #todo: init with None and replace if appData not empty
        items = []

        for ndx, item in enumerate(appData.mainDict):
            prefix = "(#" + str(ndx) + ") "
            items.append(tree.AppendItem(root, prefix + item.alias, 0))
            sub_item = items[-1]
            tree.AppendItem(sub_item, item.Name, 1)
            tree.AppendItem(sub_item, item.Path, 1)
            tree.AppendItem(sub_item, item.Type, 1)
            tree.AppendItem(sub_item, str(item.fileID), 1)
            tree.AppendItem(sub_item, item.dataTimeStamp, 1)

            # tree.SetItemData(sub_item, item)  # will create copy also of the data
            tree.SetItemData(sub_item, item.fileID)

        tree.Expand(root)

        tree.Bind(wx.EVT_TREE_ITEM_ACTIVATED, treeItemActivatedCapture) # will catch mouse double click only if the above is not binded

        return tree

def treeItemActivatedCapture(event=None):
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


    # wx.MessageBox("msg box")