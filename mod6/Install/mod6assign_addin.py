import arcpy
import pythonaddins
import os

class addLayer(object):
    """Implementation for mod6assign_addin.addLayer (ComboBox)"""
    def __init__(self):
        self.items = ["item1", "item2"]
        self.editable = True
        self.enabled = True
        self.dropdownWidth = 'WWWWWW'
        self.width = 'WWWWWW'
    def onSelChange(self, selection):
		# List all data frames controlled by selector string at the end. This returns a list even if only one is selected thus index is at 0 for the array
		findFrame = arcpy.mapping.ListDataFrames(self.mxd,"Crime")[0]
		# Creates a Layer object from path
		addLyr = arcpy.mapping.Layer(selection)
		# Finds the data frame -> adds the layer -> allow the new layer to be grouped with similar feature classes
		arcpy.mapping.AddLayer(findFrame, addLyr, "TOP")
		arcpy.RefreshActiveView()
    def onEditChange(self, text):
        pass
    def onFocus(self, focused):
        if focused:
		# Sets the variable for the map document (.mxd)
		self.mxd = arcpy.mapping.MapDocument("CURRENT")
		findFrame = arcpy.mapping.ListDataFrames(self.mxd,"Crime")[0]
		layers = arcpy.mapping.ListLayers(self.mxd,"",findFrame)
		self.items = []
		for layer in layers:
			self.items.append(layer.name)
    def onEnter(self):
        pass
    def refresh(self):
        pass

class delLayer(object):
    """Implementation for mod6assign_addin.delLayer (ComboBox)"""
    def __init__(self):
        self.items = ["item1", "item2"]
        self.editable = True
        self.enabled = True
        self.dropdownWidth = 'WWWWWW'
        self.width = 'WWWWWW'
    def onSelChange(self, selection):
		# for each data frome from all frames available...
		for delFram in arcpy.mapping.ListDataFrames(self.mxd):
			# Prints out each frame's name as the for loop progresses
			arcpy.AddMessage(delFram.name)
			# for each layer in each data frame...
			for thislyr in arcpy.mapping.ListLayers(self.mxd,"",delFram):
				# If a layer matches the file name, file path, or layer name...
				if thislyr.name == selection:
					# Gives the user the name of the layer then deletes the layer		
					arcpy.AddMessage(thislyr.name)
					arcpy.mapping.RemoveLayer(delFram, thislyr)
		arcpy.RefreshActiveView()
    def onEditChange(self, text):
        pass
    def onFocus(self, focused):
		if focused:
# Sets the variable for the map document (.mxd)
			self.mxd = arcpy.mapping.MapDocument("CURRENT")
			findFrame = arcpy.mapping.ListDataFrames(self.mxd,"Crime")[0]
			layers = arcpy.mapping.ListLayers(self.mxd,"",findFrame)
			self.items = []
			for layer in layers:
				self.items.append(layer.name)
    def onEnter(self):
        pass
    def refresh(self):
        pass

class pdfMake(object):
    """Implementation for mod6assign_addin.pdfMaker (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        # Splits path from user input, creates output path
		saveDataPath = pythonaddins.SaveDialog()
		self.mxd = arcpy.mapping.MapDocument("CURRENT")
		crimeInsetFrame = arcpy.mapping.ListDataFrames(self.mxd, "Crime_Inset")[0]
		# Creates a pdf from user input. PDF has control variable of only printing the Crime_Inset.
		arcpy.mapping.ExportToPDF(self.mxd, saveDataPath, crimeInsetFrame)