#IMPORTANT: Ensure that no features in "Airfield Sign" are selected


layer=arcpy.GetParameterAsText(0) #featuredataset
fields=["OBJECTID","GlobalID"]
fields_attach=["REL_GLOBALID","CONTENT_TYPE"]
at_table=arcpy.GetParameterAsText(1) #attachment table

list_jpg=[]
list_null=[]
filetype=arcpy.GetParameterAsText(2)

with arcpy.da.SearchCursor(layer,fields) as cursor:
    for row in cursor:#iter over main layer
        with arcpy.da.SearchCursor(at_table,fields_attach) as cursor_a: #searches attach table utilizing attachment columns
            for row_a in cursor_a: #iter over attachment table
                if row[1]==row_a[0]:
                    if row_a[1]== filetype:
                        if row[0] in list_jpg:
                            continue
                        else:
                            list_jpg.append(row[0])
with arcpy.da.SearchCursor(layer,fields)as cursor:
    for row in cursor:
        if row[0] not in list_jpg:
            list_null.append(row[0])
                    
arcpy.AddMessage(f'ObjectID that have jpg attachments are: {list_jpg}')
arcpy.AddMessage(f'ObjectID that do not have jpg attachments are: {list_null}')     
