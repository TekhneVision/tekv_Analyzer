'''
Created on Jan 14, 2018

@author: Jerime Cortes
'''
import json
import csv
import iteratorUtil as util


# Retrieve path for the data files to be analyzed.
def _getDataFileConfig():
    with open('dataFileConfig.json', 'r') as jsonFile:
        return json.load(jsonFile)
            
# Open the file and return as list.
def _openFile(filePath):
    f = open(filePath, 'r')
    return list(csv.reader(f))
    

# Retrieve a list with file 1 data.              
def getFileData(fileId, requestType): # fileId is json parent id and Request type is either 'file' or 'header'
    jsonData = _getDataFileConfig()
    pathData = jsonData[fileId]
            
    filePath = pathData['path'] + pathData[requestType]    
    fileList = _openFile(filePath) 
    
    if requestType == 'header':        
        return util.unwrapListOfLists(fileList)
    else:
        return util.unwrapList(fileList)

       
   


