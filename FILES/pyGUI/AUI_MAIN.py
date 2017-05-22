''''''
# import wx # ran note: used directly by CSizeReportCtrl
import wx.html
import wx.grid

import os
import sys
# import time # ran note: used directly by CProgressGauge

# import specific_files.pyTesting_xml_to_nexX as rNX  #ran - TODO : set the import just as class preparation
import from_demo_agw.ZoomBar                as zB
import from_demo_agw.XMLtreeview            as Xtr
import from_demo_agw.DragAndDrop            as DD

try:
    dirName = os.path.dirname(os.path.abspath(__file__))
except:
    dirName = os.path.dirname(os.path.abspath(sys.argv[0]))

sys.path.append(os.path.split(dirName)[0])

try:
    from agw import aui
    from agw.aui import aui_switcherdialog as ASD
except ImportError: # if it's not there locally, try the wxPython lib.
    import wx.lib.agw.aui as aui
    from wx.lib.agw.aui import aui_switcherdialog as ASD

''' separated files from the original main AUI file '''
from Custom_pane_buttons    import *
from Intro_html_text        import *
from CSizeReportCtrl        import *
from CProgressGauge         import *

import random
import from_demo_agw.images as images

#----------------------------------------------------------------------


# Custom pane bitmaps reference
#                      bitmap  button id       active  maximize
CUSTOM_PANE_BITMAPS = [(close, aui.AUI_BUTTON_CLOSE, True, False),
                       (close_inactive, aui.AUI_BUTTON_CLOSE, False, False),
                       (minimize, aui.AUI_BUTTON_MINIMIZE, True, False),
                       (minimize_inactive, aui.AUI_BUTTON_MINIMIZE, False, False),
                       (maximize, aui.AUI_BUTTON_MAXIMIZE_RESTORE, True, True),
                       (maximize_inactive, aui.AUI_BUTTON_MAXIMIZE_RESTORE, False, True),
                       (restore, aui.AUI_BUTTON_MAXIMIZE_RESTORE, True, False),
                       (restore_inactive, aui.AUI_BUTTON_MAXIMIZE_RESTORE, False, False)]

#----------------------------------------------------------------------
# Custom buttons in tab area
#
CUSTOM_TAB_BUTTONS = {"Left": [(sort, aui.AUI_BUTTON_CUSTOM1),
                               (superscript, aui.AUI_BUTTON_CUSTOM2)],
                      "Right": [(fullscreen, aui.AUI_BUTTON_CUSTOM3),
                                (remove, aui.AUI_BUTTON_CUSTOM4),
                                (reload, aui.AUI_BUTTON_CUSTOM5)]
                      }
#----------------------------------------------------------------------


ArtIDs = [ "wx.ART_ADD_BOOKMARK",
           "wx.ART_DEL_BOOKMARK",
           "wx.ART_HELP_SIDE_PANEL",
           "wx.ART_HELP_SETTINGS",
           "wx.ART_HELP_BOOK",
           "wx.ART_HELP_FOLDER",
           "wx.ART_HELP_PAGE",
           "wx.ART_GO_BACK",
           "wx.ART_GO_FORWARD",
           "wx.ART_GO_UP",
           "wx.ART_GO_DOWN",
           "wx.ART_GO_TO_PARENT",
           "wx.ART_GO_HOME",
           "wx.ART_FILE_OPEN",
           "wx.ART_PRINT",
           "wx.ART_HELP",
           "wx.ART_TIP",
           "wx.ART_REPORT_VIEW",
           "wx.ART_LIST_VIEW",
           "wx.ART_NEW_DIR",
           "wx.ART_HARDDISK",
           "wx.ART_FLOPPY",
           "wx.ART_CDROM",
           "wx.ART_REMOVABLE",
           "wx.ART_FOLDER",
           "wx.ART_FOLDER_OPEN",
           "wx.ART_GO_DIR_UP",
           "wx.ART_EXECUTABLE_FILE",
           "wx.ART_NORMAL_FILE",
           "wx.ART_TICK_MARK",
           "wx.ART_CROSS_MARK",
           "wx.ART_ERROR",
           "wx.ART_QUESTION",
           "wx.ART_WARNING",
           "wx.ART_INFORMATION",
           "wx.ART_MISSING_IMAGE",
           ]

#----------------------------------------------------------------------

# Define a translation function
_ = wx.GetTranslation

ID_CreateTree = wx.ID_HIGHEST + 1
ID_CreateGrid = ID_CreateTree + 1
ID_CreateText = ID_CreateTree + 2
ID_CreateHTML = ID_CreateTree + 3
ID_CreateNotebook = ID_CreateTree + 4
ID_CreateSizeReport = ID_CreateTree + 5
ID_GridContent = ID_CreateTree + 6
ID_TextContent = ID_CreateTree + 7
ID_TreeContent = ID_CreateTree + 8
ID_HTMLContent = ID_CreateTree + 9
ID_NotebookContent = ID_CreateTree + 10
ID_SizeReportContent = ID_CreateTree + 11
ID_SwitchPane = ID_CreateTree + 12
ID_CreatePerspective = ID_CreateTree + 13
ID_CopyPerspectiveCode = ID_CreateTree + 14
ID_CreateNBPerspective = ID_CreateTree + 15
ID_CopyNBPerspectiveCode = ID_CreateTree + 16
ID_AllowFloating = ID_CreateTree + 17
ID_AllowActivePane = ID_CreateTree + 18
ID_TransparentHint = ID_CreateTree + 19
ID_VenetianBlindsHint = ID_CreateTree + 20
ID_RectangleHint = ID_CreateTree + 21
ID_NoHint = ID_CreateTree + 22
ID_HintFade = ID_CreateTree + 23
ID_NoVenetianFade = ID_CreateTree + 24
ID_TransparentDrag = ID_CreateTree + 25
ID_NoGradient = ID_CreateTree + 26
ID_VerticalGradient = ID_CreateTree + 27
ID_HorizontalGradient = ID_CreateTree + 28
ID_LiveUpdate = ID_CreateTree + 29
ID_AnimateFrames = ID_CreateTree + 30
ID_PaneIcons = ID_CreateTree + 31
ID_TransparentPane = ID_CreateTree + 32
ID_DefaultDockArt = ID_CreateTree + 33
ID_ModernDockArt = ID_CreateTree + 34
ID_SnapToScreen = ID_CreateTree + 35
ID_SnapPanes = ID_CreateTree + 36
ID_FlyOut = ID_CreateTree + 37
ID_CustomPaneButtons = ID_CreateTree + 38
ID_Settings = ID_CreateTree + 39
ID_CustomizeToolbar = ID_CreateTree + 40
ID_DropDownToolbarItem = ID_CreateTree + 41
ID_MinimizePosSmart = ID_CreateTree + 42
ID_MinimizePosTop = ID_CreateTree + 43
ID_MinimizePosLeft = ID_CreateTree + 44
ID_MinimizePosRight = ID_CreateTree + 45
ID_MinimizePosBottom = ID_CreateTree + 46
ID_MinimizeCaptSmart = ID_CreateTree + 47
ID_MinimizeCaptHorz = ID_CreateTree + 48
ID_MinimizeCaptHide = ID_CreateTree + 49
ID_NotebookNoCloseButton = ID_CreateTree + 50
ID_NotebookCloseButton = ID_CreateTree + 51
ID_NotebookCloseButtonAll = ID_CreateTree + 52
ID_NotebookCloseButtonActive = ID_CreateTree + 53
ID_NotebookCloseOnLeft = ID_CreateTree + 54
ID_NotebookAllowTabMove = ID_CreateTree + 55
ID_NotebookAllowTabExternalMove = ID_CreateTree + 56
ID_NotebookAllowTabSplit = ID_CreateTree + 57
ID_NotebookTabFloat = ID_CreateTree + 58
ID_NotebookTabDrawDnd = ID_CreateTree + 59
ID_NotebookDclickUnsplit = ID_CreateTree + 60
ID_NotebookWindowList = ID_CreateTree + 61
ID_NotebookScrollButtons = ID_CreateTree + 62
ID_NotebookTabFixedWidth = ID_CreateTree + 63
ID_NotebookArtGloss = ID_CreateTree + 64
ID_NotebookArtSimple = ID_CreateTree + 65
ID_NotebookArtVC71 = ID_CreateTree + 66
ID_NotebookArtFF2 = ID_CreateTree + 67
ID_NotebookArtVC8 = ID_CreateTree + 68
ID_NotebookArtChrome = ID_CreateTree + 69
ID_NotebookAlignTop = ID_CreateTree + 70
ID_NotebookAlignBottom = ID_CreateTree + 71
ID_NotebookHideSingle = ID_CreateTree + 72
ID_NotebookSmartTab = ID_CreateTree + 73
ID_NotebookUseImagesDropDown = ID_CreateTree + 74
ID_NotebookCustomButtons = ID_CreateTree + 75
ID_NotebookMinMaxWidth = ID_CreateTree + 76

ID_SampleItem = ID_CreateTree + 77
ID_StandardGuides = ID_CreateTree + 78
ID_AeroGuides = ID_CreateTree + 79
ID_WhidbeyGuides = ID_CreateTree + 80
ID_NotebookPreview = ID_CreateTree + 81
ID_PreviewMinimized = ID_CreateTree + 82

ID_SmoothDocking = ID_CreateTree + 83
ID_NativeMiniframes = ID_CreateTree + 84

ID_RanDDContent = ID_CreateTree + 85    #ran

ID_FirstPerspective = ID_CreatePerspective + 1000
ID_FirstNBPerspective = ID_CreateNBPerspective + 10000

ID_PaneBorderSize = ID_SampleItem + 100
ID_SashSize = ID_PaneBorderSize + 2
ID_CaptionSize = ID_PaneBorderSize + 3
ID_BackgroundColour = ID_PaneBorderSize + 4
ID_SashColour = ID_PaneBorderSize + 5
ID_InactiveCaptionColour = ID_PaneBorderSize + 6
ID_InactiveCaptionGradientColour = ID_PaneBorderSize + 7
ID_InactiveCaptionTextColour = ID_PaneBorderSize + 8
ID_ActiveCaptionColour = ID_PaneBorderSize + 9
ID_ActiveCaptionGradientColour = ID_PaneBorderSize + 10
ID_ActiveCaptionTextColour = ID_PaneBorderSize + 11
ID_BorderColour = ID_PaneBorderSize + 12
ID_GripperColour = ID_PaneBorderSize + 13
ID_SashGrip = ID_PaneBorderSize + 14
ID_HintColour = ID_PaneBorderSize + 15

ID_VetoTree = ID_PaneBorderSize + 16
ID_VetoText = ID_PaneBorderSize + 17
ID_NotebookMultiLine = ID_PaneBorderSize + 18

#  TODO: create AUI directory for all files that will be resulted from this AUI.py big file
#         -AUI
#           -imports
#           -images
#           -classes
#           -mainAUI
#

########################################################################
########################################################################
#todo: consider seperating this class. it depends on the controls IDs.
class SettingsPanel(wx.Panel):

    def __init__(self, parent, frame):

        wx.Panel.__init__(self, parent)
        self._frame = frame

        s1 = wx.BoxSizer(wx.HORIZONTAL)
        self._border_size = wx.SpinCtrl(self, ID_PaneBorderSize, "%d"%frame.GetDockArt().GetMetric(aui.AUI_DOCKART_PANE_BORDER_SIZE),
                                        wx.DefaultPosition, wx.Size(50, 20), wx.SP_ARROW_KEYS, 0, 100,
                                        frame.GetDockArt().GetMetric(aui.AUI_DOCKART_PANE_BORDER_SIZE))
        s1.Add((1, 1), 1, wx.EXPAND)
        s1.Add(wx.StaticText(self, -1, "Pane Border Size:"))
        s1.Add(self._border_size)
        s1.Add((1, 1), 1, wx.EXPAND)
        s1.SetItemMinSize(1, (180, 20))

        s2 = wx.BoxSizer(wx.HORIZONTAL)
        self._sash_size = wx.SpinCtrl(self, ID_SashSize, "%d"%frame.GetDockArt().GetMetric(aui.AUI_DOCKART_SASH_SIZE), wx.DefaultPosition,
                                      wx.Size(50, 20), wx.SP_ARROW_KEYS, 0, 100, frame.GetDockArt().GetMetric(aui.AUI_DOCKART_SASH_SIZE))
        s2.Add((1, 1), 1, wx.EXPAND)
        s2.Add(wx.StaticText(self, -1, "Sash Size:"))
        s2.Add(self._sash_size)
        s2.Add((1, 1), 1, wx.EXPAND)
        s2.SetItemMinSize(1, (180, 20))

        s3 = wx.BoxSizer(wx.HORIZONTAL)
        self._caption_size = wx.SpinCtrl(self, ID_CaptionSize, "%d"%frame.GetDockArt().GetMetric(aui.AUI_DOCKART_CAPTION_SIZE),
                                         wx.DefaultPosition, wx.Size(50, 20), wx.SP_ARROW_KEYS, 0, 100, frame.GetDockArt().GetMetric(aui.AUI_DOCKART_CAPTION_SIZE))
        s3.Add((1, 1), 1, wx.EXPAND)
        s3.Add(wx.StaticText(self, -1, "Caption Size:"))
        s3.Add(self._caption_size)
        s3.Add((1, 1), 1, wx.EXPAND)
        s3.SetItemMinSize(1, (180, 20))

        b = self.CreateColourBitmap(wx.BLACK)

        s4 = wx.BoxSizer(wx.HORIZONTAL)
        self._background_colour = wx.BitmapButton(self, ID_BackgroundColour, b, wx.DefaultPosition, wx.Size(50, 25))
        s4.Add((1, 1), 1, wx.EXPAND)
        s4.Add(wx.StaticText(self, -1, "Background Colour:"))
        s4.Add(self._background_colour)
        s4.Add((1, 1), 1, wx.EXPAND)
        s4.SetItemMinSize(1, (180, 20))

        s5 = wx.BoxSizer(wx.HORIZONTAL)
        self._sash_colour = wx.BitmapButton(self, ID_SashColour, b, wx.DefaultPosition, wx.Size(50, 25))
        s5.Add((1, 1), 1, wx.EXPAND)
        s5.Add(wx.StaticText(self, -1, "Sash Colour:"))
        s5.Add(self._sash_colour)
        s5.Add((1, 1), 1, wx.EXPAND)
        s5.SetItemMinSize(1, (180, 20))

        s6 = wx.BoxSizer(wx.HORIZONTAL)
        self._inactive_caption_colour = wx.BitmapButton(self, ID_InactiveCaptionColour, b, wx.DefaultPosition, wx.Size(50, 25))
        s6.Add((1, 1), 1, wx.EXPAND)
        s6.Add(wx.StaticText(self, -1, "Normal Caption:"))
        s6.Add(self._inactive_caption_colour)
        s6.Add((1, 1), 1, wx.EXPAND)
        s6.SetItemMinSize(1, (180, 20))

        s7 = wx.BoxSizer(wx.HORIZONTAL)
        self._inactive_caption_gradient_colour = wx.BitmapButton(self, ID_InactiveCaptionGradientColour, b, wx.DefaultPosition, wx.Size(50, 25))
        s7.Add((1, 1), 1, wx.EXPAND)
        s7.Add(wx.StaticText(self, -1, "Normal Caption Gradient:"))
        s7.Add(self._inactive_caption_gradient_colour)
        s7.Add((1, 1), 1, wx.EXPAND)
        s7.SetItemMinSize(1, (180, 20))

        s8 = wx.BoxSizer(wx.HORIZONTAL)
        self._inactive_caption_text_colour = wx.BitmapButton(self, ID_InactiveCaptionTextColour, b, wx.DefaultPosition, wx.Size(50, 25))
        s8.Add((1, 1), 1, wx.EXPAND)
        s8.Add(wx.StaticText(self, -1, "Normal Caption Text:"))
        s8.Add(self._inactive_caption_text_colour)
        s8.Add((1, 1), 1, wx.EXPAND)
        s8.SetItemMinSize(1, (180, 20))

        s9 = wx.BoxSizer(wx.HORIZONTAL)
        self._active_caption_colour = wx.BitmapButton(self, ID_ActiveCaptionColour, b, wx.DefaultPosition, wx.Size(50, 25))
        s9.Add((1, 1), 1, wx.EXPAND)
        s9.Add(wx.StaticText(self, -1, "Active Caption:"))
        s9.Add(self._active_caption_colour)
        s9.Add((1, 1), 1, wx.EXPAND)
        s9.SetItemMinSize(1, (180, 20))

        s10 = wx.BoxSizer(wx.HORIZONTAL)
        self._active_caption_gradient_colour = wx.BitmapButton(self, ID_ActiveCaptionGradientColour, b, wx.DefaultPosition, wx.Size(50, 25))
        s10.Add((1, 1), 1, wx.EXPAND)
        s10.Add(wx.StaticText(self, -1, "Active Caption Gradient:"))
        s10.Add(self._active_caption_gradient_colour)
        s10.Add((1, 1), 1, wx.EXPAND)
        s10.SetItemMinSize(1, (180, 20))

        s11 = wx.BoxSizer(wx.HORIZONTAL)
        self._active_caption_text_colour = wx.BitmapButton(self, ID_ActiveCaptionTextColour, b, wx.DefaultPosition, wx.Size(50, 25))
        s11.Add((1, 1), 1, wx.EXPAND)
        s11.Add(wx.StaticText(self, -1, "Active Caption Text:"))
        s11.Add(self._active_caption_text_colour)
        s11.Add((1, 1), 1, wx.EXPAND)
        s11.SetItemMinSize(1, (180, 20))

        s12 = wx.BoxSizer(wx.HORIZONTAL)
        self._border_colour = wx.BitmapButton(self, ID_BorderColour, b, wx.DefaultPosition, wx.Size(50, 25))
        s12.Add((1, 1), 1, wx.EXPAND)
        s12.Add(wx.StaticText(self, -1, "Border Colour:"))
        s12.Add(self._border_colour)
        s12.Add((1, 1), 1, wx.EXPAND)
        s12.SetItemMinSize(1, (180, 20))

        s13 = wx.BoxSizer(wx.HORIZONTAL)
        self._gripper_colour = wx.BitmapButton(self, ID_GripperColour, b, wx.DefaultPosition, wx.Size(50,25))
        s13.Add((1, 1), 1, wx.EXPAND)
        s13.Add(wx.StaticText(self, -1, "Gripper Colour:"))
        s13.Add(self._gripper_colour)
        s13.Add((1, 1), 1, wx.EXPAND)
        s13.SetItemMinSize(1, (180, 20))

        s14 = wx.BoxSizer(wx.HORIZONTAL)
        self._sash_grip = wx.CheckBox(self, ID_SashGrip, "", wx.DefaultPosition, wx.Size(50,20))
        s14.Add((1, 1), 1, wx.EXPAND)
        s14.Add(wx.StaticText(self, -1, "Draw Sash Grip:"))
        s14.Add(self._sash_grip)
        s14.Add((1, 1), 1, wx.EXPAND)
        s14.SetItemMinSize(1, (180, 20))

        s15 = wx.BoxSizer(wx.HORIZONTAL)
        self._hint_colour = wx.BitmapButton(self, ID_HintColour, b, wx.DefaultPosition, wx.Size(50,25))
        s15.Add((1, 1), 1, wx.EXPAND)
        s15.Add(wx.StaticText(self, -1, "Hint Window Colour:"))
        s15.Add(self._hint_colour)
        s15.Add((1, 1), 1, wx.EXPAND)
        s15.SetItemMinSize(1, (180, 20))

        grid_sizer = wx.GridSizer(0, 2)
        grid_sizer.SetHGap(5)
        grid_sizer.Add(s1)
        grid_sizer.Add(s4)
        grid_sizer.Add(s2)
        grid_sizer.Add(s5)
        grid_sizer.Add(s3)
        grid_sizer.Add(s13)
        grid_sizer.Add(s14)
        grid_sizer.Add((1, 1))
        grid_sizer.Add(s12)
        grid_sizer.Add(s6)
        grid_sizer.Add(s9)
        grid_sizer.Add(s7)
        grid_sizer.Add(s10)
        grid_sizer.Add(s8)
        grid_sizer.Add(s11)
        grid_sizer.Add(s15)

        cont_sizer = wx.BoxSizer(wx.VERTICAL)
        cont_sizer.Add(grid_sizer, 1, wx.EXPAND | wx.ALL, 5)
        self.SetSizer(cont_sizer)
        self.GetSizer().SetSizeHints(self)

        self._border_size.SetValue(frame.GetDockArt().GetMetric(aui.AUI_DOCKART_PANE_BORDER_SIZE))
        self._sash_size.SetValue(frame.GetDockArt().GetMetric(aui.AUI_DOCKART_SASH_SIZE))
        self._caption_size.SetValue(frame.GetDockArt().GetMetric(aui.AUI_DOCKART_CAPTION_SIZE))
        self._sash_grip.SetValue(frame.GetDockArt().GetMetric(aui.AUI_DOCKART_DRAW_SASH_GRIP))

        self.UpdateColours()

        self.Bind(wx.EVT_SPINCTRL, self.OnPaneBorderSize, id=ID_PaneBorderSize)
        self.Bind(wx.EVT_SPINCTRL, self.OnSashSize, id=ID_SashSize)
        self.Bind(wx.EVT_SPINCTRL, self.OnCaptionSize, id=ID_CaptionSize)
        self.Bind(wx.EVT_CHECKBOX, self.OnDrawSashGrip, id=ID_SashGrip)
        self.Bind(wx.EVT_BUTTON, self.OnSetColour, id=ID_BackgroundColour)
        self.Bind(wx.EVT_BUTTON, self.OnSetColour, id=ID_SashColour)
        self.Bind(wx.EVT_BUTTON, self.OnSetColour, id=ID_InactiveCaptionColour)
        self.Bind(wx.EVT_BUTTON, self.OnSetColour, id=ID_InactiveCaptionGradientColour)
        self.Bind(wx.EVT_BUTTON, self.OnSetColour, id=ID_InactiveCaptionTextColour)
        self.Bind(wx.EVT_BUTTON, self.OnSetColour, id=ID_ActiveCaptionColour)
        self.Bind(wx.EVT_BUTTON, self.OnSetColour, id=ID_ActiveCaptionGradientColour)
        self.Bind(wx.EVT_BUTTON, self.OnSetColour, id=ID_ActiveCaptionTextColour)
        self.Bind(wx.EVT_BUTTON, self.OnSetColour, id=ID_BorderColour)
        self.Bind(wx.EVT_BUTTON, self.OnSetColour, id=ID_GripperColour)
        self.Bind(wx.EVT_BUTTON, self.OnSetColour, id=ID_HintColour)


    def CreateColourBitmap(self, c):

        image = wx.EmptyImage(25, 14)
        for x in xrange(25):
            for y in xrange(14):
                pixcol = c
                if x == 0 or x == 24 or y == 0 or y == 13:
                    pixcol = wx.BLACK

                image.SetRGB(x, y, pixcol.Red(), pixcol.Green(), pixcol.Blue())

        return image.ConvertToBitmap()


    def UpdateColours(self):

        bk = self._frame.GetDockArt().GetColour(aui.AUI_DOCKART_BACKGROUND_COLOUR)
        self._background_colour.SetBitmapLabel(self.CreateColourBitmap(bk))

        cap = self._frame.GetDockArt().GetColour(aui.AUI_DOCKART_INACTIVE_CAPTION_COLOUR)
        self._inactive_caption_colour.SetBitmapLabel(self.CreateColourBitmap(cap))

        capgrad = self._frame.GetDockArt().GetColour(aui.AUI_DOCKART_INACTIVE_CAPTION_GRADIENT_COLOUR)
        self._inactive_caption_gradient_colour.SetBitmapLabel(self.CreateColourBitmap(capgrad))

        captxt = self._frame.GetDockArt().GetColour(aui.AUI_DOCKART_INACTIVE_CAPTION_TEXT_COLOUR)
        self._inactive_caption_text_colour.SetBitmapLabel(self.CreateColourBitmap(captxt))

        acap = self._frame.GetDockArt().GetColour(aui.AUI_DOCKART_ACTIVE_CAPTION_COLOUR)
        self._active_caption_colour.SetBitmapLabel(self.CreateColourBitmap(acap))

        acapgrad = self._frame.GetDockArt().GetColour(aui.AUI_DOCKART_ACTIVE_CAPTION_GRADIENT_COLOUR)
        self._active_caption_gradient_colour.SetBitmapLabel(self.CreateColourBitmap(acapgrad))

        acaptxt = self._frame.GetDockArt().GetColour(aui.AUI_DOCKART_ACTIVE_CAPTION_TEXT_COLOUR)
        self._active_caption_text_colour.SetBitmapLabel(self.CreateColourBitmap(acaptxt))

        sash = self._frame.GetDockArt().GetColour(aui.AUI_DOCKART_SASH_COLOUR)
        self._sash_colour.SetBitmapLabel(self.CreateColourBitmap(sash))

        border = self._frame.GetDockArt().GetColour(aui.AUI_DOCKART_BORDER_COLOUR)
        self._border_colour.SetBitmapLabel(self.CreateColourBitmap(border))

        gripper = self._frame.GetDockArt().GetColour(aui.AUI_DOCKART_GRIPPER_COLOUR)
        self._gripper_colour.SetBitmapLabel(self.CreateColourBitmap(gripper))

        hint = self._frame.GetDockArt().GetColour(aui.AUI_DOCKART_HINT_WINDOW_COLOUR)
        self._hint_colour.SetBitmapLabel(self.CreateColourBitmap(hint))


    def OnPaneBorderSize(self, event):

        self._frame.GetDockArt().SetMetric(aui.AUI_DOCKART_PANE_BORDER_SIZE,
                                           event.GetInt())
        self._frame.DoUpdate()


    def OnSashSize(self, event):

        self._frame.GetDockArt().SetMetric(aui.AUI_DOCKART_SASH_SIZE,
                                           event.GetInt())
        self._frame.DoUpdate()


    def OnCaptionSize(self, event):

        self._frame.GetDockArt().SetMetric(aui.AUI_DOCKART_CAPTION_SIZE,
                                           event.GetInt())
        self._frame.DoUpdate()


    def OnDrawSashGrip(self, event):

        self._frame.GetDockArt().SetMetric(aui.AUI_DOCKART_DRAW_SASH_GRIP,
                                           event.GetInt())
        self._frame.DoUpdate()


    def OnSetColour(self, event):

        dlg = wx.ColourDialog(self._frame)
        dlg.SetTitle("Colour Picker")

        if dlg.ShowModal() != wx.ID_OK:
            return

        evId = event.GetId()
        if evId == ID_BackgroundColour:
            var = aui.AUI_DOCKART_BACKGROUND_COLOUR
        elif evId == ID_SashColour:
            var = aui.AUI_DOCKART_SASH_COLOUR
        elif evId == ID_InactiveCaptionColour:
            var = aui.AUI_DOCKART_INACTIVE_CAPTION_COLOUR
        elif evId == ID_InactiveCaptionGradientColour:
            var = aui.AUI_DOCKART_INACTIVE_CAPTION_GRADIENT_COLOUR
        elif evId == ID_InactiveCaptionTextColour:
            var = aui.AUI_DOCKART_INACTIVE_CAPTION_TEXT_COLOUR
        elif evId == ID_ActiveCaptionColour:
            var = aui.AUI_DOCKART_ACTIVE_CAPTION_COLOUR
        elif evId == ID_ActiveCaptionGradientColour:
            var = aui.AUI_DOCKART_ACTIVE_CAPTION_GRADIENT_COLOUR
        elif evId == ID_ActiveCaptionTextColour:
            var = aui.AUI_DOCKART_ACTIVE_CAPTION_TEXT_COLOUR
        elif evId == ID_BorderColour:
            var = aui.AUI_DOCKART_BORDER_COLOUR
        elif evId == ID_GripperColour:
            var = aui.AUI_DOCKART_GRIPPER_COLOUR
        elif evId == ID_HintColour:
            var = aui.AUI_DOCKART_HINT_WINDOW_COLOUR
        else:
            return

        self._frame.GetDockArt().SetColour(var, dlg.GetColourData().GetColour())
        self._frame.DoUpdate()
        self.UpdateColours()

########################################################################
########################################################################

class AuiFrame(wx.Frame):

    def __init__(self, parent, id=wx.ID_ANY, title="", pos= wx.DefaultPosition,
                 size=wx.DefaultSize, style=wx.DEFAULT_FRAME_STYLE|wx.SUNKEN_BORDER, log=None):

        wx.Frame.__init__(self, parent, id, title, pos, size, style)

        self._mgr = aui.AuiManager()

        # tell AuiManager to manage this frame
        self._mgr.SetManagedWindow(self)
        
        # set frame icon
        self.SetIcon(images.Mondrian.GetIcon()) #TODO: set to relevant icon file

        # set up default notebook style
        self._notebook_style = aui.AUI_NB_DEFAULT_STYLE | aui.AUI_NB_TAB_EXTERNAL_MOVE | wx.NO_BORDER
        self._notebook_theme = 0
        # Attributes
        self._textCount = 1
        self._transparency = 255
        self._snapped = False
        self._custom_pane_buttons = False
        self._custom_tab_buttons = False
        self._pane_icons = False
        self._veto_tree = self._veto_text = False

        self.log = log

        self.CreateStatusBar()
        self.GetStatusBar().SetStatusText("Ready")

        self.BuildPanes()
        self.CreateMenuBar()
        self.BindEvents()


    def CreateMenuBar(self):

        # create menu
        mb = wx.MenuBar()

        file_menu = wx.Menu()
        file_menu.Append(wx.ID_EXIT, "Exit")

        view_menu = wx.Menu()
        view_menu.Append(ID_CreateText, "Create Text Control")
        view_menu.Append(ID_CreateHTML, "Create HTML Control")
        view_menu.Append(ID_CreateTree, "Create Tree")
        view_menu.Append(ID_CreateGrid, "Create Grid")
        view_menu.Append(ID_CreateNotebook, "Create Notebook")
        view_menu.Append(ID_CreateSizeReport, "Create Size Reporter")
        view_menu.AppendSeparator()
        view_menu.Append(ID_GridContent, "Use a Grid for the Content Pane")
        view_menu.Append(ID_TextContent, "Use a Text Control for the Content Pane")
        view_menu.Append(ID_HTMLContent, "Use an HTML Control for the Content Pane")
        view_menu.Append(ID_TreeContent, "Use a Tree Control for the Content Pane")
        view_menu.Append(ID_NotebookContent, "Use a AuiNotebook control for the Content Pane")

        view_menu.Append(ID_RanDDContent, "Use a ID_RanDDContent control for the Content Pane")  #todo: replace with min layout commnad

        view_menu.Append(ID_SizeReportContent, "Use a Size Reporter for the Content Pane")
        view_menu.AppendSeparator()

##        if wx.Platform == "__WXMAC__":
##            switcherAccel = "Alt+Tab"
##        elif wx.Platform == "__WXGTK__":
##            switcherAccel = "Ctrl+/"
##        else:
##            switcherAccel = "Ctrl+Tab"
##
##        view_menu.Append(ID_SwitchPane, _("S&witch Window...") + "\t" + switcherAccel)

        options_menu = wx.Menu()
        options_menu.AppendRadioItem(ID_TransparentHint, "Transparent Hint")
        options_menu.AppendRadioItem(ID_VenetianBlindsHint, "Venetian Blinds Hint")
        options_menu.AppendRadioItem(ID_RectangleHint, "Rectangle Hint")
        options_menu.AppendRadioItem(ID_NoHint, "No Hint")
        options_menu.AppendSeparator()
        options_menu.AppendCheckItem(ID_HintFade, "Hint Fade-in")
        options_menu.AppendCheckItem(ID_AllowFloating, "Allow Floating")
        options_menu.AppendCheckItem(ID_NoVenetianFade, "Disable Venetian Blinds Hint Fade-in")
        options_menu.AppendCheckItem(ID_TransparentDrag, "Transparent Drag")
        options_menu.AppendCheckItem(ID_AllowActivePane, "Allow Active Pane")
        options_menu.AppendCheckItem(ID_LiveUpdate, "Live Resize Update")
        options_menu.AppendCheckItem(ID_NativeMiniframes, "Use Native wx.MiniFrames")
        options_menu.AppendSeparator()
        options_menu.AppendRadioItem(ID_MinimizePosSmart, "Minimize in Smart mode").Check()
        options_menu.AppendRadioItem(ID_MinimizePosTop, "Minimize on Top")
        options_menu.AppendRadioItem(ID_MinimizePosLeft, "Minimize on the Left")
        options_menu.AppendRadioItem(ID_MinimizePosRight, "Minimize on the Right")
        options_menu.AppendRadioItem(ID_MinimizePosBottom, "Minimize at the Bottom")
        options_menu.AppendSeparator()
        options_menu.AppendRadioItem(ID_MinimizeCaptSmart, "Smart Minimized Caption")
        options_menu.AppendRadioItem(ID_MinimizeCaptHorz, "Horizontal Minimized Caption")
        options_menu.AppendRadioItem(ID_MinimizeCaptHide, "Hidden Minimized Caption").Check()
        options_menu.AppendSeparator()
        options_menu.AppendCheckItem(ID_PaneIcons, "Set Icons On Panes")
        options_menu.AppendCheckItem(ID_AnimateFrames, "Animate Dock/Close/Minimize Of Floating Panes")
        options_menu.AppendCheckItem(ID_SmoothDocking, "Smooth Docking Effects (PyQT Style)")
        options_menu.AppendSeparator()
        options_menu.Append(ID_TransparentPane, "Set Floating Panes Transparency")
        options_menu.AppendSeparator()
        options_menu.AppendRadioItem(ID_DefaultDockArt, "Default DockArt")
        options_menu.AppendRadioItem(ID_ModernDockArt, "Modern Dock Art")
        options_menu.AppendSeparator()
        options_menu.Append(ID_SnapToScreen, "Snap To Screen")
        options_menu.AppendCheckItem(ID_SnapPanes, "Snap Panes To Managed Window")
        options_menu.AppendCheckItem(ID_FlyOut, "Use Fly-Out Floating Panes")
        options_menu.AppendSeparator()
        options_menu.AppendCheckItem(ID_CustomPaneButtons, "Set Custom Pane Button Bitmaps")
        options_menu.AppendSeparator()
        options_menu.AppendRadioItem(ID_NoGradient, "No Caption Gradient")
        options_menu.AppendRadioItem(ID_VerticalGradient, "Vertical Caption Gradient")
        options_menu.AppendRadioItem(ID_HorizontalGradient, "Horizontal Caption Gradient")
        options_menu.AppendSeparator()
        options_menu.AppendCheckItem(ID_PreviewMinimized, "Preview Minimized Panes")
        options_menu.AppendSeparator()
        options_menu.Append(ID_Settings, "Settings Pane")

        notebook_menu = wx.Menu()
        notebook_menu.AppendRadioItem(ID_NotebookArtGloss, "Glossy Theme (Default)")
        notebook_menu.AppendRadioItem(ID_NotebookArtSimple, "Simple Theme")
        notebook_menu.AppendRadioItem(ID_NotebookArtVC71, "VC71 Theme")
        notebook_menu.AppendRadioItem(ID_NotebookArtFF2, "Firefox 2 Theme")
        notebook_menu.AppendRadioItem(ID_NotebookArtVC8, "VC8 Theme")
        notebook_menu.AppendRadioItem(ID_NotebookArtChrome, "Chrome Theme")
        notebook_menu.AppendSeparator()
        notebook_menu.AppendRadioItem(ID_NotebookNoCloseButton, "No Close Button")
        notebook_menu.AppendRadioItem(ID_NotebookCloseButton, "Close Button At Right")
        notebook_menu.AppendRadioItem(ID_NotebookCloseButtonAll, "Close Button On All Tabs")
        notebook_menu.AppendRadioItem(ID_NotebookCloseButtonActive, "Close Button On Active Tab")
        notebook_menu.AppendSeparator()
        notebook_menu.AppendCheckItem(ID_NotebookCloseOnLeft, "Close Button On The Left Of Tabs")
        notebook_menu.AppendSeparator()
        notebook_menu.AppendRadioItem(ID_NotebookAlignTop, "Tab Top Alignment")
        notebook_menu.AppendRadioItem(ID_NotebookAlignBottom, "Tab Bottom Alignment")
        notebook_menu.AppendSeparator()
        notebook_menu.AppendCheckItem(ID_NotebookAllowTabMove, "Allow Tab Move")
        notebook_menu.AppendCheckItem(ID_NotebookAllowTabExternalMove, "Allow External Tab Move")
        notebook_menu.AppendCheckItem(ID_NotebookAllowTabSplit, "Allow Notebook Split")
        notebook_menu.AppendCheckItem(ID_NotebookTabFloat, "Allow Single Tab Floating")
        notebook_menu.AppendSeparator()
        notebook_menu.AppendCheckItem(ID_NotebookDclickUnsplit, "Unsplit On Sash Double-Click")
        notebook_menu.AppendCheckItem(ID_NotebookTabDrawDnd, "Draw Tab Image On Drag 'n' Drop")
        notebook_menu.AppendSeparator()
        notebook_menu.AppendCheckItem(ID_NotebookScrollButtons, "Scroll Buttons Visible")
        notebook_menu.AppendCheckItem(ID_NotebookWindowList, "Window List Button Visible")
        notebook_menu.AppendCheckItem(ID_NotebookTabFixedWidth, "Fixed-Width Tabs")
        notebook_menu.AppendSeparator()
        notebook_menu.AppendCheckItem(ID_NotebookHideSingle, "Hide On Single Tab")
        notebook_menu.AppendCheckItem(ID_NotebookSmartTab, "Use Smart Tabbing")
        notebook_menu.AppendCheckItem(ID_NotebookUseImagesDropDown, "Use Tab Images In Dropdown Menu")
        notebook_menu.AppendCheckItem(ID_NotebookCustomButtons, "Show Custom Buttons In Tab Area")
        notebook_menu.AppendSeparator()
        notebook_menu.Append(ID_NotebookMinMaxWidth, "Set Min/Max Tab Widths")
        notebook_menu.Append(ID_NotebookMultiLine, "Add A Multi-Line Label Tab")
        notebook_menu.AppendSeparator()
        notebook_menu.Append(ID_NotebookPreview, "Preview Of All Notebook Pages")

        perspectives_menu = wx.Menu()

        self._perspectives_menu = wx.Menu()
        self._perspectives_menu.Append(ID_CreatePerspective, "Create Perspective")
        self._perspectives_menu.Append(ID_CopyPerspectiveCode, "Copy Perspective Data To Clipboard")
        self._perspectives_menu.AppendSeparator()
        self._perspectives_menu.Append(ID_FirstPerspective+0, "Default Startup")
        self._perspectives_menu.Append(ID_FirstPerspective+1, "All Panes")
        self._perspectives_menu.Append(ID_FirstPerspective + 2, "Minimum for DragAndDrop") #ran

        self._nb_perspectives_menu = wx.Menu()
        self._nb_perspectives_menu.Append(ID_CreateNBPerspective, "Create Perspective")
        self._nb_perspectives_menu.Append(ID_CopyNBPerspectiveCode, "Copy Perspective Data To Clipboard")
        self._nb_perspectives_menu.AppendSeparator()
        self._nb_perspectives_menu.Append(ID_FirstNBPerspective+0, "Default Startup")

        guides_menu = wx.Menu()
        guides_menu.AppendRadioItem(ID_StandardGuides, "Standard Docking Guides")
        guides_menu.AppendRadioItem(ID_AeroGuides, "Aero-Style Docking Guides")
        guides_menu.AppendRadioItem(ID_WhidbeyGuides, "Whidbey-Style Docking Guides")

        perspectives_menu.AppendMenu(wx.ID_ANY, "Frame Perspectives", self._perspectives_menu)
        perspectives_menu.AppendMenu(wx.ID_ANY, "AuiNotebook Perspectives", self._nb_perspectives_menu)
        perspectives_menu.AppendSeparator()
        perspectives_menu.AppendMenu(wx.ID_ANY, "Docking Guides", guides_menu)

        action_menu = wx.Menu()
        action_menu.AppendCheckItem(ID_VetoTree, "Veto Floating Of Tree Pane")
        action_menu.AppendCheckItem(ID_VetoText, "Veto Docking Of Fixed Pane")
        action_menu.AppendSeparator()

        attention_menu = wx.Menu()

        self._requestPanes = {}
        for indx, pane in enumerate(self._mgr.GetAllPanes()):
            if pane.IsToolbar():
                continue
            if not pane.caption or not pane.name:
                continue
            ids = wx.ID_HIGHEST + 12345 + indx
            self._requestPanes[ids] = pane.name
            attention_menu.Append(ids, pane.caption)

        action_menu.AppendMenu(wx.ID_ANY, "Request User Attention For", attention_menu)

        help_menu = wx.Menu()
        help_menu.Append(wx.ID_ABOUT, "About...")

        mb.Append(file_menu, "&File")
        mb.Append(view_menu, "&View")
        mb.Append(perspectives_menu, "&Perspectives")
        mb.Append(options_menu, "&Options")
        mb.Append(notebook_menu, "&Notebook")
        mb.Append(action_menu, "&Actions")
        mb.Append(help_menu, "&Help")

        self.SetMenuBar(mb)


    def BuildPanes(self):

        # min size for the frame itself isn't completely done.
        # see the end up AuiManager.Update() for the test
        # code. For now, just hard code a frame minimum size
        # self.SetMinSize(wx.Size(400, 300))
        self.SetMinSize(wx.Size(300, 150)) #ran

        # prepare a few custom overflow elements for the toolbars' overflow buttons

        prepend_items, append_items = [], []
        item = aui.AuiToolBarItem()

        item.SetKind(wx.ITEM_SEPARATOR)
        append_items.append(item)

        item = aui.AuiToolBarItem()
        item.SetKind(wx.ITEM_NORMAL)
        item.SetId(ID_CustomizeToolbar)
        item.SetLabel("Customize...")
        append_items.append(item)


        # create some toolbars
        tb1 = aui.AuiToolBar(self, -1, wx.DefaultPosition, wx.DefaultSize,
                             agwStyle=aui.AUI_TB_DEFAULT_STYLE | aui.AUI_TB_OVERFLOW)
        tb1.SetToolBitmapSize(wx.Size(48, 48))
        tb1.AddSimpleTool(ID_SampleItem+1, "Test", wx.ArtProvider.GetBitmap(wx.ART_ERROR))
        tb1.AddSeparator()
        tb1.AddSimpleTool(ID_SampleItem+2, "Test", wx.ArtProvider.GetBitmap(wx.ART_QUESTION))
        tb1.AddSimpleTool(ID_SampleItem+3, "Test", wx.ArtProvider.GetBitmap(wx.ART_INFORMATION))
        tb1.AddSimpleTool(ID_SampleItem+4, "Test", wx.ArtProvider.GetBitmap(wx.ART_WARNING))
        tb1.AddSimpleTool(ID_SampleItem+5, "Test", wx.ArtProvider.GetBitmap(wx.ART_MISSING_IMAGE))
        tb1.SetCustomOverflowItems(prepend_items, append_items)
        tb1.Realize()

        tb2 = aui.AuiToolBar(self, -1, wx.DefaultPosition, wx.DefaultSize,
                             agwStyle=aui.AUI_TB_DEFAULT_STYLE | aui.AUI_TB_OVERFLOW)
        tb2.SetToolBitmapSize(wx.Size(16, 16))

        tb2_bmp1 = wx.ArtProvider.GetBitmap(wx.ART_QUESTION, wx.ART_OTHER, wx.Size(16, 16))
        tb2.AddSimpleTool(ID_SampleItem+6, "Test", tb2_bmp1)
        tb2.AddSimpleTool(ID_SampleItem+7, "Test", tb2_bmp1)
        tb2.AddSimpleTool(ID_SampleItem+8, "Test", tb2_bmp1)
        tb2.AddSimpleTool(ID_SampleItem+9, "Test", tb2_bmp1)
        tb2.AddSeparator()
        tb2.AddSimpleTool(ID_SampleItem+10, "Test", tb2_bmp1)
        tb2.AddSimpleTool(ID_SampleItem+11, "Test", tb2_bmp1)
        tb2.AddSeparator()
        tb2.AddSimpleTool(ID_SampleItem+12, "Test", tb2_bmp1)
        tb2.AddSimpleTool(ID_SampleItem+13, "Test", tb2_bmp1)
        tb2.AddSimpleTool(ID_SampleItem+14, "Test", tb2_bmp1)
        tb2.AddSimpleTool(ID_SampleItem+15, "Test", tb2_bmp1)
        tb2.SetCustomOverflowItems(prepend_items, append_items)
        tb2.Realize()

        tb3 = aui.AuiToolBar(self, -1, wx.DefaultPosition, wx.DefaultSize,
                             agwStyle=aui.AUI_TB_DEFAULT_STYLE | aui.AUI_TB_OVERFLOW)
        tb3.SetToolBitmapSize(wx.Size(16, 16))
        tb3_bmp1 = wx.ArtProvider.GetBitmap(wx.ART_FOLDER, wx.ART_OTHER, wx.Size(16, 16))
        tb3.AddSimpleTool(ID_SampleItem+16, "Check 1", tb3_bmp1, "Check 1", aui.ITEM_CHECK)
        tb3.AddSimpleTool(ID_SampleItem+17, "Check 2", tb3_bmp1, "Check 2", aui.ITEM_CHECK)
        tb3.AddSimpleTool(ID_SampleItem+18, "Check 3", tb3_bmp1, "Check 3", aui.ITEM_CHECK)
        tb3.AddSimpleTool(ID_SampleItem+19, "Check 4", tb3_bmp1, "Check 4", aui.ITEM_CHECK)
        tb3.AddSeparator()
        tb3.AddSimpleTool(ID_SampleItem+20, "Radio 1", tb3_bmp1, "Radio 1", aui.ITEM_RADIO)
        tb3.AddSimpleTool(ID_SampleItem+21, "Radio 2", tb3_bmp1, "Radio 2", aui.ITEM_RADIO)
        tb3.AddSimpleTool(ID_SampleItem+22, "Radio 3", tb3_bmp1, "Radio 3", aui.ITEM_RADIO)
        tb3.AddSeparator()
        tb3.AddSimpleTool(ID_SampleItem+23, "Radio 1 (Group 2)", tb3_bmp1, "Radio 1 (Group 2)", aui.ITEM_RADIO)
        tb3.AddSimpleTool(ID_SampleItem+24, "Radio 2 (Group 2)", tb3_bmp1, "Radio 2 (Group 2)", aui.ITEM_RADIO)
        tb3.AddSimpleTool(ID_SampleItem+25, "Radio 3 (Group 2)", tb3_bmp1, "Radio 3 (Group 2)", aui.ITEM_RADIO)

        tb3.SetCustomOverflowItems(prepend_items, append_items)
        tb3.Realize()

        tb4 = aui.AuiToolBar(self, -1, wx.DefaultPosition, wx.DefaultSize,
                             agwStyle=aui.AUI_TB_OVERFLOW | aui.AUI_TB_TEXT | aui.AUI_TB_HORZ_TEXT)
        tb4.SetToolBitmapSize(wx.Size(16, 16))
        tb4_bmp1 = wx.ArtProvider.GetBitmap(wx.ART_NORMAL_FILE, wx.ART_OTHER, wx.Size(16, 16))
        tb4.AddSimpleTool(ID_DropDownToolbarItem, "Item 1", tb4_bmp1)
        tb4.AddSimpleTool(ID_SampleItem+23, "Item 2", tb4_bmp1)
        tb4.AddSimpleTool(ID_SampleItem+24, "Item 3", tb4_bmp1)
        tb4.AddSimpleTool(ID_SampleItem+25, "Item 4", tb4_bmp1)
        tb4.AddSeparator()
        tb4.AddSimpleTool(ID_SampleItem+26, "Item 5", tb4_bmp1)
        tb4.AddSimpleTool(ID_SampleItem+27, "Item 6", tb4_bmp1)
        tb4.AddSimpleTool(ID_SampleItem+28, "Item 7", tb4_bmp1)
        tb4.AddSimpleTool(ID_SampleItem+29, "Item 8", tb4_bmp1)

        choice = wx.Choice(tb4, -1, choices=["One choice", "Another choice"])
        tb4.AddControl(choice)

        tb4.SetToolDropDown(ID_DropDownToolbarItem, True)
        tb4.Realize()

        tb5 = aui.AuiToolBar(self, -1, wx.DefaultPosition, wx.DefaultSize,
                             agwStyle=aui.AUI_TB_OVERFLOW | aui.AUI_TB_VERTICAL)

        tb5.SetToolBitmapSize(wx.Size(48, 48))
        tb5.AddSimpleTool(ID_SampleItem+30, "Test", wx.ArtProvider.GetBitmap(wx.ART_ERROR))
        tb5.AddSeparator()
        tb5.AddSimpleTool(ID_SampleItem+31, "Test", wx.ArtProvider.GetBitmap(wx.ART_QUESTION))
        tb5.AddSimpleTool(ID_SampleItem+32, "Test", wx.ArtProvider.GetBitmap(wx.ART_INFORMATION))
        tb5.AddSimpleTool(ID_SampleItem+33, "Test", wx.ArtProvider.GetBitmap(wx.ART_WARNING))
        tb5.AddSimpleTool(ID_SampleItem+34, "Test", wx.ArtProvider.GetBitmap(wx.ART_MISSING_IMAGE))
        tb5.SetCustomOverflowItems(prepend_items, append_items)
        tb5.Realize()

        tb6 = aui.AuiToolBar(self, -1, wx.DefaultPosition, wx.DefaultSize,
                             agwStyle=aui.AUI_TB_OVERFLOW | aui.AUI_TB_VERT_TEXT)
        tb6.SetToolBitmapSize(wx.Size(48, 48))
        tb6.AddSimpleTool(ID_SampleItem+35, "Clockwise 1", wx.ArtProvider.GetBitmap(wx.ART_ERROR, wx.ART_OTHER, wx.Size(16, 16)))
        tb6.AddSeparator()
        tb6.AddSimpleTool(ID_SampleItem+36, "Clockwise 2", wx.ArtProvider.GetBitmap(wx.ART_QUESTION, wx.ART_OTHER, wx.Size(16, 16)))
        tb6.AddSimpleTool(ID_DropDownToolbarItem, "Clockwise 3", wx.ArtProvider.GetBitmap(wx.ART_WARNING, wx.ART_OTHER, wx.Size(16, 16)))
        tb6.SetCustomOverflowItems(prepend_items, append_items)
        tb6.SetToolDropDown(ID_DropDownToolbarItem, True)
        tb6.Realize()

        # add a bunch of panes

        self._mgr.AddPane(self.CreateRan_PanelCtrl(), aui.AuiPaneInfo().Name("RAN_name").Caption("RAN_caption").MaximizeButton(True))
        self._mgr.AddPane(self.CreateRan_TreeCtrl(), aui.AuiPaneInfo().Name("RAN_name2").Caption("RAN_caption2").MaximizeButton(True))

        self._mgr.AddPane(self.CreateSizeReportCtrl(), aui.AuiPaneInfo().
                          Name("test1").Caption("Pane Caption").Top().MinimizeButton(True))

        if 1==2:    # extra 6+3 SizeReportCtrl
            self._mgr.AddPane(self.CreateSizeReportCtrl(), aui.AuiPaneInfo().
                              Name("test2").Caption("Client Size Reporter").
                              Bottom().Position(1).CloseButton(True).MaximizeButton(True).
                              MinimizeButton(True).CaptionVisible(True, left=True))

            self._mgr.AddPane(self.CreateSizeReportCtrl(), aui.AuiPaneInfo().
                              Name("test3").Caption("Client Size Reporter").
                              Bottom().CloseButton(True).MaximizeButton(True).MinimizeButton(True).
                              CaptionVisible(True, left=True))

            self._mgr.AddPane(self.CreateSizeReportCtrl(), aui.AuiPaneInfo().
                              Name("test4").Caption("Pane Caption").Left())

            self._mgr.AddPane(self.CreateSizeReportCtrl(), aui.AuiPaneInfo().
                              Name("test5").Caption("No Close Button").Right().CloseButton(False))

            self._mgr.AddPane(self.CreateSizeReportCtrl(), aui.AuiPaneInfo().
                              Name("test6").Caption("Client Size Reporter").Right().Row(1).
                              CloseButton(True).MaximizeButton(True).MinimizeButton(True))

            self._mgr.AddPane(self.CreateSizeReportCtrl(), aui.AuiPaneInfo().
                              Name("test7").Caption("Client Size Reporter").Left().Layer(1).
                              CloseButton(True).MaximizeButton(True).MinimizeButton(True))

            self._mgr.AddPane(self.CreateSizeReportCtrl(), aui.AuiPaneInfo().
                              Name("test9").Caption("Min Size 200x100").
                              BestSize(wx.Size(200, 100)).MinSize(wx.Size(200, 100)).Bottom().Layer(1).
                              CloseButton(True).MaximizeButton(True).MinimizeButton(True))

            self._mgr.AddPane(self.CreateSizeReportCtrl(), aui.AuiPaneInfo().
                              Name("test11").Caption("Fixed Pane").
                              Bottom().Layer(1).Position(2).Fixed().MinimizeButton(True))

            self._mgr.AddPane(self.CreateSizeReportCtrl(), aui.AuiPaneInfo().Name("sizereport_content").
                              CenterPane().Hide().MinimizeButton(True))

        self._mgr.AddPane(self.CreateTreeCtrl(), aui.AuiPaneInfo().Name("test8").Caption("Tree Pane").
                          Left().Layer(1).Position(1).CloseButton(True).MaximizeButton(True).
                          MinimizeButton(True))


        self._mgr.AddPane(self.CreateTreeCtrl(), aui.AuiPaneInfo().
                          Name("autonotebook").Caption("Auto NB").
                          Bottom().Layer(1).Position(1).MinimizeButton(True))

        self._mgr.AddPane(self.CreateTreeCtrl(), aui.AuiPaneInfo().
                          Name("thirdauto").Caption("A Third Auto-NB Pane").
                          Bottom().MinimizeButton(True), target=self._mgr.GetPane("autonotebook"))  # ran note: using target creates tabs collection

        wnd10 = self.CreateTextCtrl("This pane will prompt the user before hiding.")
        self._mgr.AddPane(wnd10, aui.AuiPaneInfo().
                          Name("test10").Caption("Text Pane with Hide Prompt").
                          Bottom().MinimizeButton(True), target=self._mgr.GetPane("autonotebook"))


        self._mgr.AddPane(SettingsPanel(self,self), aui.AuiPaneInfo().
                          Name("settings").Caption("Dock Manager Settings").
                          Dockable(False).Float().Hide().MinimizeButton(True))

        # create some center panes

        if 1==2:    # hiden by default, shown later by replacing the NoteBook
            self._mgr.AddPane(self.CreateGrid(), aui.AuiPaneInfo().Name("grid_content").
                              CenterPane().Hide().MinimizeButton(True))

            self._mgr.AddPane(self.CreateTreeCtrl(), aui.AuiPaneInfo().Name("tree_content").
                              CenterPane().Hide().MinimizeButton(True))

            self._mgr.AddPane(self.CreateTextCtrl(), aui.AuiPaneInfo().Name("text_content").
                              CenterPane().Hide().MinimizeButton(True))

            self._mgr.AddPane(self.CreateHTMLCtrl(), aui.AuiPaneInfo().Name("html_content").
                              CenterPane().Hide().MinimizeButton(True))

        self._mgr.AddPane(self.CreateRan_DandDCtrl(), aui.AuiPaneInfo().Name("DandD_content").
                          CenterPane().Hide().MinimizeButton(True))

        self._mgr.AddPane(self.CreateNotebook(), aui.AuiPaneInfo().Name("notebook_content").
                          CenterPane().PaneBorder(False))

        # add the toolbars to the manager
        self._mgr.AddPane(tb4, aui.AuiPaneInfo().Name("tb4").Caption("Sample Bookmark Toolbar").
                          # ToolbarPane().Top().Row(2))
                          ToolbarPane().Top().Row(1))
        if 1==1:    #choosing toolbars to add
            # pass
            self._mgr.AddPane(tb1, aui.AuiPaneInfo().Name("tb1").Caption("Big Toolbar").
                              ToolbarPane().Top())

            self._mgr.AddPane(tb2, aui.AuiPaneInfo().Name("tb2").Caption("Toolbar 2").
                              ToolbarPane().Top().Row(1))

            self._mgr.AddPane(tb3, aui.AuiPaneInfo().Name("tb3").Caption("Toolbar 3").
                              ToolbarPane().Top().Row(1).Position(1))


            self._mgr.AddPane(tb5, aui.AuiPaneInfo().Name("tb5").Caption("Sample Vertical Toolbar").
                              ToolbarPane().Left().GripperTop())

            self._mgr.AddPane(tb6, aui.AuiPaneInfo().
                              Name("tb6").Caption("Sample Vertical Clockwise Rotated Toolbar").
                              ToolbarPane().Right().GripperTop().TopDockable(False).BottomDockable(False));

            self._mgr.AddPane(wx.Button(self, -1, "Test Button"),
                              aui.AuiPaneInfo().Name("tb7").ToolbarPane().Top().Row(2).Position(1))

        # Show how to add a control inside a tab
        notebook = self._mgr.GetPane("notebook_content").window
        # self.gauge = ProgressGauge(notebook, size=(55, 15))   #ran
        # notebook.AddControlToPage(4, self.gauge) #ran : it is annoying..

        self._main_notebook = notebook

        ''' perspective keeping '''
        # make some default perspectives
        perspective_all = self._mgr.SavePerspective()

        all_panes = self._mgr.GetAllPanes()
        for pane in all_panes:
            if not pane.IsToolbar():
                pane.Hide()
            else:   #ran added
                print pane.Hide()
                print " is toolbar "

        #ran:
        self._mgr.GetPane("DandD_content").Show()
        #:todo: set win size to min. set as external win.
        # get screen resolution

        print self
        print self.GetSize()
        print self.GetParent()
        print self.GetParent().GetSize()
        print self.GetParent().GetParent()
        print self.GetParent().GetParent().GetSize()

        print self
        print self.GetPosition()
        print self.GetParent()
        print self.GetParent().GetPosition()
        print self.GetParent().GetParent()
        print self.GetParent().GetParent().GetPosition()

        desiredFramePos = wx.Point(1200,100)
        desiredFramePos = wx.Point(683,384)
        previousSize = self.GetParent().GetParent().GetPosition()
        self.GetParent().GetParent().SetPosition(desiredFramePos)
        # self.pos = (700,900)

        desiredFrameSize = wx.Size(400  ,200)
        print self.GetParent().GetParent().SetSize(desiredFrameSize)
        print self.SetSize(desiredFrameSize)

        print self
        print self.GetPosition()
        print self.GetParent()
        print self.GetParent().GetPosition()
        print self.GetParent().GetParent()
        print self.GetParent().GetParent().GetPosition()

        # self.CenterOnScreen()
        #set size  , previousSize =
        # self.GetStartPosition()
        # self.GetParent().GetParent().SetSize(wx.Size(750, 150))
        w = wx.SystemSettings.GetMetric(wx.SYS_SCREEN_X)
        h = wx.SystemSettings.GetMetric(wx.SYS_SCREEN_Y)
        centerPos = (w / 2, h / 2)
        print "screen centerPos : " + str(centerPos[0]) + "," + str(centerPos[1])




        # "commit" all changes made to AuiManager
        self._mgr.Update()
        perspective_min = self._mgr.SavePerspective()  # ran note: consider using 'Config' class and 'LoadPerspective' method

        self._mgr.GetPane("DandD_content").Hide()
        # self._perspectives_menu.Append(ID_FirstPerspective + len(self._perspectives), "Minimum layout")
        # self._perspectives.append(perspective_min)
#        self.SetSize(previousSize)
    
        # manual display configurations:
        if 1==2:
            self._mgr.GetPane("tb1").Hide()
            self._mgr.GetPane("tb7").Hide()
        self._mgr.GetPane("tb4").Show() #ran

        self._mgr.GetPane("test8").Show().Left().Layer(0).Row(0).Position(0)
        self._mgr.GetPane("__notebook_%d"%self._mgr.GetPane("test10").notebook_id).Show().Bottom().Layer(0).Row(0).Position(0)
        self._mgr.GetPane("autonotebook").Show()
        self._mgr.GetPane("thirdauto").Show()
        self._mgr.GetPane("test10").Show()
        self._mgr.GetPane("notebook_content").Show()

        perspective_default = self._mgr.SavePerspective()   # ran note: consider using 'Config' class and 'LoadPerspective' method

        self._perspectives = []
        self._perspectives.append(perspective_default)
        self._perspectives.append(perspective_all)
        self._perspectives.append(perspective_min)  #ran

        self._nb_perspectives = []
        auibook = self._mgr.GetPane("notebook_content").window
        nb_perspective_default = auibook.SavePerspective()
        self._nb_perspectives.append(nb_perspective_default)

        self._mgr.LoadPerspective(perspective_default)  ##
        self._mgr.LoadPerspective(perspective_min)  ## ran
        ''''''''''''''''''''''''

        # Show how to get a custom minimizing behaviour, i.e., to minimize a pane
        # inside an existing AuiToolBar
        tree = self._mgr.GetPane("test8")
        tree.MinimizeMode(aui.AUI_MINIMIZE_POS_TOOLBAR)

        toolbarPane = self._mgr.GetPane(tb4)
        tree.MinimizeTarget(toolbarPane)

        # "commit" all changes made to AuiManager
        self._mgr.Update()


    def BindEvents(self):

        self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)
        self.Bind(wx.EVT_SIZE, self.OnSize)
        self.Bind(wx.EVT_MENU, self.OnCreateTree, id=ID_CreateTree)
        self.Bind(wx.EVT_MENU, self.OnCreateGrid, id=ID_CreateGrid)
        self.Bind(wx.EVT_MENU, self.OnCreateText, id=ID_CreateText)
        self.Bind(wx.EVT_MENU, self.OnCreateHTML, id=ID_CreateHTML)
        self.Bind(wx.EVT_MENU, self.OnCreateSizeReport, id=ID_CreateSizeReport)
        self.Bind(wx.EVT_MENU, self.OnCreateNotebook, id=ID_CreateNotebook)
##        self.Bind(wx.EVT_MENU, self.OnSwitchPane, id=ID_SwitchPane)
        self.Bind(wx.EVT_MENU, self.OnCreatePerspective, id=ID_CreatePerspective)
        self.Bind(wx.EVT_MENU, self.OnCopyPerspectiveCode, id=ID_CopyPerspectiveCode)
        self.Bind(wx.EVT_MENU, self.OnCreateNBPerspective, id=ID_CreateNBPerspective)
        self.Bind(wx.EVT_MENU, self.OnCopyNBPerspectiveCode, id=ID_CopyNBPerspectiveCode)
        self.Bind(wx.EVT_MENU, self.OnGuides, id=ID_StandardGuides)
        self.Bind(wx.EVT_MENU, self.OnGuides, id=ID_AeroGuides)
        self.Bind(wx.EVT_MENU, self.OnGuides, id=ID_WhidbeyGuides)
        self.Bind(wx.EVT_MENU, self.OnManagerFlag, id=ID_AllowFloating)
        self.Bind(wx.EVT_MENU, self.OnManagerFlag, id=ID_TransparentHint)
        self.Bind(wx.EVT_MENU, self.OnManagerFlag, id=ID_VenetianBlindsHint)
        self.Bind(wx.EVT_MENU, self.OnManagerFlag, id=ID_RectangleHint)
        self.Bind(wx.EVT_MENU, self.OnManagerFlag, id=ID_NoHint)
        self.Bind(wx.EVT_MENU, self.OnManagerFlag, id=ID_HintFade)
        self.Bind(wx.EVT_MENU, self.OnManagerFlag, id=ID_NoVenetianFade)
        self.Bind(wx.EVT_MENU, self.OnManagerFlag, id=ID_TransparentDrag)
        self.Bind(wx.EVT_MENU, self.OnManagerFlag, id=ID_LiveUpdate)
        self.Bind(wx.EVT_MENU, self.OnManagerFlag, id=ID_SmoothDocking)
        self.Bind(wx.EVT_MENU, self.OnManagerFlag, id=ID_NativeMiniframes)
        self.Bind(wx.EVT_MENU, self.OnMinimizePosition, id=ID_MinimizePosSmart)
        self.Bind(wx.EVT_MENU, self.OnMinimizePosition, id=ID_MinimizePosTop)
        self.Bind(wx.EVT_MENU, self.OnMinimizePosition, id=ID_MinimizePosLeft)
        self.Bind(wx.EVT_MENU, self.OnMinimizePosition, id=ID_MinimizePosRight)
        self.Bind(wx.EVT_MENU, self.OnMinimizePosition, id=ID_MinimizePosBottom)
        self.Bind(wx.EVT_MENU, self.OnMinimizeCaption, id=ID_MinimizeCaptSmart)
        self.Bind(wx.EVT_MENU, self.OnMinimizeCaption, id=ID_MinimizeCaptHorz)
        self.Bind(wx.EVT_MENU, self.OnMinimizeCaption, id=ID_MinimizeCaptHide)
        self.Bind(wx.EVT_MENU, self.OnManagerFlag, id=ID_AnimateFrames)
        self.Bind(wx.EVT_MENU, self.OnSetIconsOnPanes, id=ID_PaneIcons)
        self.Bind(wx.EVT_MENU, self.OnTransparentPane, id=ID_TransparentPane)
        self.Bind(wx.EVT_MENU, self.OnDockArt, id=ID_DefaultDockArt)
        self.Bind(wx.EVT_MENU, self.OnDockArt, id=ID_ModernDockArt)
        self.Bind(wx.EVT_MENU, self.OnSnapToScreen, id=ID_SnapToScreen)
        self.Bind(wx.EVT_MENU, self.OnSnapPanes, id=ID_SnapPanes)
        self.Bind(wx.EVT_MENU, self.OnFlyOut, id=ID_FlyOut)
        self.Bind(wx.EVT_MENU, self.OnCustomPaneButtons, id=ID_CustomPaneButtons)
        self.Bind(wx.EVT_MENU, self.OnManagerFlag, id=ID_AllowActivePane)
        self.Bind(wx.EVT_MENU, self.OnNotebookFlag, id=ID_NotebookTabFixedWidth)
        self.Bind(wx.EVT_MENU, self.OnNotebookFlag, id=ID_NotebookNoCloseButton)
        self.Bind(wx.EVT_MENU, self.OnNotebookFlag, id=ID_NotebookCloseButton)
        self.Bind(wx.EVT_MENU, self.OnNotebookFlag, id=ID_NotebookCloseButtonAll)
        self.Bind(wx.EVT_MENU, self.OnNotebookFlag, id=ID_NotebookCloseButtonActive)
        self.Bind(wx.EVT_MENU, self.OnNotebookFlag, id=ID_NotebookAllowTabMove)
        self.Bind(wx.EVT_MENU, self.OnNotebookFlag, id=ID_NotebookAllowTabExternalMove)
        self.Bind(wx.EVT_MENU, self.OnNotebookFlag, id=ID_NotebookAllowTabSplit)
        self.Bind(wx.EVT_MENU, self.OnNotebookFlag, id=ID_NotebookTabFloat)
        self.Bind(wx.EVT_MENU, self.OnNotebookFlag, id=ID_NotebookDclickUnsplit)
        self.Bind(wx.EVT_MENU, self.OnNotebookFlag, id=ID_NotebookTabDrawDnd)
        self.Bind(wx.EVT_MENU, self.OnNotebookFlag, id=ID_NotebookScrollButtons)
        self.Bind(wx.EVT_MENU, self.OnNotebookFlag, id=ID_NotebookWindowList)
        self.Bind(wx.EVT_MENU, self.OnNotebookFlag, id=ID_NotebookArtGloss)
        self.Bind(wx.EVT_MENU, self.OnNotebookFlag, id=ID_NotebookArtSimple)
        self.Bind(wx.EVT_MENU, self.OnNotebookFlag, id=ID_NotebookArtVC71)
        self.Bind(wx.EVT_MENU, self.OnNotebookFlag, id=ID_NotebookArtFF2)
        self.Bind(wx.EVT_MENU, self.OnNotebookFlag, id=ID_NotebookArtVC8)
        self.Bind(wx.EVT_MENU, self.OnNotebookFlag, id=ID_NotebookArtChrome)
        self.Bind(wx.EVT_MENU, self.OnNotebookFlag, id=ID_NotebookHideSingle)
        self.Bind(wx.EVT_MENU, self.OnNotebookFlag, id=ID_NotebookSmartTab)
        self.Bind(wx.EVT_MENU, self.OnNotebookFlag, id=ID_NotebookUseImagesDropDown)
        self.Bind(wx.EVT_MENU, self.OnNotebookFlag, id=ID_NotebookCloseOnLeft)
        self.Bind(wx.EVT_MENU, self.OnTabAlignment, id=ID_NotebookAlignTop)
        self.Bind(wx.EVT_MENU, self.OnTabAlignment, id=ID_NotebookAlignBottom)
        self.Bind(wx.EVT_MENU, self.OnCustomTabButtons, id=ID_NotebookCustomButtons)
        self.Bind(wx.EVT_MENU, self.OnMinMaxTabWidth, id=ID_NotebookMinMaxWidth)
        self.Bind(wx.EVT_MENU, self.OnPreview, id=ID_NotebookPreview)
        self.Bind(wx.EVT_MENU, self.OnAddMultiLine, id=ID_NotebookMultiLine)

        self.Bind(wx.EVT_MENU, self.OnGradient, id=ID_NoGradient)
        self.Bind(wx.EVT_MENU, self.OnGradient, id=ID_VerticalGradient)
        self.Bind(wx.EVT_MENU, self.OnGradient, id=ID_HorizontalGradient)
        self.Bind(wx.EVT_MENU, self.OnSettings, id=ID_Settings)
        self.Bind(wx.EVT_MENU, self.OnPreviewMinimized, id=ID_PreviewMinimized)
        self.Bind(wx.EVT_MENU, self.OnCustomizeToolbar, id=ID_CustomizeToolbar)
        self.Bind(wx.EVT_MENU, self.OnChangeContentPane, id=ID_GridContent)
        self.Bind(wx.EVT_MENU, self.OnChangeContentPane, id=ID_TreeContent)
        self.Bind(wx.EVT_MENU, self.OnChangeContentPane, id=ID_TextContent)
        self.Bind(wx.EVT_MENU, self.OnChangeContentPane, id=ID_SizeReportContent)
        self.Bind(wx.EVT_MENU, self.OnChangeContentPane, id=ID_HTMLContent)
        self.Bind(wx.EVT_MENU, self.OnChangeContentPane, id=ID_NotebookContent)

        self.Bind(wx.EVT_MENU, self.OnChangeContentPane, id=ID_RanDDContent) #ran

        self.Bind(wx.EVT_MENU, self.OnVetoTree, id=ID_VetoTree)
        self.Bind(wx.EVT_MENU, self.OnVetoText, id=ID_VetoText)

        for ids in self._requestPanes:
            self.Bind(wx.EVT_MENU, self.OnRequestUserAttention, id=ids)

        self.Bind(wx.EVT_CLOSE, self.onClose)
        self.Bind(wx.EVT_MENU, self.OnExit, id=wx.ID_EXIT)
        self.Bind(wx.EVT_MENU, self.OnAbout, id=wx.ID_ABOUT)

        self.Bind(wx.EVT_MENU_RANGE, self.OnRestorePerspective, id=ID_FirstPerspective,
                  id2=ID_FirstPerspective+1000)
        self.Bind(wx.EVT_MENU_RANGE, self.OnRestoreNBPerspective, id=ID_FirstNBPerspective,
                  id2=ID_FirstNBPerspective+1000)

        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_AllowFloating)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_TransparentHint)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_HintFade)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_TransparentDrag)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_NoGradient)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_VerticalGradient)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_HorizontalGradient)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_VenetianBlindsHint)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_RectangleHint)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_NoHint)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_NoVenetianFade)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_LiveUpdate)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_PaneIcons)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_AnimateFrames)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_DefaultDockArt)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_ModernDockArt)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_SnapPanes)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_FlyOut)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_CustomPaneButtons)

        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_NotebookTabFixedWidth)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_NotebookNoCloseButton)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_NotebookCloseButton)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_NotebookCloseButtonAll)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_NotebookCloseButtonActive)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_NotebookAllowTabMove)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_NotebookAllowTabExternalMove)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_NotebookAllowTabSplit)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_NotebookTabFloat)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_NotebookDclickUnsplit)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_NotebookTabDrawDnd)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_NotebookScrollButtons)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_NotebookWindowList)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_NotebookHideSingle)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_NotebookSmartTab)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_NotebookUseImagesDropDown)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_NotebookCustomButtons)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_VetoTree)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_VetoText)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_StandardGuides)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_AeroGuides)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_WhidbeyGuides)

        for ids in self._requestPanes:
            self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ids)

        self.Bind(aui.EVT_AUITOOLBAR_TOOL_DROPDOWN, self.OnDropDownToolbarItem, id=ID_DropDownToolbarItem)
        self.Bind(aui.EVT_AUI_PANE_CLOSE, self.OnPaneClose)
        self.Bind(aui.EVT_AUINOTEBOOK_ALLOW_DND, self.OnAllowNotebookDnD)
        self.Bind(aui.EVT_AUINOTEBOOK_PAGE_CLOSE, self.OnNotebookPageClose)

# ran removed those Alarm bindings
        # self.Bind(aui.EVT_AUI_PANE_FLOATING, self.OnFloatDock)
        # self.Bind(aui.EVT_AUI_PANE_FLOATED, self.OnFloatDock)
        # self.Bind(aui.EVT_AUI_PANE_DOCKING, self.OnFloatDock)
        # self.Bind(aui.EVT_AUI_PANE_DOCKED, self.OnFloatDock)

        self.Bind(wx.EVT_CLOSE, self.OnClose)

        self.Bind(wx.EVT_TIMER, self.TimerHandler)
        self.timer = wx.Timer(self)
        self.timer.Start(100)


    def __del__(self):

        self.timer.Stop()


    def OnClose(self, event):

        self.timer.Stop()
        self._mgr.UnInit()
        event.Skip()


    def TimerHandler(self, event):

        try:
            self.gauge.Pulse()
        except wx.PyDeadObjectError:
            print "TimerHandler event : wx.PyDeadObjectError exception "
            self.timer.Stop()
        except:
            print "TimerHandler event : no gauge.Pulse() object - stopping the timer"
            self.timer.Stop()


    def GetDockArt(self):

        return self._mgr.GetArtProvider()


    def DoUpdate(self):

        self._mgr.Update()
        self.Refresh()


    def OnEraseBackground(self, event):

        event.Skip()


    def OnSize(self, event):

        event.Skip()


    def OnSettings(self, event):

        # show the settings pane, and float it
        floating_pane = self._mgr.GetPane("settings").Float().Show()

        if floating_pane.floating_pos == wx.DefaultPosition:
            floating_pane.FloatingPosition(self.GetStartPosition())

        self._mgr.Update()


    def OnPreviewMinimized(self, event):

        checked = event.IsChecked()
        agwFlags = self._mgr.GetAGWFlags()

        if event.IsChecked():
            agwFlags ^= aui.AUI_MGR_PREVIEW_MINIMIZED_PANES
        else:
            agwFlags &= ~aui.AUI_MGR_PREVIEW_MINIMIZED_PANES

        self._mgr.SetAGWFlags(agwFlags)


    def OnSetIconsOnPanes(self, event):

        panes = self._mgr.GetAllPanes()
        checked = event.IsChecked()
        self._pane_icons = checked

        for pane in panes:
            if checked:
                randimage = random.randint(0, len(ArtIDs) - 1)
                bmp = wx.ArtProvider_GetBitmap(eval(ArtIDs[randimage]), wx.ART_OTHER, (16, 16))
            else:
                bmp = None

            pane.Icon(bmp)

        self._mgr.Update()


    def OnTransparentPane(self, event):

        dlg = wx.TextEntryDialog(self, "Enter a transparency value (0-255):", "Pane transparency")

        dlg.SetValue("%d"%self._transparency)
        if dlg.ShowModal() != wx.ID_OK:
            return

        transparency = int(dlg.GetValue())
        dlg.Destroy()
        try:
            transparency = int(transparency)
        except:
            dlg = wx.MessageDialog(self, 'Invalid transparency value. Transparency' \
                                   ' should be an integer between 0 and 255.',
                                   'Error',
                                   wx.OK | wx.ICON_ERROR)
            dlg.ShowModal()
            dlg.Destroy()
            return

        if transparency < 0 or transparency > 255:
            dlg = wx.MessageDialog(self, 'Invalid transparency value. Transparency' \
                                   ' should be an integer between 0 and 255.',
                                   'Error',
                                   wx.OK | wx.ICON_ERROR)
            dlg.ShowModal()
            dlg.Destroy()
            return

        self._transparency = transparency
        panes = self._mgr.GetAllPanes()
        for pane in panes:
            pane.Transparent(self._transparency)

        self._mgr.Update()


    def OnDockArt(self, event):

        if event.GetId() == ID_DefaultDockArt:
            self._mgr.SetArtProvider(aui.AuiDefaultDockArt())
        else:
            if self._mgr.CanUseModernDockArt():
                self._mgr.SetArtProvider(aui.ModernDockArt(self))

        self._mgr.Update()
        self.Refresh()


    def OnSnapToScreen(self, event):

        self._mgr.SnapToScreen(True, monitor=0, hAlign=wx.RIGHT, vAlign=wx.TOP)


    def OnSnapPanes(self, event):

        allPanes = self._mgr.GetAllPanes()

        if not self._snapped:
            self._captions = {}
            for pane in allPanes:
                self._captions[pane.name] = pane.caption

        toSnap = not self._snapped

        if toSnap:
            for pane in allPanes:
                if pane.IsToolbar() or isinstance(pane.window, aui.AuiNotebook):
                    continue

                snap = random.randint(0, 4)
                if snap == 0:
                    # Snap everywhere
                    pane.Caption(pane.caption + " (Snap Everywhere)")
                    pane.Snappable(True)
                elif snap == 1:
                    # Snap left
                    pane.Caption(pane.caption + " (Snap Left)")
                    pane.LeftSnappable(True)
                elif snap == 2:
                    # Snap right
                    pane.Caption(pane.caption + " (Snap Right)")
                    pane.RightSnappable(True)
                elif snap == 3:
                    # Snap top
                    pane.Caption(pane.caption + " (Snap Top)")
                    pane.TopSnappable(True)
                elif snap == 4:
                    # Snap bottom
                    pane.Caption(pane.caption + " (Snap Bottom)")
                    pane.BottomSnappable(True)

        else:

            for pane in allPanes:
                if pane.IsToolbar() or isinstance(pane.window, aui.AuiNotebook):
                    continue

                pane.Caption(self._captions[pane.name])
                pane.Snappable(False)

        self._snapped = toSnap
        self._mgr.Update()
        self.Refresh()


    def OnFlyOut(self, event):

        checked = event.IsChecked()
        pane = self._mgr.GetPane("test8")

        if checked:
            dlg = wx.MessageDialog(self, 'The tree pane will have fly-out' \
                                   ' behaviour when floating.',
                                   'Message',
                                   wx.OK | wx.ICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()
            pane.FlyOut(True)
        else:
            pane.FlyOut(False)

        self._mgr.Update()


    def OnCustomPaneButtons(self, event):

        self._custom_pane_buttons = checked = event.IsChecked()
        art = self._mgr.GetArtProvider()

        if not checked:
            art.SetDefaultPaneBitmaps(wx.Platform == "__WXMAC__")
        else:
            for bmp, button, active, maximize in CUSTOM_PANE_BITMAPS:
                art.SetCustomPaneBitmap(bmp.GetBitmap(), button, active, maximize)

        self._mgr.Update()
        self.Refresh()


    def OnCustomizeToolbar(self, event):

        wx.MessageBox("Customize Toolbar clicked", "AUI Test")


    def OnGradient(self, event):

        evId = event.GetId()
        if evId == ID_NoGradient:
            gradient = aui.AUI_GRADIENT_NONE
        elif evId == ID_VerticalGradient:
            gradient = aui.AUI_GRADIENT_VERTICAL
        elif evId == ID_HorizontalGradient:
            gradient = aui.AUI_GRADIENT_HORIZONTAL

        self._mgr.GetArtProvider().SetMetric(aui.AUI_DOCKART_GRADIENT_TYPE, gradient)
        self._mgr.Update()


    def OnManagerFlag(self, event):

        flag = 0
        evId = event.GetId()

        if evId in [ID_TransparentHint, ID_VenetianBlindsHint, ID_RectangleHint, ID_NoHint]:

            agwFlags = self._mgr.GetAGWFlags()
            agwFlags &= ~aui.AUI_MGR_TRANSPARENT_HINT
            agwFlags &= ~aui.AUI_MGR_VENETIAN_BLINDS_HINT
            agwFlags &= ~aui.AUI_MGR_RECTANGLE_HINT
            self._mgr.SetAGWFlags(agwFlags)

        if evId == ID_AllowFloating:
            flag = aui.AUI_MGR_ALLOW_FLOATING
        elif evId == ID_TransparentDrag:
            flag = aui.AUI_MGR_TRANSPARENT_DRAG
        elif evId == ID_HintFade:
            flag = aui.AUI_MGR_HINT_FADE
        elif evId == ID_NoVenetianFade:
            flag = aui.AUI_MGR_NO_VENETIAN_BLINDS_FADE
        elif evId == ID_AllowActivePane:
            flag = aui.AUI_MGR_ALLOW_ACTIVE_PANE
        elif evId == ID_TransparentHint:
            flag = aui.AUI_MGR_TRANSPARENT_HINT
        elif evId == ID_VenetianBlindsHint:
            flag = aui.AUI_MGR_VENETIAN_BLINDS_HINT
        elif evId == ID_RectangleHint:
            flag = aui.AUI_MGR_RECTANGLE_HINT
        elif evId == ID_LiveUpdate:
            flag = aui.AUI_MGR_LIVE_RESIZE
        elif evId == ID_AnimateFrames:
            flag = aui.AUI_MGR_ANIMATE_FRAMES
        elif evId == ID_SmoothDocking:
            flag = aui.AUI_MGR_SMOOTH_DOCKING
        elif evId == ID_NativeMiniframes:
            flag = aui.AUI_MGR_USE_NATIVE_MINIFRAMES

        if flag:
            self._mgr.SetAGWFlags(self._mgr.GetAGWFlags() ^ flag)

        self._mgr.Update()


    def OnMinimizePosition(self, event):

        minize_mode = 0
        evId = event.GetId()

        if evId == ID_MinimizePosSmart:
            minize_mode |= aui.AUI_MINIMIZE_POS_SMART
        elif evId == ID_MinimizePosTop:
            minize_mode |= aui.AUI_MINIMIZE_POS_TOP
        elif evId == ID_MinimizePosLeft:
            minize_mode |= aui.AUI_MINIMIZE_POS_LEFT
        elif evId == ID_MinimizePosRight:
            minize_mode |= aui.AUI_MINIMIZE_POS_RIGHT
        elif evId == ID_MinimizePosBottom:
            minize_mode |= aui.AUI_MINIMIZE_POS_BOTTOM

        all_panes = self._mgr.GetAllPanes()
        for pane in all_panes:
            if pane.name != "test8":
                pane.MinimizeMode(minize_mode | (pane.GetMinimizeMode() & aui.AUI_MINIMIZE_CAPT_MASK))


    def OnMinimizeCaption(self, event):

        minize_mode = 0
        evId = event.GetId()

        if evId == ID_MinimizeCaptSmart:
            minize_mode |= aui.AUI_MINIMIZE_CAPT_SMART
        elif evId == ID_MinimizeCaptHorz:
            minize_mode |= aui.AUI_MINIMIZE_CAPT_HORZ
        elif evId == ID_MinimizeCaptHide:
            minize_mode |= aui.AUI_MINIMIZE_CAPT_HIDE

        all_panes = self._mgr.GetAllPanes()
        for pane in all_panes:
            pane.MinimizeMode(minize_mode | (pane.GetMinimizeMode() & aui.AUI_MINIMIZE_POS_MASK))


    def OnNotebookFlag(self, event):

        evId = event.GetId()
        unsplit = None

        if evId in [ID_NotebookNoCloseButton, ID_NotebookCloseButton, ID_NotebookCloseButtonAll, \
                    ID_NotebookCloseButtonActive]:

            self._notebook_style &= ~(aui.AUI_NB_CLOSE_BUTTON |
                                      aui.AUI_NB_CLOSE_ON_ACTIVE_TAB |
                                      aui.AUI_NB_CLOSE_ON_ALL_TABS)

            if evId == ID_NotebookCloseButton:
                self._notebook_style ^= aui.AUI_NB_CLOSE_BUTTON
            elif evId == ID_NotebookCloseButtonAll:
                self._notebook_style ^= aui.AUI_NB_CLOSE_ON_ALL_TABS
            elif evId == ID_NotebookCloseButtonActive:
                self._notebook_style ^= aui.AUI_NB_CLOSE_ON_ACTIVE_TAB

        if evId == ID_NotebookAllowTabMove:
            self._notebook_style ^= aui.AUI_NB_TAB_MOVE

        if evId == ID_NotebookAllowTabExternalMove:
            self._notebook_style ^= aui.AUI_NB_TAB_EXTERNAL_MOVE

        elif evId == ID_NotebookAllowTabSplit:
            self._notebook_style ^= aui.AUI_NB_TAB_SPLIT

        elif evId == ID_NotebookTabFloat:
            self._notebook_style ^= aui.AUI_NB_TAB_FLOAT

        elif evId == ID_NotebookTabDrawDnd:
            self._notebook_style ^= aui.AUI_NB_DRAW_DND_TAB

        elif evId == ID_NotebookWindowList:
            self._notebook_style ^= aui.AUI_NB_WINDOWLIST_BUTTON

        elif evId == ID_NotebookScrollButtons:
            self._notebook_style ^= aui.AUI_NB_SCROLL_BUTTONS

        elif evId == ID_NotebookTabFixedWidth:
            self._notebook_style ^= aui.AUI_NB_TAB_FIXED_WIDTH

        elif evId == ID_NotebookHideSingle:
            self._notebook_style ^= aui.AUI_NB_HIDE_ON_SINGLE_TAB

        elif evId == ID_NotebookSmartTab:
            self._notebook_style ^= aui.AUI_NB_SMART_TABS

        elif evId == ID_NotebookUseImagesDropDown:
            self._notebook_style ^= aui.AUI_NB_USE_IMAGES_DROPDOWN

        elif evId == ID_NotebookCloseOnLeft:
            self._notebook_style ^= aui.AUI_NB_CLOSE_ON_TAB_LEFT

        all_panes = self._mgr.GetAllPanes()

        for pane in all_panes:

            if isinstance(pane.window, aui.AuiNotebook):
                nb = pane.window

                if evId == ID_NotebookArtGloss:

                    nb.SetArtProvider(aui.AuiDefaultTabArt())
                    self._notebook_theme = 0

                elif evId == ID_NotebookArtSimple:
                    nb.SetArtProvider(aui.AuiSimpleTabArt())
                    self._notebook_theme = 1

                elif evId == ID_NotebookArtVC71:
                    nb.SetArtProvider(aui.VC71TabArt())
                    self._notebook_theme = 2

                elif evId == ID_NotebookArtFF2:
                    nb.SetArtProvider(aui.FF2TabArt())
                    self._notebook_theme = 3

                elif evId == ID_NotebookArtVC8:
                    nb.SetArtProvider(aui.VC8TabArt())
                    self._notebook_theme = 4

                elif evId == ID_NotebookArtChrome:
                    nb.SetArtProvider(aui.ChromeTabArt())
                    self._notebook_theme = 5

                if nb.GetAGWWindowStyleFlag() & aui.AUI_NB_BOTTOM == 0:
                    nb.SetAGWWindowStyleFlag(self._notebook_style)

                if evId == ID_NotebookCloseButtonAll:
                    # Demonstrate how to remove a close button from a tab
                    nb.SetCloseButton(2, False)
                elif evId == ID_NotebookDclickUnsplit:
                    nb.SetSashDClickUnsplit(event.IsChecked())

                nb.Refresh()
                nb.Update()


    def OnUpdateUI(self, event):

        agwFlags = self._mgr.GetAGWFlags()
        evId = event.GetId()

        if evId == ID_NoGradient:
            event.Check(self._mgr.GetArtProvider().GetMetric(aui.AUI_DOCKART_GRADIENT_TYPE) == aui.AUI_GRADIENT_NONE)

        elif evId == ID_VerticalGradient:
            event.Check(self._mgr.GetArtProvider().GetMetric(aui.AUI_DOCKART_GRADIENT_TYPE) == aui.AUI_GRADIENT_VERTICAL)

        elif evId == ID_HorizontalGradient:
            event.Check(self._mgr.GetArtProvider().GetMetric(aui.AUI_DOCKART_GRADIENT_TYPE) == aui.AUI_GRADIENT_HORIZONTAL)

        elif evId == ID_AllowFloating:
            event.Check((agwFlags & aui.AUI_MGR_ALLOW_FLOATING) != 0)

        elif evId == ID_TransparentDrag:
            event.Check((agwFlags & aui.AUI_MGR_TRANSPARENT_DRAG) != 0)

        elif evId == ID_TransparentHint:
            event.Check((agwFlags & aui.AUI_MGR_TRANSPARENT_HINT) != 0)

        elif evId == ID_LiveUpdate:
            event.Check(aui.AuiManager_HasLiveResize(self._mgr))

        elif evId == ID_VenetianBlindsHint:
            event.Check((agwFlags & aui.AUI_MGR_VENETIAN_BLINDS_HINT) != 0)

        elif evId == ID_RectangleHint:
            event.Check((agwFlags & aui.AUI_MGR_RECTANGLE_HINT) != 0)

        elif evId == ID_NoHint:
            event.Check(((aui.AUI_MGR_TRANSPARENT_HINT |
                              aui.AUI_MGR_VENETIAN_BLINDS_HINT |
                              aui.AUI_MGR_RECTANGLE_HINT) & agwFlags) == 0)

        elif evId == ID_HintFade:
            event.Check((agwFlags & aui.AUI_MGR_HINT_FADE) != 0)

        elif evId == ID_NoVenetianFade:
            event.Check((agwFlags & aui.AUI_MGR_NO_VENETIAN_BLINDS_FADE) != 0)

        elif evId == ID_NativeMiniframes:
            event.Check(aui.AuiManager_UseNativeMiniframes(self._mgr))

        elif evId == ID_PaneIcons:
            event.Check(self._pane_icons)

        elif evId == ID_SmoothDocking:
            event.Check((agwFlags & aui.AUI_MGR_SMOOTH_DOCKING) != 0)

        elif evId == ID_AnimateFrames:
            event.Check((agwFlags & aui.AUI_MGR_ANIMATE_FRAMES) != 0)

        elif evId == ID_DefaultDockArt:
            event.Check(isinstance(self._mgr.GetArtProvider(), aui.AuiDefaultDockArt))

        elif evId == ID_ModernDockArt:
            event.Check(isinstance(self._mgr.GetArtProvider(), aui.ModernDockArt))

        elif evId == ID_SnapPanes:
            event.Check(self._snapped)

        elif evId == ID_FlyOut:
            pane = self._mgr.GetPane("test8")
            event.Check(pane.IsFlyOut())

        elif evId == ID_AeroGuides:
            event.Check(agwFlags & aui.AUI_MGR_AERO_DOCKING_GUIDES != 0)

        elif evId == ID_WhidbeyGuides:
            event.Check(agwFlags & aui.AUI_MGR_WHIDBEY_DOCKING_GUIDES != 0)

        elif evId == ID_StandardGuides:
            event.Check((agwFlags & aui.AUI_MGR_AERO_DOCKING_GUIDES == 0) and (agwFlags & aui.AUI_MGR_WHIDBEY_DOCKING_GUIDES == 0))

        elif evId == ID_CustomPaneButtons:
            event.Check(self._custom_pane_buttons)

        elif evId == ID_PreviewMinimized:
            event.Check(agwFlags & aui.AUI_MGR_PREVIEW_MINIMIZED_PANES)

        elif evId == ID_NotebookNoCloseButton:
            event.Check((self._notebook_style & (aui.AUI_NB_CLOSE_BUTTON|aui.AUI_NB_CLOSE_ON_ALL_TABS|aui.AUI_NB_CLOSE_ON_ACTIVE_TAB)) != 0)

        elif evId == ID_NotebookCloseButton:
            event.Check((self._notebook_style & aui.AUI_NB_CLOSE_BUTTON) != 0)

        elif evId == ID_NotebookCloseButtonAll:
            event.Check((self._notebook_style & aui.AUI_NB_CLOSE_ON_ALL_TABS) != 0)

        elif evId == ID_NotebookCloseButtonActive:
            event.Check((self._notebook_style & aui.AUI_NB_CLOSE_ON_ACTIVE_TAB) != 0)

        elif evId == ID_NotebookAllowTabSplit:
            event.Check((self._notebook_style & aui.AUI_NB_TAB_SPLIT) != 0)

        elif evId == ID_NotebookTabFloat:
            event.Check((self._notebook_style & aui.AUI_NB_TAB_FLOAT) != 0)

        elif evId == ID_NotebookDclickUnsplit:
            event.Check(self._main_notebook.GetSashDClickUnsplit())

        elif evId == ID_NotebookTabDrawDnd:
            event.Check((self._notebook_style & aui.AUI_NB_DRAW_DND_TAB) != 0)

        elif evId == ID_NotebookAllowTabMove:
            event.Check((self._notebook_style & aui.AUI_NB_TAB_MOVE) != 0)

        elif evId == ID_NotebookAllowTabExternalMove:
            event.Check((self._notebook_style & aui.AUI_NB_TAB_EXTERNAL_MOVE) != 0)

        elif evId == ID_NotebookScrollButtons:
            event.Check((self._notebook_style & aui.AUI_NB_SCROLL_BUTTONS) != 0)

        elif evId == ID_NotebookWindowList:
            event.Check((self._notebook_style & aui.AUI_NB_WINDOWLIST_BUTTON) != 0)

        elif evId == ID_NotebookTabFixedWidth:
            event.Check((self._notebook_style & aui.AUI_NB_TAB_FIXED_WIDTH) != 0)

        elif evId == ID_NotebookHideSingle:
            event.Check((self._notebook_style & aui.AUI_NB_HIDE_ON_SINGLE_TAB) != 0)

        elif evId == ID_NotebookSmartTab:
            event.Check((self._notebook_style & aui.AUI_NB_SMART_TABS) != 0)

        elif evId == ID_NotebookUseImagesDropDown:
            event.Check((self._notebook_style & aui.AUI_NB_USE_IMAGES_DROPDOWN) != 0)

        elif evId == ID_NotebookCloseOnLeft:
            event.Check((self._notebook_style & aui.AUI_NB_CLOSE_ON_TAB_LEFT) != 0)

        elif evId == ID_NotebookCustomButtons:
            event.Check(self._custom_tab_buttons)

        elif evId == ID_NotebookArtGloss:
            event.Check(self._notebook_theme == 0)

        elif evId == ID_NotebookArtSimple:
            event.Check(self._notebook_theme == 1)

        elif evId == ID_NotebookArtVC71:
            event.Check(self._notebook_theme == 2)

        elif evId == ID_NotebookArtFF2:
            event.Check(self._notebook_theme == 3)

        elif evId == ID_NotebookArtVC8:
            event.Check(self._notebook_theme == 4)

        elif evId == ID_NotebookArtChrome:
            event.Check(self._notebook_theme == 5)

        elif evId == ID_VetoTree:
            event.Check(self._veto_tree)

        elif evId == ID_VetoText:
            event.Check(self._veto_text)

        else:
            for ids in self._requestPanes:
                if evId == ids:
                    paneName = self._requestPanes[ids]
                    pane = self._mgr.GetPane(paneName)
                    event.Enable(pane.IsShown())


    def OnPaneClose(self, event):

        if event.pane.name == "test10":

            msg = "Are you sure you want to "
            if event.GetEventType() == aui.wxEVT_AUI_PANE_MINIMIZE:
                msg += "minimize "
            else:
                msg += "close/hide "

            res = wx.MessageBox(msg + "this pane?", "AUI", wx.YES_NO, self)
            if res != wx.YES:
                event.Veto()


    def OnCreatePerspective(self, event):

        dlg = wx.TextEntryDialog(self, "Enter a name for the new perspective:", "AUI Test")

        dlg.SetValue("Perspective %u"%(len(self._perspectives) + 1))
        if dlg.ShowModal() != wx.ID_OK:
            return

        if len(self._perspectives) == 0:
            self._perspectives_menu.AppendSeparator()

        self._perspectives_menu.Append(ID_FirstPerspective + len(self._perspectives), dlg.GetValue())
        self._perspectives.append(self._mgr.SavePerspective())


    def OnCopyPerspectiveCode(self, event):

        s = self._mgr.SavePerspective()

        if wx.TheClipboard.Open():

            wx.TheClipboard.SetData(wx.TextDataObject(s))
            wx.TheClipboard.Close()


    def OnRestorePerspective(self, event):

        self._mgr.LoadPerspective(self._perspectives[event.GetId() - ID_FirstPerspective])


    def OnCreateNBPerspective(self, event):

        dlg = wx.TextEntryDialog(self, "Enter a name for the new perspective:", "AUI Test")

        dlg.SetValue("Perspective %u"%(len(self._nb_perspectives) + 1))
        if dlg.ShowModal() != wx.ID_OK:
            return

        if len(self._nb_perspectives) == 0:
            self._nb_perspectives_menu.AppendSeparator()

        auibook = self._mgr.GetPane("notebook_content").window
        self._nb_perspectives_menu.Append(ID_FirstNBPerspective + len(self._nb_perspectives), dlg.GetValue())
        self._nb_perspectives.append(auibook.SavePerspective())


    def OnCopyNBPerspectiveCode(self, event):

        auibook = self._mgr.GetPane("notebook_content").window
        s = auibook.SavePerspective()

        if wx.TheClipboard.Open():

            wx.TheClipboard.SetData(wx.TextDataObject(s))
            wx.TheClipboard.Close()


    def OnRestoreNBPerspective(self, event):

        auibook = self._mgr.GetPane("notebook_content").window
        auibook.LoadPerspective(self._nb_perspectives[event.GetId() - ID_FirstNBPerspective])

        self.gauge = ProgressGauge(auibook, size=(55, 15))
        auibook.AddControlToPage(4, self.gauge)


    def OnGuides(self, event):

        useAero = event.GetId() == ID_AeroGuides
        useWhidbey = event.GetId() == ID_WhidbeyGuides
        agwFlags = self._mgr.GetAGWFlags()

        if useAero:
            agwFlags ^= aui.AUI_MGR_AERO_DOCKING_GUIDES
            agwFlags &= ~aui.AUI_MGR_WHIDBEY_DOCKING_GUIDES
        elif useWhidbey:
            agwFlags ^= aui.AUI_MGR_WHIDBEY_DOCKING_GUIDES
            agwFlags &= ~aui.AUI_MGR_AERO_DOCKING_GUIDES
        else:
            agwFlags &= ~aui.AUI_MGR_AERO_DOCKING_GUIDES
            agwFlags &= ~aui.AUI_MGR_WHIDBEY_DOCKING_GUIDES

        self._mgr.SetAGWFlags(agwFlags)


    def OnNotebookPageClose(self, event):

        ctrl = event.GetEventObject()
        if isinstance(ctrl.GetPage(event.GetSelection()), wx.html.HtmlWindow):

            res = wx.MessageBox("Are you sure you want to close/hide this notebook page?",
                                "AUI", wx.YES_NO, self)
            if res != wx.YES:
                event.Veto()


    def OnAllowNotebookDnD(self, event):

        # for the purpose of this test application, explicitly
        # allow all noteboko drag and drop events
        event.Allow()


    def GetStartPosition(self):

        x = 20
        pt = self.ClientToScreen(wx.Point(0, 0))
        return wx.Point(pt.x + x, pt.y + x)


    def OnCreateTree(self, event):

        self._mgr.AddPane(self.CreateTreeCtrl(), aui.AuiPaneInfo().
                          Caption("Tree Control").
                          Float().FloatingPosition(self.GetStartPosition()).
                          FloatingSize(wx.Size(150, 300)).MinimizeButton(True))
        self._mgr.Update()


    def OnCreateGrid(self, event):

        self._mgr.AddPane(self.CreateGrid(), aui.AuiPaneInfo().
                          Caption("Grid").
                          Float().FloatingPosition(self.GetStartPosition()).
                          FloatingSize(wx.Size(300, 200)).MinimizeButton(True))
        self._mgr.Update()


    def OnCreateHTML(self, event):

        self._mgr.AddPane(self.CreateHTMLCtrl(), aui.AuiPaneInfo().
                          Caption("HTML Control").
                          Float().FloatingPosition(self.GetStartPosition()).
                          FloatingSize(wx.Size(300, 200)).MinimizeButton(True))
        self._mgr.Update()


    def OnCreateNotebook(self, event):

        self._mgr.AddPane(self.CreateNotebook(), aui.AuiPaneInfo().
                          Caption("Notebook").
                          Float().FloatingPosition(self.GetStartPosition()).
                          CloseButton(True).MaximizeButton(True).MinimizeButton(True))
        self._mgr.Update()


    def OnCreateText(self, event):

        self._mgr.AddPane(self.CreateTextCtrl(), aui.AuiPaneInfo().
                          Caption("Text Control").
                          Float().FloatingPosition(self.GetStartPosition()).
                          MinimizeButton(True))
        self._mgr.Update()


    def OnCreateSizeReport(self, event):

        self._mgr.AddPane(self.CreateSizeReportCtrl(), aui.AuiPaneInfo().
                          Caption("Client Size Reporter").
                          Float().FloatingPosition(self.GetStartPosition()).
                          CloseButton(True).MaximizeButton(True).MinimizeButton(True))
        self._mgr.Update()


    def OnChangeContentPane(self, event):

        self._mgr.GetPane("grid_content").Show(event.GetId() == ID_GridContent)
        self._mgr.GetPane("text_content").Show(event.GetId() == ID_TextContent)
        self._mgr.GetPane("tree_content").Show(event.GetId() == ID_TreeContent)
        self._mgr.GetPane("sizereport_content").Show(event.GetId() == ID_SizeReportContent)
        self._mgr.GetPane("html_content").Show(event.GetId() == ID_HTMLContent)
        self._mgr.GetPane("notebook_content").Show(event.GetId() == ID_NotebookContent)
        self._mgr.GetPane("DandD_content").Show(event.GetId() == ID_RanDDContent)   #ran
        self._mgr.Update()


    def OnVetoTree(self, event):

        self._veto_tree = event.IsChecked()


    def OnVetoText(self, event):

        self._veto_text = event.IsChecked()


    def OnRequestUserAttention(self, event):

        ids = event.GetId()
        if ids not in self._requestPanes:
            return

        paneName = self._requestPanes[ids]
        pane = self._mgr.GetPane(paneName)
        self._mgr.RequestUserAttention(pane.window)


    def OnDropDownToolbarItem(self, event):

        if event.IsDropDownClicked():

            tb = event.GetEventObject()
            tb.SetToolSticky(event.GetId(), True)

            # create the popup menu
            menuPopup = wx.Menu()
            bmp = wx.ArtProvider.GetBitmap(wx.ART_QUESTION, wx.ART_OTHER, wx.Size(16, 16))

            m1 =  wx.MenuItem(menuPopup, 10001, "Drop Down Item 1")
            m1.SetBitmap(bmp)
            menuPopup.AppendItem(m1)

            m2 =  wx.MenuItem(menuPopup, 10002, "Drop Down Item 2")
            m2.SetBitmap(bmp)
            menuPopup.AppendItem(m2)

            m3 =  wx.MenuItem(menuPopup, 10003, "Drop Down Item 3")
            m3.SetBitmap(bmp)
            menuPopup.AppendItem(m3)

            m4 =  wx.MenuItem(menuPopup, 10004, "Drop Down Item 4")
            m4.SetBitmap(bmp)
            menuPopup.AppendItem(m4)

            # line up our menu with the button
            rect = tb.GetToolRect(event.GetId())
            pt = tb.ClientToScreen(rect.GetBottomLeft())
            pt = self.ScreenToClient(pt)

            self.PopupMenu(menuPopup, pt)

            # make sure the button is "un-stuck"
            tb.SetToolSticky(event.GetId(), False)


    def OnTabAlignment(self, event):

        for pane in self._mgr.GetAllPanes():

            if isinstance(pane.window, aui.AuiNotebook):

                nb = pane.window
                style = nb.GetAGWWindowStyleFlag()

                if event.GetId() == ID_NotebookAlignTop:
                    style &= ~aui.AUI_NB_BOTTOM
                    style ^= aui.AUI_NB_TOP
                    nb.SetAGWWindowStyleFlag(style)
                elif event.GetId() == ID_NotebookAlignBottom:
                    style &= ~aui.AUI_NB_TOP
                    style ^= aui.AUI_NB_BOTTOM
                    nb.SetAGWWindowStyleFlag(style)

                self._notebook_style = style
                nb.Update()
                nb.Refresh()


    def OnCustomTabButtons(self, event):

        checked = event.IsChecked()
        self._custom_tab_buttons = checked
        auibook = self._mgr.GetPane("notebook_content").window

        left = CUSTOM_TAB_BUTTONS["Left"]
        for btn, ids in left:
            if checked:
                auibook.AddTabAreaButton(ids, wx.LEFT, btn.GetBitmap())
            else:
                auibook.RemoveTabAreaButton(ids)

        right = CUSTOM_TAB_BUTTONS["Right"]
        for btn, ids in right:
            if checked:
                auibook.AddTabAreaButton(ids, wx.RIGHT, btn.GetBitmap())
            else:
                auibook.RemoveTabAreaButton(ids)

        auibook.Refresh()
        auibook.Update()


    def OnMinMaxTabWidth(self, event):

        auibook = self._mgr.GetPane("notebook_content").window
        minTabWidth, maxTabWidth = auibook.GetMinMaxTabWidth()

        dlg = wx.TextEntryDialog(self, "Enter the minimum and maximum tab widths, separated by a comma:",
                                 "AuiNotebook Tab Widths")

        dlg.SetValue("%d,%d"%(minTabWidth, maxTabWidth))
        if dlg.ShowModal() != wx.ID_OK:
            return

        value = dlg.GetValue()
        dlg.Destroy()

        try:
            minTabWidth, maxTabWidth = value.split(",")
            minTabWidth, maxTabWidth = int(minTabWidth), int(maxTabWidth)
        except:
            dlg = wx.MessageDialog(self, 'Invalid minimum/maximum tab width. Tab widths should be' \
                                   ' 2 integers separated by a comma.',
                                   'Error',
                                   wx.OK | wx.ICON_ERROR)
            dlg.ShowModal()
            dlg.Destroy()
            return

        if minTabWidth > maxTabWidth:
            dlg = wx.MessageDialog(self, 'Invalid minimum/maximum tab width. Minimum tab width' \
                                   ' should be less of equal than maximum tab width.',
                                   'Error',
                                   wx.OK | wx.ICON_ERROR)
            dlg.ShowModal()
            dlg.Destroy()
            return

        auibook.SetMinMaxTabWidth(minTabWidth, maxTabWidth)
        auibook.Refresh()
        auibook.Update()


    def OnPreview(self, event):

        auibook = self._mgr.GetPane("notebook_content").window
        auibook.NotebookPreview()


    def OnAddMultiLine(self, event):

        auibook = self._mgr.GetPane("notebook_content").window

        auibook.InsertPage(1, wx.TextCtrl(auibook, -1, "Some more text", wx.DefaultPosition, wx.DefaultSize,
                                          wx.TE_MULTILINE|wx.NO_BORDER), "Multi-Line\nTab Labels", True)

        auibook.SetPageTextColour(1, wx.BLUE)


    def OnFloatDock(self, event):

        paneLabel = event.pane.caption
        etype = event.GetEventType()

        strs = "Pane %s "%paneLabel
        if etype == aui.wxEVT_AUI_PANE_FLOATING:
            strs += "is about to be floated"

            if event.pane.name == "test8" and self._veto_tree:
                event.Veto()
                strs += "... Event vetoed by user selection!"
                self.log.write(strs + "\n")
                return

        elif etype == aui.wxEVT_AUI_PANE_FLOATED:
            strs += "has been floated"
        elif etype == aui.wxEVT_AUI_PANE_DOCKING:
            strs += "is about to be docked"

            if event.pane.name == "test11" and self._veto_text:
                event.Veto()
                strs += "... Event vetoed by user selection!"
                self.log.write(strs + "\n")
                return

        elif etype == aui.wxEVT_AUI_PANE_DOCKED:
            strs += "has been docked"

        self.log.write(strs + "\n")


    def OnExit(self, event):

        self.Close(True)

    def onClose(self, evt):
        """
        Destroy the taskbar icon and the frame
        """
        # ran
        prnt = self.GetParent()
        prnt2 = prnt.GetParent()    # 2 parents , because I know the creation of this 'self' was with panel parent and frame parent
        # self.DestroyChildren()
        # self.Destroy()
        prnt2.Close(True)
        prnt2.Destroy()
        pass

    def OnAbout(self, event):

        msg = "This Is The About Dialog Of The Pure Python Version Of AUI.\n\n" + \
              "Author: Andrea Gavana @ 23 Dec 2005\n\n" + \
              "Please Report Any Bug/Requests Of Improvements\n" + \
              "To Me At The Following Adresses:\n\n" + \
              "andrea.gavana@maerskoil.com\n" + "andrea.gavana@gmail.com\n\n" + \
              "Welcome To wxPython " + wx.VERSION_STRING + "!!"

        dlg = wx.MessageDialog(self, msg, "AUI Demo",
                               wx.OK | wx.ICON_INFORMATION)

        if wx.Platform != '__WXMAC__':
            try:
                dlg.SetFont(wx.Font(8, wx.NORMAL, wx.NORMAL, wx.NORMAL, False))
            except: #ran
                pass

        dlg.ShowModal()
        dlg.Destroy()


    def CreateTextCtrl(self, ctrl_text=""):

        if ctrl_text.strip():
            text = ctrl_text
        else:
            text = "This is text box %d"%self._textCount
            self._textCount += 1

        return wx.TextCtrl(self,-1, text, wx.Point(0, 0), wx.Size(150, 90),
                           wx.NO_BORDER | wx.TE_MULTILINE)


    def CreateGrid(self):

        grid = wx.grid.Grid(self, -1, wx.Point(0, 0), wx.Size(150, 250),
                            wx.NO_BORDER | wx.WANTS_CHARS)
        grid.CreateGrid(50, 20)
        return grid


    def CreateTreeCtrl(self):

        tree = wx.TreeCtrl(self, -1, wx.Point(0, 0), wx.Size(160, 250),
                           wx.TR_DEFAULT_STYLE | wx.NO_BORDER)

        imglist = wx.ImageList(16, 16, True, 2)
        imglist.Add(wx.ArtProvider.GetBitmap(wx.ART_FOLDER, wx.ART_OTHER, wx.Size(16, 16)))
        imglist.Add(wx.ArtProvider.GetBitmap(wx.ART_NORMAL_FILE, wx.ART_OTHER, wx.Size(16, 16)))
        tree.AssignImageList(imglist)

        root = tree.AddRoot("AUI Project", 0)
        items = []

        items.append(tree.AppendItem(root, "Item 1", 0))
        items.append(tree.AppendItem(root, "Item 2", 0))
        items.append(tree.AppendItem(root, "Item 3", 0))
        items.append(tree.AppendItem(root, "Item 4", 0))
        items.append(tree.AppendItem(root, "Item 5", 0))

        for item in items:
            tree.AppendItem(item, "Subitem 1", 1)
            tree.AppendItem(item, "Subitem 2", 1)
            tree.AppendItem(item, "Subitem 3", 1)
            tree.AppendItem(item, "Subitem 4", 1)
            tree.AppendItem(item, "Subitem 5", 1)

        tree.Expand(root)

        return tree


    def CreateSizeReportCtrl(self, width=80, height=80):

        ctrl = SizeReportCtrl(self, -1, wx.DefaultPosition, wx.Size(width, height), self._mgr)
        return ctrl

    def CreateRan_DandDCtrl(self):
        # pnl = wx.Panel(self)
        # DD.TestPanel(pnl,log)
        # pnl.Show()
        # item1 = wx.DropTarget

        obj = DD.FileDropPanel(self, log)
        #todo: add button for 'back to previous or default layout'
                 #remove the text menu
                 # resize the window for small rectangle
        return obj

    def CreateRan_PanelCtrl(self):
        # frame = wx.Frame(None, wx.ID_ANY, "Hello World")  # A Frame is a top-level window.
        # frame.Show(False)  # Show the frame.
        pnl = wx.Panel(self)

        ## ctrl = rNX.getMeFig()   #TODO: how to add fig to the panel
        # pnl.fig =

        zB.TestPanel(pnl, log)   #adding this example to the panel (panel type into panel parent)

        # DD.FileDropPanel(pnl,log)
        return pnl

    def CreateRan_TreeCtrl(self):

        win = Xtr.XMLTree(self,-1)
        win.LoadTree("./specific_files/example.xml")
        return  win

#######################

    def CreateHTMLCtrl(self, parent=None):

        if not parent:
            parent = self

        ctrl = wx.html.HtmlWindow(parent, -1, wx.DefaultPosition, wx.Size(400, 300))
        ctrl.SetPage(GetIntroText())
        return ctrl


    def CreateNotebook(self):

        # create the notebook off-window to avoid flicker
        client_size = self.GetClientSize()
        ctrl = aui.AuiNotebook(self, -1, wx.Point(client_size.x, client_size.y),
                              wx.Size(430, 200), agwStyle=self._notebook_style)

        arts = [aui.AuiDefaultTabArt, aui.AuiSimpleTabArt, aui.VC71TabArt, aui.FF2TabArt,
                aui.VC8TabArt, aui.ChromeTabArt]

        art = arts[self._notebook_theme]()
        ctrl.SetArtProvider(art)

        page_bmp = wx.ArtProvider.GetBitmap(wx.ART_NORMAL_FILE, wx.ART_OTHER, wx.Size(16, 16))
        ctrl.AddPage(self.CreateHTMLCtrl(ctrl), "Welcome to AUI", False, page_bmp)

        panel = wx.Panel(ctrl, -1)
        flex = wx.FlexGridSizer(0, 2)
        flex.Add((5, 5))
        flex.Add((5, 5))
        flex.Add(wx.StaticText(panel, -1, "wxTextCtrl:"), 0, wx.ALL|wx.ALIGN_CENTRE, 5)
        flex.Add(wx.TextCtrl(panel, -1, "", wx.DefaultPosition, wx.Size(100, -1)),
                 1, wx.ALL|wx.ALIGN_CENTRE, 5)
        flex.Add(wx.StaticText(panel, -1, "wxSpinCtrl:"), 0, wx.ALL|wx.ALIGN_CENTRE, 5)
        flex.Add(wx.SpinCtrl(panel, -1, "5", wx.DefaultPosition, wx.Size(100, -1),
                             wx.SP_ARROW_KEYS, 5, 50, 5), 0, wx.ALL|wx.ALIGN_CENTRE, 5)
        flex.Add((5, 5))
        flex.Add((5, 5))
        flex.AddGrowableRow(0)
        flex.AddGrowableRow(3)
        flex.AddGrowableCol(1)
        panel.SetSizer(flex)
        ctrl.AddPage(panel, "Disabled", False, page_bmp)

        ctrl.AddPage(wx.TextCtrl(ctrl, -1, "Some text", wx.DefaultPosition, wx.DefaultSize,
                                 wx.TE_MULTILINE|wx.NO_BORDER), "DClick Edit!", False, page_bmp)

        ctrl.AddPage(wx.TextCtrl(ctrl, -1, "Some more text", wx.DefaultPosition, wx.DefaultSize,
                                 wx.TE_MULTILINE|wx.NO_BORDER), "Blue Tab")

        ctrl.AddPage(wx.TextCtrl(ctrl, -1, "Some more text", wx.DefaultPosition, wx.DefaultSize,
                                 wx.TE_MULTILINE|wx.NO_BORDER), "A Control")

        ctrl.AddPage(wx.TextCtrl(ctrl, -1, "Some more text", wx.DefaultPosition, wx.DefaultSize,
                                 wx.TE_MULTILINE|wx.NO_BORDER), "wxTextCtrl 4")

        ctrl.AddPage(wx.TextCtrl(ctrl, -1, "Some more text", wx.DefaultPosition, wx.DefaultSize,
                                 wx.TE_MULTILINE|wx.NO_BORDER), "wxTextCtrl 5")

        ctrl.AddPage(wx.TextCtrl(ctrl, -1, "Some more text", wx.DefaultPosition, wx.DefaultSize,
                                 wx.TE_MULTILINE|wx.NO_BORDER), "wxTextCtrl 6")

        ctrl.AddPage(wx.TextCtrl(ctrl, -1, "Some more text", wx.DefaultPosition, wx.DefaultSize,
                                 wx.TE_MULTILINE|wx.NO_BORDER), "wxTextCtrl 7 (longer title)")

        ctrl.AddPage(wx.TextCtrl(ctrl, -1, "Some more text", wx.DefaultPosition, wx.DefaultSize,
                                 wx.TE_MULTILINE|wx.NO_BORDER), "wxTextCtrl 8")

        # Demonstrate how to disable a tab
        ctrl.EnableTab(1, False)

        ctrl.SetPageTextColour(2, wx.RED)
        ctrl.SetPageTextColour(3, wx.BLUE)
        ctrl.SetRenamable(2, True)

        return ctrl


    def OnSwitchPane(self, event):

        items = ASD.SwitcherItems()
        items.SetRowCount(12)

        # Add the main windows and toolbars, in two separate columns
        # We'll use the item 'id' to store the notebook selection, or -1 if not a page

        for k in xrange(2):
            if k == 0:
                items.AddGroup(_("Main Windows"), "mainwindows")
            else:
                items.AddGroup(_("Toolbars"), "toolbars").BreakColumn()

            for pane in self._mgr.GetAllPanes():
                name = pane.name
                caption = pane.caption
                if not caption:
                    continue

                toolBar = isinstance(pane.window, wx.ToolBar) or isinstance(pane.window, aui.AuiToolBar)
                bitmap = (pane.icon.IsOk() and [pane.icon] or [wx.NullBitmap])[0]

                if (toolBar and k == 1) or (not toolBar and k == 0):
                    items.AddItem(caption, name, -1, bitmap).SetWindow(pane.window)

        # Now add the wxAuiNotebook pages
        items.AddGroup(_("Notebook Pages"), "pages").BreakColumn()

        for pane in self._mgr.GetAllPanes():
            nb = pane.window
            if isinstance(nb, aui.AuiNotebook):
                for j in xrange(nb.GetPageCount()):

                    name = nb.GetPageText(j)
                    win = nb.GetPage(j)

                    items.AddItem(name, name, j, nb.GetPageBitmap(j)).SetWindow(win)

        # Select the focused window

        idx = items.GetIndexForFocus()
        if idx != wx.NOT_FOUND:
            items.SetSelection(idx)

        if wx.Platform == "__WXMAC__":
            items.SetBackgroundColour(wx.WHITE)

        # Show the switcher dialog

        dlg = ASD.SwitcherDialog(items, self, self._mgr)

        # In GTK+ we can't use Ctrl+Tab; we use Ctrl+/ instead and tell the switcher
        # to treat / in the same was as tab (i.e. cycle through the names)

        if wx.Platform == "__WXGTK__":
            dlg.SetExtraNavigationKey('/')

        if wx.Platform == "__WXMAC__":
            dlg.SetBackgroundColour(wx.WHITE)
            dlg.SetModifierKey(wx.WXK_ALT)

        ans = dlg.ShowModal()

        if ans == wx.ID_OK and dlg.GetSelection() != -1:
            item = items.GetItem(dlg.GetSelection())

            if item.GetId() == -1:
                info = self._mgr.GetPane(item.GetName())
                info.Show()
                self._mgr.Update()
                info.window.SetFocus()

            else:
                nb = item.GetWindow().GetParent()
                win = item.GetWindow()
                if isinstance(nb, aui.AuiNotebook):
                    nb.SetSelection(item.GetId())
                    win.SetFocus()

#----------------------------------------------------------------------

# class ParentFrame(aui.AuiMDIParentFrame):
#
#     def __init__(self, parent):
#
#         aui.AuiMDIParentFrame.__init__(self, parent, -1, title="AGW AuiMDIParentFrame",
#                                        size=(640,480), style=wx.DEFAULT_FRAME_STYLE)
#         self.count = 0
#
#         # set frame icon
#         self.SetIcon(images.Mondrian.GetIcon())
#
#         mb = self.MakeMenuBar()
#         self.SetMenuBar(mb)
#         self.CreateStatusBar()
#
#
#     def MakeMenuBar(self):
#
#         mb = wx.MenuBar()
#         menu = wx.Menu()
#         item = menu.Append(-1, "New child window\tCtrl-N")
#         self.Bind(wx.EVT_MENU, self.OnNewChild, item)
#         item = menu.Append(-1, "Close parent")
#         self.Bind(wx.EVT_MENU, self.OnDoClose, item)
#         mb.Append(menu, "&File")
#         return mb
#
#
#     def OnNewChild(self, evt):
#
#         self.count += 1
#         child = ChildFrame(self, self.count)
#         child.Show()
#
#
#     def OnDoClose(self, evt):
#         self.Close()


#----------------------------------------------------------------------

# class ChildFrame(aui.AuiMDIChildFrame):
#
#     def __init__(self, parent, count):
#
#         aui.AuiMDIChildFrame.__init__(self, parent, -1, title="Child: %d" % count)
#         mb = parent.MakeMenuBar()
#         menu = wx.Menu()
#         item = menu.Append(-1, "This is child %d's menu" % count)
#         mb.Append(menu, "&Child")
#         self.SetMenuBar(mb)
#
#         p = wx.Panel(self)
#         wx.StaticText(p, -1, "This is child %d" % count, (10,10))
#         p.SetBackgroundColour('light blue')
#
#         sizer = wx.BoxSizer()
#         sizer.Add(p, 1, wx.EXPAND)
#         self.SetSizer(sizer)
#
#         wx.CallAfter(self.Layout)


#---------------------------------------------------------------------------

def MainAUI(parent, log):

    frame = AuiFrame(parent, -1, "AUI Test Frame", size=(800, 600), log=log)
    # frame.CenterOnScreen()

    desiredFramePos = wx.Point(683, 384)
    desiredFramePos = wx.Point(2, 2)
    previousSize = frame.GetPosition()
    frame.SetPosition(desiredFramePos)
    # self.pos = (7
    frame.Show()


#---------------------------------------------------------------------------

# def MDIAUI(parent, log):
#
#     frame = ParentFrame(parent)
#     frame.CenterOnScreen()
#     frame.Show()

#---------------------------------------------------------------------------


# class TestPanel(wx.Panel):
#     def __init__(self, parent, log):
#         self.log = log
#         wx.Panel.__init__(self, parent, -1)
#
#         b1 = wx.Button(self, -1, " AGW AUI Docking Library ", (50,50))
#         self.Bind(wx.EVT_BUTTON, self.OnButton1, b1)
#
# ##        b2 = wx.Button(self, -1, " AGW AuiMDIs ", (50, 80))
# ##        self.Bind(wx.EVT_BUTTON, self.OnButton2, b2)
#
#
#     def OnButton1(self, event):
#         self.win = MainAUI(self, self.log)
#
#
#     def OnButton2(self, event):
#         self.win = MDIAUI(self, self.log)

#----------------------------------------------------------------------

# def runTest(frame, nb, log):
#
#     win = TestPanel(nb, log)
#     return win

#----------------------------------------------------------------------


overview = GetIntroText()

class Log:
    def WriteText(self, text):
        if text[-1:] == '\n':
            text = text[:-1]
        wx.LogMessage(text)
    write = WriteText

if __name__ == '__main__':
    # import sys,os
    # import run
    # run.main(['', os.path.basename(sys.argv[0])] + sys.argv[1:])
    app = wx.App(False)  # Create a new app, don't redirect stdout/stderr to a window.
    frame = wx.Frame(None, wx.ID_ANY, "Hello World")  # A Frame is a top-level window.
    frame.Show(False)  # Show the frame.
    pnl = wx.Panel(frame)
    log = Log()

    win = MainAUI(pnl, log)
    app.MainLoop()
    pass