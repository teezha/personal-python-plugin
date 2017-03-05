import arcpy
import pythonaddins
import os

import datetime


class btnHelp(object):
    """Implementation for mod78_addin.btnHelp (Button)"""

    def __init__(self):
        self.mxd = arcpy.mapping.MapDocument("CURRENT")
        self.enabled = True
        self.checked = False

    def onClick(self):
        pythonaddins.MessageBox(
            "Drop Down Box: Select Crimes based on Region Chosen\nSelect Crimes Tool: Use mouse to draw rectangle on map\nAdd Table and Export: Adds Summary table to layout and Exports to jpg\nUpdate Name and Date: Adds Author name and today's date",
            "Help")


class btnSumTable(object):
    """Implementation for mod78_addin.btnSumTable (Button)"""

    def __init__(self):
        self.mxd = arcpy.mapping.MapDocument("CURRENT")
        self.enabled = True
        self.checked = False

    def onClick(self):
        pass


class btnUpdate(object):
    """Implementation for mod78_addin.btnUpdate (Button)"""

    def __init__(self):
        self.mxd = arcpy.mapping.MapDocument("CURRENT")
        self.enabled = True
        self.checked = False

    def onClick(self):
        authText = '"Author: Toby Zhang\n' + datetime.datetime.today().strftime("%B %d, %Y") + '"'
        for elem in arcpy.mapping.ListLayoutElements(self.mxd, "TEXT_ELEMENT"):
            if elem.name == "CrimeAuthor":
                elem.text = authText


class cbPolZone(object):
    """Implementation for mod78_addin.cbPolZone (ComboBox)"""

    def __init__(self):
        self.mxd = arcpy.mapping.MapDocument("CURRENT")
        self.items = ["West End", "East End", "West Side"]
        self.editable = True
        self.enabled = True
        self.dropdownWidth = 'WWWWWWWWWWWW'
        self.width = 'WWWWWWWWWWWW'

    def onSelChange(self, selection):
        query = """ "REGION" = '%s'""" % str(selection)
        findFrame = arcpy.mapping.ListDataFrames(self.mxd, "Crime")[0]
        layer = arcpy.mapping.ListLayers(self.mxd, "", findFrame)
        arcpy.SelectLayerByAttribute_management(layer, "CLEAR_SELECTION")
        arcpy.SelectLayerByAttribute_management(layer, "NEW_SELECTION", query)
        arcpy.SelectLayerByLocation_management("crime95", "WITHIN", layer, "", "SUBSET_SELECTION")

    def onEditChange(self, text):
        pass

    def onFocus(self, focused):
        pass

    def onEnter(self):
        pass

    def refresh(self):
        pass


class toolToPolygon(object):
    """Implementation for mod78_addin.toolToPolygon (Tool)"""

    def convertCoords(x, y):
        thisMap = arcpy.mapping.MapDocument("CURRENT")
        dataFrame = arcpy.mapping.ListDataFrames(thisMap)[0]
        pageX = x
        pageY = y
        df_page_w = dataFrame.elementWidth
        df_page_h = dataFrame.elementHeight
        df_page_x_min = dataFrame.elementPositionX
        df_page_y_min = dataFrame.elementPositionY
        df_page_x_max = df_page_w + df_page_x_min
        df_page_y_max = df_page_h + df_page_y_min

        df_min_x = dataFrame.extent.XMin
        df_min_y = dataFrame.extent.YMin
        df_max_x = dataFrame.extent.XMax
        df_max_y = dataFrame.extent.YMax
        df_proj_w = dataFrame.extent.width
        df_proj_h = dataFrame.extent.height

        if pageX < df_page_x_min or pageX > df_page_x_max:
            pythonaddins.MessageBox('X coordinates are not within map portion of the page.', "Out of Bounds")
            return 0, 0
        if pageY < df_page_y_min or pageY > df_page_y_max:
            pythonaddins.MessageBox('Y coordinates are not within map portion of the page.', "Out of Bounds")
            return 0, 0

        scale = dataFrame.scale / 39.3701
        map_x = df_min_x + ((pageX - df_page_x_min) * scale)
        map_y = df_min_y + ((pageY - df_page_y_min) * scale)

        return map_x, map_y

    def __init__(self):
        self.mxd = arcpy.mapping.MapDocument("CURRENT")
        self.enabled = True
        self.shape = "NONE"  # Can set to "Line", "Circle" or "Rectangle" for interactive shape drawing and to activate the onLine/Polygon/Circle event sinks.

    def onMouseDown(self, x, y, button, shift):
        pass

    def onMouseDownMap(self, x, y, button, shift):
        pass

    def onMouseUp(self, x, y, button, shift):
        pass

    def onMouseUpMap(self, x, y, button, shift):
        pass

    def onMouseMove(self, x, y, button, shift):
        pass

    def onMouseMoveMap(self, x, y, button, shift):
        pass

    def onDblClick(self):
        pass

    def onKeyDown(self, keycode, shift):
        pass

    def onKeyUp(self, keycode, shift):
        pass

    def deactivate(self):
        pass

    def onCircle(self, circle_geometry):
        pass

    def onLine(self, line_geometry):
        pass

    def onRectangle(self, rectangle_geometry):
        pass
