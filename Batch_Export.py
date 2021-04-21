aprx=arcpy.mp.ArcGISProject("CURRENT")
#grabs from tool window in arcgis pro
outfolder=arcpy.GetParameterAsText(0) #which folder to save
filetype=arcpy.GetParameterAsText(1) #which file type to save
try:
    for lyt in aprx.listLayouts():
        if filetype=="pdf":
            lyt.exportToPDF(outfolder+'\\'+lyt.name+'.pdf')
        elif filetype=='png':
            lyt.exportToPNG(outfolder+'\\'+lyt.name+'.png')
        else:
            print("File type is not supported")
    print("Layouts exported")
except Exception as e:
    print(e)
